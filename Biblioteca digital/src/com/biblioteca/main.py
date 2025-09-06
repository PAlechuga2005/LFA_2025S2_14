from servicio_biblioteca import BibliotecaService
import generador_reportes as reportes

def mostrar_menu():
    print("\nMENÚ BIBLIOTECA DIGITAL")
    print(" 1. Cargar usuarios")
    print(" 2. Cargar libros")
    print(" 3. Cargar registro de préstamos desde archivo")
    print(" 4. Mostrar historial de préstamos")
    print(" 5. Mostrar listado de usuarios únicos")
    print(" 6. Mostrar listado de libros prestados")
    print(" 7. Mostrar estadísticas de préstamos")
    print(" 8. Mostrar préstamos vencidos")
    print(" 9. Exportar todos los reportes a HTML")
    print("10. Salir")

def main():
    """Función principal que ejecuta el bucle del menú."""
    servicio = BibliotecaService()
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if not servicio.datos_cargados and opcion not in ["1", "2", "3", "10"]:
            print("\nPrimero necesitas cargar un archivo de préstamos (Opción 3)")
            continue

        #Menú
        if opcion == "1":
            print("\nNota: Los usuarios se cargan automáticamente desde el archivo de préstamos.")
        
        elif opcion == "2":
            print("\nNota: Los libros se cargan automáticamente desde el archivo de préstamos.")

        elif opcion == "3":
            ruta = input("Ingresa la ruta del archivo: ")
            servicio.cargar_prestamos(ruta)
        
        elif opcion == "4":
            print("\nHistorial de Préstamos")
            for p in servicio.get_historial_completo(): print(p)
        
        elif opcion == "5":
            print("\nUsuarios Únicos")
            for u in sorted(servicio.get_usuarios_unicos(), key=lambda x: x.nombre_usuario):
                print(f"ID: {u.id_usuario}, Nombre: {u.nombre_usuario}")

        elif opcion == "6":
            print("\nLibros Únicos")
            for l in sorted(servicio.get_libros_unicos(), key=lambda x: x.titulo_libro):
                print(f"ID: {l.id_libro}, Título: {l.titulo_libro}")

        elif opcion == "7":
            print("\nEstadísticas")
            stats = servicio.get_estadisticas()
            if stats:
                for k, v in stats.items(): print(f"{k}: {v}")

        elif opcion == "8":
            print("\nPréstamos Vencidos")
            vencidos = servicio.get_prestamos_vencidos()
            if not vencidos:
                print("No hay préstamos vencidos.")
            for p in vencidos:
                print(f"Usuario: {p.nombre_usuario}, Libro: {p.titulo_libro}, Devolución: {p.fecha_devolucion}")
        
        elif opcion == "9":
            print("\nGenerando reportes HTML...")
            
            # 1. Historial
            html_historial = reportes.generar_html_historial(servicio.get_historial_completo())
            reportes.guardar_reporte("1_historial.html", html_historial)
            
            # 2. Usuarios
            html_usuarios = reportes.generar_html_usuarios(servicio.get_usuarios_unicos())
            reportes.guardar_reporte("2_usuarios.html", html_usuarios)

            # 3. Libros
            html_libros = reportes.generar_html_libros(servicio.get_libros_unicos())
            reportes.guardar_reporte("3_libros.html", html_libros)

            # 4. Estadísticas
            html_stats = reportes.generar_html_estadisticas(servicio.get_estadisticas())
            reportes.guardar_reporte("4_estadisticas.html", html_stats)

            # 5. Vencidos
            html_vencidos = reportes.generar_html_vencidos(servicio.get_prestamos_vencidos())
            reportes.guardar_reporte("5_vencidos.html", html_vencidos)

            print("\nReportes generados")

        elif opcion == "10":
            print("\nAdios...")
            break
        
        else:
            print("\nOpción no válida.")

# --- Punto de entrada del programa ---
if __name__ == "__main__":
    main()
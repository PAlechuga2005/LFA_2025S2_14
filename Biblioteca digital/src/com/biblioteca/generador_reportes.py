from typing import List, Set, Dict, Optional
from modelo import Prestamo, Usuario, Libro

# Plantilla

def _get_encabezado_html(titulo: str) -> str:
    """Devuelve el encabezado y estilos CSS para los reportes HTML."""
    return f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{titulo}</title>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; margin: 25px; background-color: #f9f9f9; }}
        h1 {{ color: #0056b3; border-bottom: 2px solid #0056b3; padding-bottom: 10px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        th, td {{ border: 1px solid #ccc; padding: 12px; text-align: left; }}
        th {{ background-color: #007bff; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
        tr:hover {{ background-color: #e9ecef; }}
    </style>
</head>
<body>
    <h1>{titulo}</h1>
"""

def _get_pie_html() -> str:
    """Devuelve el cierre de las etiquetas HTML."""
    return "</body></html>"

def guardar_reporte(nombre_archivo: str, contenido_html: str):
    """Guarda el contenido HTML en un archivo de texto."""
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(contenido_html)
        print(f"Reporte '{nombre_archivo}' generado con éxito.")
    except IOError as e:
        print(f"Error: No se pudo guardar el archivo {nombre_archivo}: {e}")

# Generador de  cada Reporte

def generar_html_historial(prestamos: List[Prestamo]) -> str:
    """Genera el HTML para el historial completo de préstamos."""
    html = _get_encabezado_html("Historial de Préstamos")
    html += "<table><tr><th>Usuario</th><th>Libro</th><th>Fecha Préstamo</th><th>Fecha Devolución</th></tr>"
    for p in prestamos:
        devolucion = p.fecha_devolucion.isoformat() if p.fecha_devolucion else "<strong>No Devuelto</strong>"
        html += f"<tr><td>{p.nombre_usuario}</td><td>{p.titulo_libro}</td><td>{p.fecha_prestamo.isoformat()}</td><td>{devolucion}</td></tr>"
    html += "</table>" + _get_pie_html()
    return html

def generar_html_usuarios(usuarios: Set[Usuario]) -> str:
    """Genera el HTML para el listado de usuarios únicos."""
    html = _get_encabezado_html("Listado de Usuarios Únicos")
    html += "<table><tr><th>ID Usuario</th><th>Nombre de Usuario</th></tr>"
    # Convertimos el set a lista para poder ordenarlo
    for u in sorted(list(usuarios), key=lambda usr: usr.nombre_usuario):
        html += f"<tr><td>{u.id_usuario}</td><td>{u.nombre_usuario}</td></tr>"
    html += "</table>" + _get_pie_html()
    return html

def generar_html_libros(libros: Set[Libro]) -> str:
    """Genera el HTML para el listado de libros únicos."""
    html = _get_encabezado_html("Listado de Libros Prestados")
    html += "<table><tr><th>ID Libro</th><th>Título del Libro</th></tr>"
    for l in sorted(list(libros), key=lambda lib: lib.titulo_libro):
        html += f"<tr><td>{l.id_libro}</td><td>{l.titulo_libro}</td></tr>"
    html += "</table>" + _get_pie_html()
    return html

def generar_html_estadisticas(estadisticas: Optional[Dict[str, str]]) -> str:
    """Genera el HTML para las estadísticas."""
    html = _get_encabezado_html("Estadísticas de Préstamos")
    html += "<table><tr><th>Métrica</th><th>Valor</th></tr>"
    if estadisticas:
        for metrica, valor in estadisticas.items():
            html += f"<tr><td>{metrica}</td><td>{valor}</td></tr>"
    else:
        html += "<tr><td colspan='2'>No hay datos para mostrar.</td></tr>"
    html += "</table>" + _get_pie_html()
    return html

def generar_html_no_devueltos(prestamos: List[Prestamo]) -> str:
    """Genera el HTML para los préstamos que aún no han sido devueltos."""
    html = _get_encabezado_html("Préstamos No Devueltos")
    html += "<table><tr><th>Usuario</th><th>Libro</th><th>Fecha de Préstamo</th></tr>"
    for p in sorted(prestamos, key=lambda pr: pr.fecha_prestamo):
        html += f"<tr><td>{p.nombre_usuario}</td><td>{p.titulo_libro}</td><td>{p.fecha_prestamo.isoformat()}</td></tr>"
    html += "</table>" + _get_pie_html()
    return html

def generar_html_vencidos(prestamos: List[Prestamo]) -> str:
    """Genera el HTML para los préstamos cuya fecha de devolución ya pasó."""
    html = _get_encabezado_html("Préstamos Vencidos")
    html += "<table><tr><th>Usuario</th><th>Libro</th><th>Fecha de Devolución</th></tr>"
    if not prestamos:
        html += "<tr><td colspan='3'>No se encontraron préstamos vencidos.</td></tr>"
    else:
        for p in sorted(prestamos, key=lambda pr: pr.fecha_devolucion):
            html += f"<tr><td>{p.nombre_usuario}</td><td>{p.titulo_libro}</td><td>{p.fecha_devolucion.isoformat()}</td></tr>"
    html += "</table>" + _get_pie_html()
    return html
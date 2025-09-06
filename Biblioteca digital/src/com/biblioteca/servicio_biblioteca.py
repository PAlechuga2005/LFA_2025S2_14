# servicio_biblioteca.py

from collections import Counter
from datetime import date
from typing import List, Set, Dict, Optional
from modelo import Prestamo, Usuario, Libro
from lector_lfa import leer_archivo_lfa

class BibliotecaService:
    """Gestiona toda la lógica de negocio de la biblioteca."""
    
    def __init__(self):
        self._prestamos: List[Prestamo] = []

    def cargar_prestamos(self, ruta_archivo: str):
        """Carga los registros de préstamos desde un archivo .lfa."""
        self._prestamos = leer_archivo_lfa(ruta_archivo)
        if self._prestamos:
            print(f"\nSe cargaron con exito los {len(self._prestamos)} registros.")
        else:
            print("\n No se cargó ningún registro. Revisa el archivo o los mensajes de error.")

    @property
    def datos_cargados(self) -> bool:
        """Devuelve True si hay préstamos cargados en memoria."""
        return bool(self._prestamos)

    def get_historial_completo(self) -> List[Prestamo]:
        return self._prestamos

    def get_usuarios_unicos(self) -> Set[Usuario]:
        return {Usuario(p.id_usuario, p.nombre_usuario) for p in self._prestamos}

    def get_libros_unicos(self) -> Set[Libro]:
        return {Libro(p.id_libro, p.titulo_libro) for p in self._prestamos}

    # PRÉSTAMOS VENCIDOS
    def get_prestamos_vencidos(self) -> List[Prestamo]:
        hoy = date.today()
        # Se filtran los préstamos que tienen una fecha de devolución y esta es anterior a hoy.
        return [p for p in self._prestamos if p.fecha_devolucion is not None and p.fecha_devolucion < hoy]

    def get_estadisticas(self) -> Optional[Dict[str, str]]:
        if not self._prestamos:
            return None
        
        conteo_libros = Counter(p.titulo_libro for p in self._prestamos)
        conteo_usuarios = Counter(p.nombre_usuario for p in self._prestamos)
        
        return {
            "Total de Préstamos": str(len(self._prestamos)),
            "Total de Usuarios Únicos": str(len(self.get_usuarios_unicos())),
            "Libro Más Prestado": conteo_libros.most_common(1)[0][0],
            "Usuario Más Activo": conteo_usuarios.most_common(1)[0][0],
        }
from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass(frozen=True)
class Usuario:
    """Representa a un usuario único. 'frozen=True' hace que no se pueda modificar,
    y permite que lo usemos en 'sets' para eliminar duplicados."""
    id_usuario: int
    nombre_usuario: str

@dataclass(frozen=True)
class Libro:
    """Representa a un libro único."""
    id_libro: str
    titulo_libro: str

@dataclass
class Prestamo:
    """Representa una línea de préstamo del archivo .lfa."""
    id_usuario: int
    nombre_usuario: str
    id_libro: str
    titulo_libro: str
    fecha_prestamo: date
    fecha_devolucion: Optional[date] = None
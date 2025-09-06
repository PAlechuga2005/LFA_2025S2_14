# lector_lfa.py

import sys
from datetime import date
from typing import List
from modelo import Prestamo

def leer_archivo_lfa(ruta_archivo: str) -> List[Prestamo]:

    prestamos = []
    
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()[1:]
            
            for num_linea, linea_actual in enumerate(lineas, start=2):
                
                if not linea_actual.strip():
                    continue

                campos = linea_actual.strip().split(',')
                
                if len(campos) not in [5, 6]:
                    print(f"Error en línea {num_linea}: Número de campos incorrecto (se esperaban 5 o 6).", file=sys.stderr)
                    continue

                try:
                    id_usuario = int(campos[0])
                    nombre_usuario = campos[1]
                    id_libro = campos[2]
                    titulo_libro = campos[3]
                    fecha_prestamo = date.fromisoformat(campos[4])
                    
                    fecha_devolucion = None
                    # Si existe el sexto campo y no está vacío, lo procesamos
                    if len(campos) == 6 and campos[5]:
                        fecha_devolucion = date.fromisoformat(campos[5])

                    # Si todo  bien, creamos el objeto y lo agregamos a la lista
                    prestamos.append(Prestamo(
                        id_usuario, nombre_usuario, id_libro, titulo_libro,
                        fecha_prestamo, fecha_devolucion
                    ))

                except ValueError:
                    print(f"Error en línea {num_linea}: El ID de usuario o una fecha no tienen el formato correcto.", file=sys.stderr)
                except Exception as e:
                    print(f"Error inesperado en línea {num_linea}: {e}", file=sys.stderr)

    except FileNotFoundError:
        print(f"Error No se encontró el archivo en la ruta: {ruta_archivo}", file=sys.stderr)
    except Exception as e:
        print(f"Error No se pudo leer el archivo: {e}", file=sys.stderr)
        
    return prestamos
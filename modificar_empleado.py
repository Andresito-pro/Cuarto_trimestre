from typing import Tuple, List
from dataclasses import dataclass

#Exepción de los errores

class ListaEmpleadosVaciaError(Exception):
    pass

#Validación de los datos
def validar_datos_empleado(nombre: str, cargo: str, salario: float):
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre debe ser un texto válido y no vacío")
    if not isinstance(cargo, str) or not cargo.strip():
        raise ValueError("El cargo debe ser un texto válido")
    if not isinstance(salario, (int,float)):
        raise TypeError("El salario debe ser numerico")
    if salario <= 0:
        raise ValueError("El salario debe ser mayor a cero")


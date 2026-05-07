from typing import Tuple, List
from dataclasses import dataclass

class ListaEmpleadosVacioError(Exception):
    pass

def _validar_datos_empleado(nombre: str, cargo: str, salario: float) -> None:
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre debe ser un texto no vacío y válido")
    if not isinstance(cargo, str) or not cargo.strip():
        raise ValueError("El cargo debe ser un texto no vacío y válido")
    if not isinstance(salario, (int, float)):
        raise TypeError("El salario debe ser un valor numérico")
    if salario <= 0:
        raise ValueError("El salario debe ser mayor a 0")

def registrar_empleado(nombre: str, cargo: str, salario: float) -> Tuple[str, str, float]:
    _validar_datos_empleado(nombre, cargo, salario)
    return (
        nombre.strip().title(),
        cargo.strip().title(), 
        float(salario)
    )
    
@dataclass
class ResultadoRegistro:
    empleados: List[Tuple[str, str, float]]
    errores: List[str]

def registrar_empleados(datos: List[Tuple[str, str, float]]) -> ResultadoRegistro:
    empleados_registrados = []
    errores_encontrados = []
    
    for nombre, cargo, salario in datos:
        try:
            # Llamamos a la función en singular para procesar cada uno
            empleado = registrar_empleado(nombre, cargo, salario)
            empleados_registrados.append(empleado)
        except (ValueError, TypeError) as error:
            errores_encontrados.append(f"Error con {nombre}: {str(error)}")
            
    return ResultadoRegistro(empleados=empleados_registrados, errores=errores_encontrados)

def mostrar_empleados(empleados: List[Tuple[str, str, float]]) -> None:
    if not empleados:
        raise ListaEmpleadosVacioError("No existen empleados para mostrar")
    
    print("\nRegistro de contratos laborales:")
    for indice, (nombre, cargo, salario) in enumerate(empleados, start=1):
        print(f"{indice} -> {nombre} - {cargo} - ${salario:,.2f}")

def main() -> None:
    
    datos_empleados = [
        ("Juan Perez", "Desarrollador", 5000.00),
        ("Maria Gomez", "Diseñadora", 4500.00),
        ("", "Analista", 4800.00),        
        ("Ana Rodriguez", "Gerente", -100), 
        ("Luis Fernandez", "Tester", 4000.00)
    ]
    
    resultado = registrar_empleados(datos_empleados)
    
    if resultado.empleados:
        mostrar_empleados(resultado.empleados)
        
    if resultado.errores:
        print("\nErrores encontrados durante el registro:")
        for error in resultado.errores:
            print(f"- {error}")
    
if __name__ == "__main__":    
    main()
# REEMPLAZA TODO EN conexion.py CON ESTO:
import psycopg

def conectar():
    try:
        conexion = psycopg.connect(
            host = "localhost", 
            dbname = "sena_adso",
            user = "postgres",
            password = "root",
            port = 5432
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
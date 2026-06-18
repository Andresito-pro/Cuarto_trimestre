import psycopg

try:
    conexion = psycopg.connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",  
        password = "root",
        port = 5432
    )
    conexion.autocommit = True
    cursor = conexion.cursor()
    cursor.execute("CREATE DATABASE sena_adso")
    print("Base de datos creada exitosamente")
    
except Exception as e:
    print(f"Ocurrió un error: {e}")


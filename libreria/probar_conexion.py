#Pip install psycopg[binary]
import psycopg
try:
    conexion = psycopg.connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",
        password = "root",
        port = 5432
    )
    print("La conexión a la base de datos ha sido exitosa")
    conexion.close()
except Exception as e:
    print(f"Error al conectar: {e}")
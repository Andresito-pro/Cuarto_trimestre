import psycopg

def conectar():
    try:
        conexion = psycopg.connect(
            host="localhost",
            dbname="chickenbiker_db",
            user="postgres",
            password="root",
            port=5432
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a ChickenBiker: {e}")
        return None
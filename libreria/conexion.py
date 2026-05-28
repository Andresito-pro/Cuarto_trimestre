import psycopg
def conectar():
    try:
        conexion = psycopg.connect(
            host = "localhost",
            dbname = "libreria",
            user = "postgres",
            password = "root",
            port = 5432
    )
        return conexion
    except Exception as e:
        print("Error de conexión",e)
        return None
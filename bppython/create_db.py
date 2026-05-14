import psycopg

conexion = psycopg.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="root",
    port=5432
)

conexion.autocommit = True
cursor = conexion.cursor()


cursor.execute("CREATE DATABASE IF NOT EXISTS sena_adso")
print("Base de datos verificada/creada")
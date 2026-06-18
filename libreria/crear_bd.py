import psycopg
try:
    conexion = psycopg.connect(
        host = "localhost",
        dbname = "libreria",
        user = "postgres",
        password = "root",
        port = 5432
    )

#Codigo para crear a base de datos
    conexion.autocommit = True
    cursor = conexion.cursor()
    #crear la BD
    cursor.execute("CREATE DATABASE libreria") # query pra crear la BD libreria
    print("Base de datos creada")
    conexion.close()
except Exception as e:
    print(e)
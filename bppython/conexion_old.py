#Instalar primero 
#pip install "psgcopg[binary]"

import psycopg
try:
    conexion = psycopg.connect(
        host = "localhost", 
        dbname = "postgres",
        user = "postgres",
        password = "root",
        port = 5432
    )
    print("La conexión a la BD fue exitosa")
    conexion.close()
except Exception as e:
    print("Error")
    print(e)
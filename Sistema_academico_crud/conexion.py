#instalar primero 
#pip install "psycopg [binary]"
import psycopg
try:
    conexion = psycopg.connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",
        password = "root",
        port = 5432
    )
    print ("La conexion es exitosa")
    conexion.clase()

except Exception as e:
    print ("Error")
    print (e)
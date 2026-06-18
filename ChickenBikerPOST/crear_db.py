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

cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'chickenbiker_db'")
print("Base de datos creada exitosamente.")
import psycopg

conexion = psycopg.connect(
        host = "localhost",
        dbname = "libreria",
        user = "postgres",
        password = "root",
        port = 5432
    )

cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS libro (
        id SERIAL PRIMARY KEY,
        titulo VARCHAR(100) NOT NULL,
        autor VARCHAR(100) NOT NULL
    )
''')

conexion.commit()
print("Tabla creada correctamente")
cursor.close()
conexion.close()
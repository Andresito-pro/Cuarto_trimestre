import psycopg

conexion = psycopg.connect(
    host = "localhost",
    dbname = "sena_adso",
    user = "postgres",
    password = "root",
    port = 5432
)

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS aprendices(
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        ficha VARCHAR(50),
        programa VARCHAR(100)
    )
''')


conexion.commit()
print("Tabla creada correctamente")
conexion.close()
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
    CREATE TABLE IF NOT EXISTS ambiente(
        id SERIAL PRIMARY KEY,
        nombreAmbiente VARCHAR(100),
        ubicacionAmbiente VARCHAR(100)
    )
''')

conexion.commit()
print("Tabla creada correctamente")
conexion.close()
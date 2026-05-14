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
    CREATE TABLE IF NOT EXISTS instructor(
        id SERIAL PRIMARY KEY,
        nombreInstructor VARCHAR(100),
        apellidoInstructor VARCHAR(100),
        tipoDocumento VARCHAR(100),
        documento VARCHAR(100),
        ocupacion VARCHAR(100)
    )
''')

conexion.commit()
print("Tabla creada correctamente")
conexion.close()

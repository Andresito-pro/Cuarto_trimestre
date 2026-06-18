import psycopg
conexion = psycopg.connect (
        host = "localhost",
        dbname = "sena_adso",
        user = "postgres",
        password = "root",
        port = 5432
    )   
cursor = conexion.cursor ()
cursor.execute ('''
CREATE TABLE IF NOT EXISTS  ambientes(
                    id SERIAL PRIMARY KEY,
                    nombre_ambiente VARCHAR (100),
                    ubicacion VARCHAR (50)
                )
'''   )
conexion.commit()
print ("Tabla creada correctamente")
cursor.close()
conexion.close()



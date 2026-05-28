from conexion import conectar
conexion = conectar()
cursor = conexion.cursor()

sql = """
CREATE TABLE IF NOT EXISTS prestamo(
    id SERIAL PRIMARY KEY,
    libro_id INTEGER NOT NULL,
    usuario VARCHAR(100) NOT NULL,
    fecha_prestamo TIMESTAMP NOT NULL,
    CONSTRAINT fk_libro
        FOREIGN KEY (libro_id)
        REFERENCES libro(id)
        ON DELETE CASCADE
)
"""
try:
    cursor.execute(sql)
    conexion.commit()
    print("Tabla prestamo creada correctamente.")
except Exception as e:
    conexion.rollback()
    print("Error: ", e)
finally:
    cursor.close()
    conexion.close
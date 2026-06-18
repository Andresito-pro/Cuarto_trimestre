from conexion import conectar

def crear_tabla_tipos_documento():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        
        # Creamos la tabla con un ID autoincremental y los campos correspondientes
        sql = """
        CREATE TABLE IF NOT EXISTS TipoDocumento (
            id_tp_doc INT AUTO_INCREMENT PRIMARY KEY,
            nombreTpDoc VARCHAR(10) NOT NULL,
            descripcionTpDoc VARCHAR(100) NOT NULL
        );
        """
        
        try:
            cursor.execute(sql)
            print("¡Éxito! La tabla 'TipoDocumento' ha sido verificada o creada correctamente.")
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    crear_tabla_tipos_documento()
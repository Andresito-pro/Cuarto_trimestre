from conexion import conectar

def crear_tabla_tipoDocumento():
    conexion = conectar()
    
    if conexion:
        cursor = conexion.cursor()
        

        sql = """
        CREATE TABLE IF NOT EXISTS TipoDocumento (
            idTipoDocumento INT AUTO_INCREMENT PRIMARY KEY,
            nombreTpDoc VARCHAR(50) NOT NULL UNIQUE,
            descripcionTpDoc VARCHAR(255) NOT NULL
        )
        """
        
        try:
            cursor.execute(sql)
            print("Tabla 'tipoDocumento' creada correctamente (o ya existía).")
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    crear_tabla_tipoDocumento()
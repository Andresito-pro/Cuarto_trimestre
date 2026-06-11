
from conexion import conectar

def insertar_tipos_documento():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        
        tipos_data = [
            ("CC", "Cédula de Ciudadanía"),
            ("TI", "Tarjeta de Identidad"),
            ("CE", "Cédula de Extranjería")
        ]
        
        sql = "INSERT INTO TipoDocumento (nombreTpDoc, descripcionTpDoc) VALUES (%s, %s)"
        
        try:
            for tipo in tipos_data:
                cursor.execute(sql, tipo)
                print(f"Tipo de documento '{tipo[0]}' insertado correctamente.")
            
            conexion.commit()
            print("Todos los tipos de documento fueron guardados con éxito.")
            
        except Exception as e:
            print(f"Error al insertar tipos de documento: {e}")
        finally:
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    insertar_tipos_documento()
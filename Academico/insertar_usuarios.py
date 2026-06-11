# insertar_datos_individual.py
from conexion import conectar

def insertar_usuarios_individual():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        
        # Lista de usuarios a insertar
        usuarios_data = [
            ("Juan", "Perez", "12345678", "juan@ejemplo.com", "pass123", "3001234567", "Calle 1", 1, 1),
            ("Maria", "Gomez", "87654321", "maria@ejemplo.com", "pass456", "3007654321", "Calle 2", 2, 1),
            ("Carlos", "Lopez", "11223344", "carlos@ejemplo.com", "pass789", "3001122334", "Calle 3", 2, 2)
        ]
        
        sql = """
        INSERT INTO Usuarios 
        (nombresUsuario, apellidosUsuarios, documentoUsuario, correoUsuario, passwordUsuario, telefonoUsuario, direccionUsuario, idRoles, idTipoDocumento) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        try:
            for fila in usuarios_data:
                cursor.execute(sql, fila)
                print(f"Insertado: {fila[0]} {fila[1]}")
            
            conexion.commit()
            print("Todas las filas fueron insertadas exitosamente.")
            
        except Exception as e:
            conexion.rollback()
            print(f"Error al insertar datos: {e}")
            
        finally:
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    insertar_usuarios_individual()
from conexion import conectar

def insertar_roles():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        
        roles_data = [
            ("Administrador",),
            ("Estudiante",),
            ("Docente",)
        ]
        
        sql = "INSERT INTO Roles (nombre_rol) VALUES (%s)"
        
        try:
            for rol in roles_data:
                cursor.execute(sql, rol)
                print(f"Rol '{rol[0]}' preparado para insertar.")
            
            # Confirmamos los cambios en la base de datos
            conexion.commit()
            print("¡Éxito! Todos los roles fueron guardados en la base de datos.")
            
        except Exception as e:
            print(f"Error al insertar los datos: {e}")
        finally:
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    insertar_roles()
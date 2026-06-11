# insertar_roles.py
from conexion import conectar

def insertar_roles():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        
        roles_data = [
            ("Administrador", "Usuario con acceso total al sistema"),
            ("Estudiante", "Usuario con acceso a materias y calificaciones"),
            ("Docente", "Usuario encargado de gestionar notas y cursos")
        ]
        
        sql = "INSERT INTO Roles (nombreRol, descripcionRol) VALUES (%s, %s)"
        
        try:
            for rol in roles_data:
                cursor.execute(sql, rol)
                print(f"Rol '{rol[0]}' insertado correctamente.")
            
            conexion.commit()
            print("Todos los roles fueron guardados con éxito.")
            
        except Exception as e:
            print(f"Error al insertar roles: {e}")
        finally:
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    insertar_roles()
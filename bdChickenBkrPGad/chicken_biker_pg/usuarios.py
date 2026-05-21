import sys
sys.path.append('..')
from conexion import conectar

def registrar_usuario(nombres, apellidos, documento, correo, password, telefono, direccion, id_tipo_doc, id_rol):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            sql = """INSERT INTO Usuario (nombresUsuario, apellidosUsuario, documentoUsuario, correoUsuario, 
                                          passwordUsuario, telefonoUsuario, direccionUsuario, TipoDocumento_idTipoDocumento, Roles_idRoles) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            cursor.execute(sql, (nombres, apellidos, documento, correo, password, telefono, direccion, id_tipo_doc, id_rol))
            conn.commit()
            print(f"Usuario '{nombres} {apellidos}' guardado exitosamente.")
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error al registrar usuario: {e}")

def buscar_usuario_por_documento(documento):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            sql = """SELECT u.idUsuario, u.nombresUsuario, u.apellidosUsuario, r.nombreRol 
                     FROM Usuario u 
                     JOIN Roles r ON u.Roles_idRoles = r.idRoles 
                     WHERE u.documentoUsuario = %s;"""
            cursor.execute(sql, (documento,))
            usuario = cursor.fetchone()
            cursor.close()
            conn.close()
            return usuario
        except Exception as e:
            print(f"Error al buscar usuario: {e}")
            return None
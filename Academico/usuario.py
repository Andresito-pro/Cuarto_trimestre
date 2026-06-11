from conexion import conectar

def crear_tabla_usuarios():
    conexion = conectar()
    
    if conexion:
        cursor = conexion.cursor()
        

        sql = """
        CREATE TABLE IF NOT EXISTS Usuarios (
            idUsuarios INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            nombresUsuario VARCHAR(100) NOT NULL,
            apellidosUsuarios VARCHAR(255) NOT NULL,
            documentoUsuario VARCHAR(50) NOT NULL,
            correoUsuario VARCHAR(150) NOT NULL,
            passwordUsuario VARCHAR(255) NOT NULL,
            telefonoUsuario VARCHAR(50),
            direccionUsuario VARCHAR(150),
            idRoles INT NOT NULL,
            idTipoDocumento INT NOT NULL,
    
            CONSTRAINT FK_Usuarios_Roles 
                FOREIGN KEY (idRoles) 
                REFERENCES Roles(idRoles),
            CONSTRAINT FK_Usuarios_TipoDocumento 
                FOREIGN KEY (idTipoDocumento) 
                REFERENCES TipoDocumento(idTipoDocumento)

        )
        """
        
        try:
            cursor.execute(sql)
            print("Tabla 'usuarios' creada correctamente (o ya existía).")
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    crear_tabla_usuarios()
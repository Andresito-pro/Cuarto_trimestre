import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER")
        )

        print("conexion a la base de datos exitosa")
        return conexion
    
    except Exception as e:
        print("Error al conectar a la base de datos")
        print(e)
        return None

if __name__ == "__main__":
    conexion = conectar()
    
    if conexion:
        print("conectado correctamente")
        conexion.close()
        print("conexion cerrada")
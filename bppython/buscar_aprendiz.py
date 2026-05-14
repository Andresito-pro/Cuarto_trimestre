from conexion import conectar
conexion = conectar()
cursor = conexion.cursor()
nombre = input("Ingrese el nombre del aprendiz a buscar: ")
cursor.execute(
    "SELECT * FROM aprendices WHERE nombre=%s",
    (nombre,)

)
resultado = cursor.fetchall()
print("\nRESULTADOS")
for dato in resultado:
    print(dato)
cursor.close()
conexion.close()

from conexion import conectar
conexion = conectar()
cursor = conexion.cursor()
cursor.execute("SELECT * FROM aprendices")
datos = cursor.fetchall()
print("\nLISTA DE APRENDICES")
for aprendiz in datos:
    print(aprendiz)
cursor.close()
conexion.close()

from conexion import conectar

conexion = conectar()

cursor = conexion.cursor()

  
sql = '''
INSERT INTO instructor(nombreInstructor,apellidoInstructor,tipoDocumento,documento,ocupacion) 
VALUES(%s, %s, %s,%s,%s)
'''

nombreInstructor = input("Ingrese el nombre del instructor: ")
apellidoInstructor = input("Ingrese el apellido del instructor: ")
tipoDocumento = input("Ingrese el tipo de documento: ")
documento = input("Ingrese el número de documento: ")
ocupacion = input("Ingrese la ocupación: ")
datos = (nombreInstructor, apellidoInstructor, tipoDocumento, documento, ocupacion)

cursor.execute(sql, datos)
conexion.commit()
print("¡El registro fue insertado correctamente!")
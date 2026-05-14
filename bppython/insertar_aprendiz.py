from conexion import conectar

conexion = conectar()

cursor = conexion.cursor()

  
sql = '''
INSERT INTO aprendices(nombre, ficha, programme) 
VALUES(%s, %s, %s)
'''

nombre = input("Ingrese el nombre del aprendiz: ")
ficha = input("Ingrese el número de ficha: ")
programa = input("Ingrese el programa de formación: ")
datos = (nombre, ficha, programa)

cursor.execute(sql, datos)
conexion.commit()
print("¡El registro fue insertado correctamente!")
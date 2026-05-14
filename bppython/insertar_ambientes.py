from conexion import conectar

conexion = conectar()

cursor = conexion.cursor()

  
sql = '''
INSERT INTO ambiente(nombreAmbiente, ubicacionAmbiente) 
VALUES(%s, %s)
'''

nombreAmbiente = input("Ingrese el nombre del ambiente: ")
ubicacionAmbiente = input("Ingrese la ubicación del ambiente: ")

datos = (nombreAmbiente, ubicacionAmbiente)

cursor.execute(sql, datos)
conexion.commit()
print("¡El registro fue insertado correctamente!")
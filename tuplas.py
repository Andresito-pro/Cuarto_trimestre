#ES UNA ESTRUCTURA DE DATOS
empleado = ("Luis", "Ventas", 300000)

#inmutable no se puede modificar
#permite duplicados
'''
1. Cuando los datos no van a cambiar de forma accidental
2. Retorno de multiples valores de funciones y que no se combinen
3. Mayor seguridad 
4. Mayor rendimiento en consumo de recursos. RAM
5. Uso de estructuras protegidas
'''
colores = ("rojo", "verde", "azul")
print(colores[0])
print(colores[2])
print(f"{colores[2]} {colores[0]}")
for i in colores: 
    print(i)

#persona = ("edad", "ciudad", "apellido", "estatura", "nombre")
#print(f"{persona[4]}: Carlos, {persona[2]}: Cordoba, {persona[1]}: Bogotá, {persona[0]}: 30, {persona[3]}: 180cm")
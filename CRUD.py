#Crearemos un CRUD dentro de un diccionario
#Problema
#Una tienda necesita administrar sus prductos
#El sistema debe permitir
#1.Crear productos
#2.Mostrar productos registrados
#3.Actualizar información de productos
#4.Eliminar productos

#============================================
#DICCIONARIO PRINCIPAL
productos = {}

#Variable para generar los códigos de identificación
id_producto = 1

#Crear

def crear_producto(nombre,precio):
    global id_producto

    productos[id_producto] = {"nombre": nombre, "precio":precio}
    id_producto += 1

#Leer los prooductos utilizando ID producto

def mostrar_productos():
    if not productos:
        print("No hay productos registrados")
        return
    for id, datos in productos.items():
        print(f"ID: {id}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Precio: {datos['precio']}")
        print("*" *20)

#ACTUALIZAR
def actualizar_producto(id, nombre = None, precio = None):
    if id in productos:
        if nombre:
            productos[id]['nombre'] = nombre
        if precio:
            productos[id]['precio'] = precio
        print("Producto Actualizado")
    else:
        print("Producto no encontrado")


crear_producto("laptop", 250000)
crear_producto("Tablet", 320000)
crear_producto("Celular", 400000)
crear_producto("Mouse", 32000)
crear_producto("Cámara", 340000)
crear_producto("auriculares", 20000)
crear_producto("teclado", 150000)
crear_producto("PC", 1000000)
crear_producto("microfono", 240000)
crear_producto("USB", 30000)
mostrar_productos()

actualizar_producto(1, nombre = "Laptop lenovo")(3, nombre = "Celular samsung")


actualizar_producto(2, precio = 299999)
actualizar_producto(5, precio = 35000)

actualizar_producto(6, nombre = "Auricular", precio = 23000)
actualizar_producto(8, nombre = "Microfonos", precio = 500000)

mostrar_productos()


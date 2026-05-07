#Se crea la lista
productos = []

#Se crea el producto

def crear_producto():
    id_producto = int(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    producto = {
        "id": id_producto,
        "nombre" : nombre,
        "precio": precio
    }
    productos.append(producto)
    print("Producto agregado correctamente")
    #_______________________________________________________________________
    #Mostrar producto
def mostrar_producto():
    if len(productos) == 0:
        print("No hay productos registrados")
    else: 
        print("\n=========LISTA DE PRODUCTOS=============")
        for producto in productos:
            print("--------------------------------------")
            print("ID: ", producto["id"])
            print("Nombre: ", producto["nombre"])
            print("Precio", producto["precio"])

#____________________________________________________________________________
#Actualizar producto
def actualizar_producto():
    id_buscar = int(input("Ingrese el ID del producto a actualizar: "))
    encontrado = False
    for producto in productos:
        if producto["id"] == id_buscar:
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            nuevo_precio = float(input("Ingrese le nuevo precio: "))
            producto["nombre"] = nuevo_nombre
            producto["precio"] = nuevo_precio
            print("producto actualizados")
    if not encontrado:
        print("producto no encontrado")

def eliminar_producto():
    id_buscar = int(input("ingrese el id del producto a eliminar: "))
    encontrado = False
    for producto in productos:
        if producto ["id"] == id_buscar:
            productos.remove(producto)
            print("producto eliminado")
            encontrado = True
            break
        if not encontrado == False:
            print("producto no encontrado")



while True:
    print("\n==================MENÚ PRINCIPAL==========================")
    print("1.Crear producto")
    print("2.Mostrar producto")
    print("3.Actualizar producto")
    print("4.Eliminar producto")
    print("5.Finalizar/Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        crear_producto()
    #Crear producto
    if opcion == "2":
        mostrar_producto()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Programa finaliza")
        break
    else:
        print("Opción no válida")
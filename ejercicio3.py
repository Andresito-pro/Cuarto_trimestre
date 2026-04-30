def mostrar_inventario(productos):
    print("\nINVENTARIO ACTUAL")
    if not productos:
        print("No hay productos para mostrar")
        return
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")

def agregar_producto(productos, nombre, precio):
    if isinstance(nombre, str) and nombre.strip() and isinstance(precio, (int, float)) and precio > 0:
        productos.append({"nombre": nombre.title(), "precio": precio})
        print(f"Producto '{nombre.title()}' agregado con éxito.")
    else:
        print("Error: Datos del producto no válidos.")

def insertar_productos(productos, indice, nombre, precio):
    if 0 <= indice <= len(productos) and isinstance(precio, (int, float)) and precio > 0:
        productos.insert(indice, {"nombre": nombre.title(), "precio": precio})
        print(f"El producto: -- '{nombre.title()}' insertado en la posición {indice + 1}")
    else:
        print("El índice es incorrecto, o el valor es incorrecto")

def eliminar_productos(productos, nombre):
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print(f"El producto '{nombre.title()}' ha sido eliminado del inventario")
            return
    print("El producto no existe")

def main():
    inventario = [
        {'nombre': 'Taladro', 'precio': 150000},
        {'nombre': 'Martillo', 'precio': 250000},
        {'nombre': 'Destornillador', 'precio': 18000}
    ]
    
    mostrar_inventario(inventario)
    agregar_producto(inventario, "Sierra", 45000)
    insertar_productos(inventario, 1, "broca", 25)
    eliminar_productos(inventario, "martillo")
    mostrar_inventario(inventario)

if __name__ == "__main__":
    main()
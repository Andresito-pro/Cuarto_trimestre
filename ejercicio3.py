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
    print(f"Error: El producto '{nombre}' no existe")

def ordenar_por_nombre(productos):
    productos.sort(key=lambda x: x['nombre'].lower())
    print("\nInventario ordenado por nombre.")

def ordenar_por_precio(productos):
    productos.sort(key=lambda x: x['precio'])
    print(f"\nInventario ordenado por precio.")

def invertir_inventario(productos):
    productos.reverse()
    print("\nOrden del inventario invertido manualmente.")

def main():
    inventario = [
        {'nombre': 'Taladro', 'precio': 150000},
        {'nombre': 'Martillo', 'precio': 250000},
        {'nombre': 'Destornillador', 'precio': 18000}
    ]
    
    agregar_producto(inventario, "Sierra", 45000)
    insertar_productos(inventario, 1, "broca", 2500)
    eliminar_productos(inventario, "martillo")
    
    print("-" * 30)
    ordenar_por_precio(inventario)
    mostrar_inventario(inventario)
    
    invertir_inventario(inventario)
    mostrar_inventario(inventario)

if __name__ == "__main__":
    main()

import sys
sys.path.append('..') # Permite buscar conexion.py en el directorio padre
from conexion import conectar

def agregar_categoria(nombre, descripcion):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO CategoriaProducto (nombreCategoria, descripcionCategoria) VALUES (%s, %s);"
            cursor.execute(sql, (nombre, descripcion))
            conn.commit()
            print("Categoría agregada con éxito.")
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error: {e}")

def agregar_producto(nombre, descripcion, precio, id_categoria):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            sql = """INSERT INTO Productos (nombrePlato, descripcion, precioVenta, CategoriaProducto_idcategoria) 
                     VALUES (%s, %s, %s, %s);"""
            cursor.execute(sql, (nombre, descripcion, precio, id_categoria))
            conn.commit()
            print(f"Plato '{nombre}' registrado en el menú.")
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error al registrar producto: {e}")

def listar_menu():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            sql = """SELECT p.idProductos, p.nombrePlato, p.precioVenta, c.nombreCategoria 
                     FROM Productos p 
                     JOIN CategoriaProducto c ON p.CategoriaProducto_idcategoria = c.idcategoria
                     WHERE p.activoProd = TRUE;"""
            cursor.execute(sql)
            productos = cursor.fetchall()
            print("\n---MENÚ CHICKEN BIKER ---")
            for prod in productos:
                print(f"ID: {prod[0]} | Plato: {prod[1]} | Precio: ${prod[2]:,.0f} | Cat: {prod[3]}")
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error al listar el menú: {e}")
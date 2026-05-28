from validaciones import validarTexto
def agregar_libro(conexion):
    titulo = input("Titulo del libro: ")
    autor = input("Autor: ")
    if not validarTexto(titulo) or not validarTexto(autor):
        print("Datos inválidos")
        return

    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO libro (titulo, autor) VALUES (%s,%s)",
        (titulo, autor)
    )
    conexion.commit()
    print("Libro agregado correctamente")

def ver_libros(conexion):
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM libro")
    libros = cursor.fetchall()
    print("=======LISTADO DE LIBROS============")
    for libro in libros:
        print(f"ID: {libro[0]} | Titulo: {libro[1]} | Autor: {libro[2]}")

def eliminar_libro(conexion):
    id_libro = input("ID del libro a eliminar: ")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libro WHERE id = %s", (id_libro,))
    conexion.commit()
    print("Libro eliminado")

    
#Se crea el diccionario 
aprendices = {}

id_aprendices = 1

def crear_estudiante(documento, nombre, programa, ficha):
    global id_aprendices

    aprendices[id_aprendices] = {
        "documento": documento,
        "nombre": nombre,
        "programa": programa,
        "ficha": ficha
    }

    id_aprendices += 1


#Leer los aprendices utilizando el ID
def mostrar_aprendiz():

    if not aprendices:
        print("No hay aprendices registrados")
        return

    for id, datos in aprendices.items():

        print(f"id {id}")
        print(f"documento {datos['documento']}")
        print(f"nombre {datos['nombre'].title()}")
        print(f"programa {datos['programa'].title()}")
        print(f"ficha {datos['ficha']}")
        print("*" * 30)


#Actualizar
def actualizar_estudiante(id, documento, nombre, programa, ficha):

    if id in aprendices:

        if documento:
            aprendices[id]['documento'] = documento

        if nombre:
            aprendices[id]['nombre'] = nombre

        if programa:
            aprendices[id]['programa'] = programa

        if ficha:
            aprendices[id]['ficha'] = ficha

    else:
        print("Producto no encontrado")


def eliminar_producto(id):

    if id in aprendices:
        del aprendices[id]


#********************************************************************
#PRUEBAS
#********************************************************************

crear_estudiante(1025067, "Andrés", "ADSO", 3227025)

mostrar_aprendiz()
#Se crea la lista para almacenar los estudiantes
estudiantes = []

#Se crea la función para realizar la creación del estudiante

def crear_estudiante():
    documento = int(input("Ingrese su número de documento: "))
    nombre = input("Ingrese el nombre: ")
    programa = input("Ingrese el programa al cual pertenece: ")
    ficha = int(input("Ingrese su número de ficha"))
    estudiante = {
        "documento": documento,
        "nombre": nombre,
        "programa": programa,
        "ficha": ficha
    }
    estudiantes.append(estudiante)
    print("Estudiante agregado correctamente.")

def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in estudiantes:
            print(estudiante["documento"])
            print(estudiante["nombre"])
            print(estudiante["programa"])
            print(estudiante["ficha"])

def actualizar_estudiante():
    documento_buscar = int(input("Ingrese el documento: "))
    encontrado = False
    for estudiante in estudiantes:
        if estudiante["documento"] == documento_buscar:
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_programa = input("Ingrese el nuevo programa: ")
            nueva_ficha = int(input("Ingrese el nuevo número de ficha: "))
            estudiante["nombre"] = nuevo_nombre
            estudiante["programa"] = nuevo_programa
            estudiante["ficha"] = nueva_ficha

def eliminar_estudiante():
    for estudiante in estudiantes:
        if estudiante["documento"] == documento_buscar:
            estudiantes.remove(estudiante)
            print("Producto eliminado")
            encontrado = True
            break
        if not encontrado == False:
            print("Producto no encontrado")

while True:

    print("=================================================================")
    print("1 = Crear estudiante: \n2 = Mostrar estudiante: \n3 = Actualizar Estudiante: \n4 = Eliminar estudiante:  ")
    opcion = input("Seleccione una opcción: ")
    if opcion == "1":
        crear_estudiante()
    elif opcion =="2":
        mostrar_estudiantes()
    elif opcion == "3":
        actualizar_estudiante()
    elif opcion == "4":
        eliminar_estudiante()
    else:
        print("Opcion no válida")


#Una tienda necesitamos utilizar los nombres de sus clientes realizados
#para promociones
#1.Agregar nuevos clientes
#2.Mostrar todos los clientes 
#3.Modificar los nombres
#4.Eliminar clientes

print("Agregar nuevos clientes")

def agregar_cliente(lista_clientes, nombre):
    if isinstance(nombre,str) and 2 <= len(nombre) <= 50:
        lista_clientes.append(nombre.title())
        print(f"Cliente agregado -> {nombre}")
    else:
        print("Nombre de lciente inválido")

def mostrar_cliente(lista_clientes):
    for cliente in lista_clientes:
        print(cliente)

def modificar_cliente(lista_clientes, indice, nuevo_nombre):
    if not isinstance (nuevo_nombre,str) and 2 <= len(nuevo_nombre) <= 50:
        print("Nombre de cliente inválido")

        return
    if 0 >= indice > len(lista_clientes):
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"cliente modificado -> {nuevo_nombre}")

    else: 
        print("")

def eliminar_cliente (lista_clientes, indice):
    if 0 <= indice < len(lista_clientes):
        eliminado = lista_clientes.pop(indice)
        print(f"Se borró el cliente: {eliminado}")

    else:
        print("Indice ")

def main():
    clientes = ['Andres','Cesar','Melany']
    print("***CLIENTES ACTUALES***")
    mostrar_cliente(clientes)
    agregar_cliente(clientes,'Mary')
    print("**CLIENTES ACTUALIZADOS**")
    mostrar_cliente(clientes)
    eliminar_cliente(clientes, 2)
    mostrar_cliente(clientes)
if __name__=="__main__":
    main()
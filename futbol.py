# Sistema de equipos de fútbol

# 1. Crear jugadores
def agregar_jugador(plantilla, nombre):
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        plantilla.append(nombre.title())
        print(f"Jugador inscrito: {nombre.title()}")
    else:
        print("Nombre de jugador no válido")

# 2. Mostrar equipo
def mostrar_equipo(plantilla):
    if not plantilla:
        print("No hay jugadores en la plantilla")
    else:
        for i, jugador in enumerate(plantilla):
            print(f"{i}. {jugador}")

# 3. Realizar cambios (sale uno, entra otro)
def realizar_cambio(plantilla, indice_sale, nombre_entra):
    if 0 <= indice_sale < len(plantilla):
        if isinstance(nombre_entra, str) and 2 <= len(nombre_entra) <= 50:
            sale = plantilla[indice_sale]
            plantilla[indice_sale] = nombre_entra.title()
            print(f"Cambio realizado: Sale {sale}, entra {nombre_entra.title()}")
        else:
            print("Nombre del nuevo jugador no válido")
    else:
        print("Indice de jugador a salir no encontrado")

# 4. Tarjetas rojas (expulsados)
def tarjeta_roja(plantilla, lista_expulsados, indice):
    if 0 <= indice < len(plantilla):
        expulsado = plantilla.pop(indice)
        lista_expulsados.append(expulsado)
        print(f"Tarjeta roja: {expulsado} ha sido expulsado del campo")
    else:
        print("Indice de expulsion invalido")

# 5. Mostrar expulsados
def mostrar_expulsados(lista_expulsados):
    if not lista_expulsados:
        print("No hay jugadores expulsados en este encuentro")
    else:
        print("REPORTE DE EXPULSADOS:")
        for jugador in lista_expulsados:
            print(f"- {jugador}")

# MAIN
def main():
    # Equipos e historial
    equipo = ['Luis Diaz', 'James Rodriguez', 'Richard Rios', 'Daniel Muñoz']
    expulsados = []

    # Mostrar equipos iniciales
    print("--- CONVOCATORIA INICIAL ---")
    mostrar_equipo(equipo)
    print("---------------------------")

    # Agregar jugadores
    print("Inscribiendo nuevo refuerzo...")
    agregar_jugador(equipo, 'Jhon Duran')

    # Segundo tiempo - Cambios
    print("\n--- SEGUNDO TIEMPO ---")
    realizar_cambio(equipo, 1, 'Juan Quintero')

    # Tarjetas rojas
    print("\n--- INCIDENTE EN EL PARTIDO ---")
    tarjeta_roja(equipo, expulsados, 3)

    # Mostrar estado final
    print("\n--- ESTADO FINAL DE LA PLANTILLA ---")
    mostrar_equipo(equipo)

    # Mostrar expulsados
    print("\n--- INFORME DISCIPLINARIO ---")
    mostrar_expulsados(expulsados)

if __name__ == "__main__":
    main()
    
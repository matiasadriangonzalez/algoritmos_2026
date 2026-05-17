from stack import Stack

#20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.

DIRECTIONS = [
    "norte", "sur", "este", "oeste",
    "noreste", "noroeste", "sureste", "suroeste"
]

OPPOSITE = {
    "norte":    "sur",
    "sur":      "norte",
    "este":     "oeste",
    "oeste":    "este",
    "noreste":  "suroeste",
    "suroeste": "noreste",
    "noroeste": "sureste",
    "sureste":  "noroeste",
}


def registrar_movimientos() -> Stack:
    """
    Registra los movimientos del robot en una pila.
    Cada movimiento almacena (cantidad_de_pasos, dirección).
    """
    movimientos = Stack()

    print("Registro de movimientos del robot:")
    print(f"Direcciones válidas: {', '.join(DIRECTIONS)}")
    print("Escriba 'fin' como dirección para terminar.\n")

    while True:
        direccion = input("Dirección: ").strip().lower()

        if direccion == "fin":
            break

        if direccion not in DIRECTIONS:
            print(f"  Dirección inválida. Opciones: {', '.join(DIRECTIONS)}\n")
            continue

        pasos_str = input("Cantidad de pasos: ").strip()
        if not pasos_str.isdigit() or int(pasos_str) <= 0:
            print("  Ingrese un número entero positivo.\n")
            continue

        movimientos.push((int(pasos_str), direccion))
        print(f"  Registrado: {pasos_str} pasos hacia el {direccion}\n")

    return movimientos


def regresar_al_origen(movimientos: Stack) -> None:
    """
    Genera la secuencia de movimientos para que el robot
    regrese al punto de partida recorriendo el mismo camino en sentido inverso.

    Lógica:
      - Al desapilar obtenemos los movimientos en orden inverso (LIFO),
        lo que reproduce el camino de regreso automáticamente.
      - Cada dirección se reemplaza por su opuesta para que el robot
        retroceda por el mismo trayecto.
    """
    print("\nRegresar el robot al origen: ")

    if movimientos.size() == 0:
        print("No hay movimientos registrados.")
        return

    stack_aux = Stack()
    nro_paso = 1

    while movimientos.size() > 0:
        value = movimientos.pop()
        opuesta = OPPOSITE[value[1]]
        print(f"Paso {nro_paso}: {value[0]} pasos hacia el {opuesta}")
        nro_paso += 1
        stack_aux.push(value)

    while stack_aux.size() > 0:
        movimientos.push(stack_aux.pop())

    print("El robot volvio al origen.")


if __name__ == "__main__":
    movimientos = registrar_movimientos()

    print(f"\nMovimientos registrados ({movimientos.size()} en total):")
    movimientos.show()

    regresar_al_origen(movimientos)


#24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.


def cargar_personajes() -> Stack:
    """
    Carga la pila con personajes del MCU (nombre, cantidad de películas).
    """
    personajes = Stack()

    datos = [
        ("Iron Man",        10),
        ("Thor",             8),
        ("Hulk",             7),
        ("Nick Fury",        7),
        ("Capitan America",  7),
        ("Viuda Negra",      7),
        ("Loki",             6),
        ("Nebula",           6),
        ("War Machine",      6),
        ("Scarlet Witch",    6),
        ("Spider-Man",       6),
        ("Hawkeye",          5),
        ("Groot",            5),
        ("Gamora",           5),
        ("Drax",             5),
        ("Star-Lord",        5),
        ("Doctor Strange",   4),
        ("Capitana Marvel",   3),
        ("Rocket Raccoon",   6),
    ]

    for nombre, peliculas in datos:
        personajes.push((nombre, peliculas))

    return personajes


def posicion_personajes(personajes: Stack) -> None:
    """
    a. Determina la posición de Rocket Raccoon y Groot en la pila
       (posición 1 = cima).
    """
    print("\na. Posición de Rocket Raccoon y Groot:")

    stack_aux = Stack()
    posicion   = 1
    pos_rocket = None
    pos_groot  = None

    while personajes.size() > 0:
        value = personajes.pop()
        if value[0] == "Rocket Raccoon":
            pos_rocket = posicion
        if value[0] == "Groot":
            pos_groot = posicion
        posicion += 1
        stack_aux.push(value)

    while stack_aux.size() > 0:
        personajes.push(stack_aux.pop())

    if pos_rocket is not None:
        print(f"  Rocket Raccoon: posición {pos_rocket}")
    else:
        print("  Rocket Raccoon: no encontrado")

    if pos_groot is not None:
        print(f"  Groot: posición {pos_groot}")
    else:
        print("  Groot: no encontrado")


def personajes_mas_de_5(personajes: Stack) -> None:
    """
    b. Muestra los personajes que participaron en más de 5 películas.
    """
    print("\nb. Personajes con más de 5 películas:")

    stack_aux = Stack()

    while personajes.size() > 0:
        value = personajes.pop()
        if value[1] > 5:
            print(f"  {value[0]}: {value[1]} películas")
        stack_aux.push(value)

    while stack_aux.size() > 0:
        personajes.push(stack_aux.pop())


def peliculas_black_widow(personajes: Stack) -> None:
    """
    c. Indica en cuántas películas participó Black Widow.
    """
    print("\nc. Películas de Black Widow:")

    stack_aux = Stack()
    peliculas = None

    while personajes.size() > 0:
        value = personajes.pop()
        if value[0] == "Viuda Negra":
            peliculas = value[1]
        stack_aux.push(value)

    while stack_aux.size() > 0:
        personajes.push(stack_aux.pop())

    if peliculas is not None:
        print(f"  La Viuda Negra participó en {peliculas} películas")
    else:
        print("  La Viuda Negra no fue encontrada en la pila")


def personajes_CDG(personajes: Stack) -> None:
    """
    d. Muestra los personajes cuyos nombres empiezan con C, D o G.
    """
    print("\nd. Personajes cuyo nombre empieza con C, D o G:")

    stack_aux = Stack()

    while personajes.size() > 0:
        value = personajes.pop()
        if value[0][0].upper() in ["C", "D", "G"]:
            print(f"  {value[0]}")
        stack_aux.push(value)

    while stack_aux.size() > 0:
        personajes.push(stack_aux.pop())


if __name__ == "__main__":
    personajes = cargar_personajes()

    posicion_personajes(personajes)
    personajes_mas_de_5(personajes)
    peliculas_black_widow(personajes)
    personajes_CDG(personajes)
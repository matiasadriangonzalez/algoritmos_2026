#5. Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not romano:
        return 0
    
    if len(romano) == 1:
        return valores[romano[0]]
    
    valor_actual = valores[romano[0]]
    valor_siguiente = valores[romano[1]]
    
    if valor_actual >= valor_siguiente:
        return valor_actual + romano_a_decimal(romano[1:])
    else:
        return -valor_actual + romano_a_decimal(romano[1:])


print(f"El numero romano I es: {romano_a_decimal('I')}")
print(f"El numero romano IV es: {romano_a_decimal('IV')}")
print(f"El numero romano XIV es: {romano_a_decimal('XIV')}")
print(f"El numero romano MCMXCIV es: {romano_a_decimal('MCMXCIV')}")



# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.

def usar_la_fuerza(mochila, objetos_sacados=0):
    if len(mochila) == 0:
        return False, objetos_sacados
    
    objeto_actual = mochila[0]
    print(f"  Sacando objeto #{objetos_sacados + 1}: '{objeto_actual}'")

    if objeto_actual == "sable de luz":
        return True, objetos_sacados + 1
    
    return usar_la_fuerza(mochila[1:], objetos_sacados + 1)


mochila_luke = ["comida", "cantimplora", "capa", "mate","sable de luz", "holocrón"]
encontrado, cantidad = usar_la_fuerza(mochila_luke)

if encontrado:
    print(f"¡Sable encontrado! Se tuvieron que sacar {cantidad} objetos.")
else:
    print(f"No se encontró el sable. Se vació la mochila sacando {cantidad} objetos.")
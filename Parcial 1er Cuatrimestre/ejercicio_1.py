# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.
from super_heroes_data import superheroes
from list_ import List

heros = List()
for hero in superheroes[:15]:
    heros.append(hero)

heros.show()
print()


def buscar(heros: List, buscado: str, i = 0) -> bool:
    if i == heros.size():
        return False
    if heros[i]['name'] == buscado:
        return True
    return buscar(heros, buscado, i+1)

def listar_superheroes(heros: List, i = 0) -> None:
    if i == heros.size():
        return
    print(heros[i]['name'])
    listar_superheroes(heros, i+1)

value = buscar(heros, 'Captain America')
if value:
    print('Capitan America se encuentra en la lista')
else:
    print('Capitan America no se encuentra en la lista')
print()

listar_superheroes(heros)
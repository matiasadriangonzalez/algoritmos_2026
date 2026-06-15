
# Importamos tu clase List desde el archivo list_.py
import dataclasses
from list_ import List
from typing import Any

# ============================================================
# 4. LISTA (List)
# ============================================================
# Python ya tiene listas nativas, pero el profe crea una clase
# List que hereda de list y agrega metodos utiles.
#
# Operaciones nativas importantes:
#   append(x)          -> agrega al final
#   insert(i, x)       -> inserta en posicion i
#   pop(i)             -> elimina y retorna el elemento en i
#   remove(x)          -> elimina la primera ocurrencia de x
#   sort(key=func)     -> ordena in-place con una funcion clave
#   reverse()          -> invierte in-place
#   index(x)           -> retorna el indice de x
#   count(x)           -> cuenta ocurrencias de x
#
# La clase List agrega:
#   add_criterion(key, func)      -> registra una funcion de criterio
#   sort_by_criterion(key)        -> ordena usando el criterio registrado
#   search(value, criterion=None) -> busqueda binaria por criterio
#   delete_value(value, criterion)-> busca y elimina usando pop(index)
#   show()                        -> imprime todos los elementos
#   size()                        -> retorna len(self) o sea la cantidad de nodos

#1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
# def contar_nodos(lista: List) -> int:
#     return lista.size()

# l1=List([1,2,3,4,5,7,9,4,1,2])
# print(contar_nodos(l1))

#2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

# l = List()
# for c in "parcial mañana":
#     l.append(c)

# def eliminar_vocales(lista: list) -> list:
#     lista_sin_vocales = List()
#     vocales = ['a','e','i','o','u']

#     for caracter in lista:
#         if caracter not in vocales:
#             lista_sin_vocales.append(caracter)
#     return lista_sin_vocales

# resultado = eliminar_vocales(l)
# resultado.show()

#3. Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
# una que contenga los números pares y otra para los números impares.
# def pares_impares(lista_num: List) -> tuple:
#     pares = List()
#     impares = List()

#     for numero in lista_num:
#         if numero % 2 == 0:
#             pares.append(numero)
#         else:
#             impares.append(numero)

#     return pares, impares

# numeros = List([1,2,3,4,5,6,7,8,9,10])

# pares, impares = pares_impares(numeros)
# print('pares: ')
# pares.show()
# print('impares: ')
# impares.show()

#4. Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.
# def inserta_posicion_nodo(lista: List, posicion:int, elemento: Any) -> None:
#     lista.insert(posicion, elemento)

# lista = List([1,2,3,4,5,6,7,8,9,10])
# inserta_posicion_nodo(lista, 1, 23)
# lista.show()

#5. Dada una lista de números enteros eliminar de estas los números primos.
# def es_primo(n: int) -> bool:
#     if n < 2:
#         return False
#     for i in range(2, n//2 + 1):
#         if n % i == 0:
#             return False
#     return True

# def eliminar_primos(lista: List) -> List:
#     sin_primos = List()
#     for numero in lista:
#         if not es_primo(numero):
#             sin_primos.append(numero)
#     return sin_primos

# l5 = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
# resultado = eliminar_primos(l5)
# resultado.show()

#6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

# 1. Definimos la clase para estructurar los datos
class Superheroe:
    def __init__(self, nombre, anio_aparicion, casa_comic, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia

    def __str__(self):
        return f"{self.nombre} ({self.casa_comic} - {self.anio_aparicion} | Bio: {self.biografia})"

# 2. Creamos la función de criterio para que el profe sepa cómo buscar por nombre
def by_name(item: Superheroe) -> str:
    return item.nombre

# 3. Inicializamos la lista y le agregamos el criterio
lista_heroes = List()
lista_heroes.add_criterion('nombre', by_name)

lista_heroes.append(Superheroe('Linterna Verde', 1940, 'DC', 'Menciona su traje esmeralda'))
lista_heroes.append(Superheroe('Wolverine', 1974, 'Marvel', 'Conocido por sus garras de adamantium'))
lista_heroes.append(Superheroe('Dr. Strange', 1963, 'Marvel', 'Maestro de las artes místicas'))
lista_heroes.append(Superheroe('Capitana Marvel', 1968, 'Marvel', 'Su biografía menciona su traje'))
lista_heroes.append(Superheroe('Mujer Maravilla', 1941, 'DC', 'Princesa amazona con lazo de la verdad'))
lista_heroes.append(Superheroe('Flash', 1940, 'DC', 'El hombre más rápido del mundo'))
lista_heroes.append(Superheroe('Star-Lord', 1976, 'Marvel', 'Líder de los Guardianes de la Galaxia'))

#a. eliminar el nodo que contiene la información de Linterna Verde
eliminado = lista_heroes.delete_value("Linterna Verde", "nombre")
if eliminado:
    print(f'Superhéroe eliminado: {eliminado.nombre}')

#b. mostrar el año de aparición de Wolverine
index_wolverine = lista_heroes.search("Wolverine", "nombre")
if index_wolverine is not None:
    print(f'Año de aparición de Wolverine: {lista_heroes[index_wolverine].anio_aparicion}')

#c. cambiar la casa de Dr. Strange a Marvel
index_dr_strange = lista_heroes.search("Dr. Strange", "nombre")
if index_dr_strange is not None:
    lista_heroes[index_dr_strange].casa_comic = "Marvel"
    print(f'Casa de Dr. Strange cambiada a Marvel')

#d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”
for h in lista_heroes:
    bio = h.biografia.lower()
    if "traje" in bio or "armadura" in bio:
        print(f'{h.nombre} menciona traje o armadura en su biografia')

#e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
for heroe in lista_heroes:
    if heroe.anio_aparicion < 1963:
        print(f'{heroe.nombre} es de la casa {heroe.casa_comic}')

#f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
for nombre_buscado in ["capitana marvel", "Mujer Maravilla"]:
    i = lista_heroes.search(nombre_buscado, "nombre")
    if i is not None:
        print(f'{nombre_buscado} es de la casa {lista_heroes[i].casa_comic}')

#g. mostrar toda la información de Flash y Star-Lord;
for nombre_buscado in ["Flash", "Star-Lord"]:
    i = lista_heroes.search(nombre_buscado, "nombre")
    if i is not None:
        print(f'{lista_heroes[i]}')

#h. mostrar los superhéroes que comienzan con la letra B, M y S;
for heroe in lista_heroes:
    if heroe.nombre[0].upper() in {'B','M','S'}:
        print(f'{heroe.nombre} comienza con la letra {heroe.nombre[0]}')

#i. determinar cuántos superhéroes hay de cada casa de comic.
c_marvel = 0
c_dc = 0

for heroe in lista_heroes:
    if heroe.casa_comic == "Marvel":
        c_marvel +=1
    elif heroe.casa_comic == "DC":
        c_dc += 1

print(f'total marvel: {c_marvel} - total dc {c_dc}')

lista_heroes.show()



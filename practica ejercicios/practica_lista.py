
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

l = List()
for c in "parcial mañana":
    l.append(c)

def eliminar_vocales(lista: list) -> list:
    lista_sin_vocales = List()
    vocales = ['a','e','i','o','u']

    for caracter in lista:
        if caracter not in vocales:
            lista_sin_vocales.append(caracter)
    return lista_sin_vocales

resultado = eliminar_vocales(l)
resultado.show()

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
# class Superheroe:
#     def __init__(self, nombre, anio_aparicion, casa_comic, biografia):
#         self.nombre = nombre
#         self.anio_aparicion = anio_aparicion
#         self.casa_comic = casa_comic
#         self.biografia = biografia

#     def __str__(self):
#         return f"{self.nombre} ({self.casa_comic} - {self.anio_aparicion} | Bio: {self.biografia})"

# # 2. Creamos la función de criterio para que el profe sepa cómo buscar por nombre
# def by_name(item: Superheroe) -> str:
#     return item.nombre

# # 3. Inicializamos la lista y le agregamos el criterio
# lista_heroes = List()
# lista_heroes.add_criterion('nombre', by_name)

# lista_heroes.append(Superheroe('Linterna Verde', 1940, 'DC', 'Menciona su traje esmeralda'))
# lista_heroes.append(Superheroe('Wolverine', 1974, 'Marvel', 'Conocido por sus garras de adamantium'))
# lista_heroes.append(Superheroe('Dr. Strange', 1963, 'Marvel', 'Maestro de las artes místicas'))
# lista_heroes.append(Superheroe('Capitana Marvel', 1968, 'Marvel', 'Su biografía menciona su traje'))
# lista_heroes.append(Superheroe('Mujer Maravilla', 1941, 'DC', 'Princesa amazona con lazo de la verdad'))
# lista_heroes.append(Superheroe('Flash', 1940, 'DC', 'El hombre más rápido del mundo'))
# lista_heroes.append(Superheroe('Star-Lord', 1976, 'Marvel', 'Líder de los Guardianes de la Galaxia'))

# #a. eliminar el nodo que contiene la información de Linterna Verde
# eliminado = lista_heroes.delete_value("Linterna Verde", "nombre")
# if eliminado:
#     print(f'Superhéroe eliminado: {eliminado.nombre}')

# #b. mostrar el año de aparición de Wolverine
# index_wolverine = lista_heroes.search("Wolverine", "nombre")
# if index_wolverine is not None:
#     print(f'Año de aparición de Wolverine: {lista_heroes[index_wolverine].anio_aparicion}')

# #c. cambiar la casa de Dr. Strange a Marvel
# index_dr_strange = lista_heroes.search("Dr. Strange", "nombre")
# if index_dr_strange is not None:
#     lista_heroes[index_dr_strange].casa_comic = "Marvel"
#     print(f'Casa de Dr. Strange cambiada a Marvel')

# #d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# # “traje” o “armadura”
# for h in lista_heroes:
#     bio = h.biografia.lower()
#     if "traje" in bio or "armadura" in bio:
#         print(f'{h.nombre} menciona traje o armadura en su biografia')

# #e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# # sea anterior a 1963;
# for heroe in lista_heroes:
#     if heroe.anio_aparicion < 1963:
#         print(f'{heroe.nombre} es de la casa {heroe.casa_comic}')

# #f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# for nombre_buscado in ["capitana marvel", "Mujer Maravilla"]:
#     i = lista_heroes.search(nombre_buscado, "nombre")
#     if i is not None:
#         print(f'{nombre_buscado} es de la casa {lista_heroes[i].casa_comic}')

# #g. mostrar toda la información de Flash y Star-Lord;
# for nombre_buscado in ["Flash", "Star-Lord"]:
#     i = lista_heroes.search(nombre_buscado, "nombre")
#     if i is not None:
#         print(f'{lista_heroes[i]}')

# #h. mostrar los superhéroes que comienzan con la letra B, M y S;
# for heroe in lista_heroes:
#     if heroe.nombre[0].upper() in {'B','M','S'}:
#         print(f'{heroe.nombre} comienza con la letra {heroe.nombre[0]}')

# #i. determinar cuántos superhéroes hay de cada casa de comic.
# c_marvel = 0
# c_dc = 0

# for heroe in lista_heroes:
#     if heroe.casa_comic == "Marvel":
#         c_marvel +=1
#     elif heroe.casa_comic == "DC":
#         c_dc += 1

# print(f'total marvel: {c_marvel} - total dc {c_dc}')

# lista_heroes.show()


# --------------- VERSION PROFE ------------
#6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias 
# para poder realizar las siguientes actividades:

# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.
# from superheroes import superheroes 

# class Superheroes:
    
#     def __init__(self, nombre, anio_aparicion, casa_comic, biografia):
#         self.nombre = nombre
#         self.anio_aparicion = anio_aparicion
#         self.casa_comic = casa_comic
#         self.biografia = biografia

#     def __str__(self):
#         return (f'Nombre:    {self.nombre}\n'
#                 f'Aparicion: {self.anio_aparicion}\n'
#                 f'Casa:      {self.casa_comic}\n'
#                 f'Biografia: {self.biografia}\n')

# def by_nombre(item):
#     return item.nombre

# def by_anio_aparicion(item):
#     return item.anio_aparicion

# def by_casa(item):
#     return item.casa_comic



# l = List() 
# l.add_criterion('nombre', by_nombre)
# l.add_criterion('anio_aparicion', by_anio_aparicion)
# l.add_criterion('casa', by_casa)

# for s in superheroes:
#     l.append(Superheroes(s['nombre'], s['anio_aparicion'], s['casa'], s['biografia']))

# #a) eliminar el nodo que contiene la información de Linterna Verde;
# print('eliminando a Linterna Verde')
# deleted = l.delete_value("Linterna Verde", "nombre")
# print(f'dato eliminado: {deleted}')
# print()
# #b) mostrar el año de aparición de Wolverine;
# wolverine = l.search('Wolverine', 'nombre')
# print(f'año de aparicion de wolverine: {l[wolverine].anio_aparicion}')
# print()

# # c. cambiar la casa de Dr. Strange a Marvel;
# dr_strange = l.search('Dr. Strange', 'nombre')

# if dr_strange is not None:
#         l[dr_strange].casa_comic = 'Marvel'

# print(f'{l[dr_strange].nombre} es de la casa {l[dr_strange].casa_comic}')
# print()

# #d # d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# # “traje” o “armadura”;
# print('superheroes con traje o armadura')
# l.filter_contain_on_bio(["traje", "armadura"])
# print()

# #e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# # sea anterior a 1963;
# print('Superheroes anteriores a 1963:')
# for hero in l:
#     if hero.anio_aparicion < 1963:
#         print(f'SuperHeroe: {hero.nombre} - Casa: {hero.casa_comic} - Año: {hero.anio_aparicion}')
# print()

# # f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# CapiMarvel = l.search('Capitana Marvel', 'nombre')
# MujerMaravilla = l.search('Mujer Maravilla', 'nombre')

# if CapiMarvel is not None and MujerMaravilla is not None:
#     print(f'casa de capitana marvel: {l[CapiMarvel].casa_comic}')
#     print(f'casa de mujer maravilla: {l[MujerMaravilla].casa_comic}')
# else:
#     print('no se encontro a capitana marvel o mujer maravilla')
# print()

# # g. mostrar toda la información de Flash y Star-Lord;
# flash = l.search('Flash', 'nombre')
# starLoad = l.search('Star-Lord', 'nombre')
# print('informacion de flash y star-lord: ')
# print(f'{l[flash]}')
# print(f'{l[starLoad]}')

# # h. listar los superhéroes que comienzan con la letra B, M y S;
# print('superheroes que comienzan con B, M y S:')
# l.filter_start_with(('B', 'M', 'S'))
# print()

# # i. determinar cuántos superhéroes hay de cada casa de comic.
# print(f'Marvel: {l.count_by("casa", "Marvel")}')
# print(f'DC: {l.count_by("casa", "DC")}')



# 7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.
# l1 = List()
# l2 = List()

# l1.append(1)
# l1.append(2)
# l1.append(3)
# l1.append(4)
# l1.append(5)

# l2.append(4)
# l2.append(5)
# l2.append(6)
# l2.append(7)
# l2.append(8)

# # a. concatenar dos listas, una atrás de la otra;

# for elem in l2:
#     l1.append(elem)

# l1.show()

# #b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# print(f'- Concatenar dos listas sin repetir: ')
# resultado = List()

# for elem in l1:
#     if elem not in resultado:
#         resultado.append(elem)

# for elem in l2:
#     if elem not in resultado:
#         resultado.append(elem)

# resultado.show()

# # c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
# count = 0
# for elem in l1:
#     if l2.search(elem) is not None:
#         count +=1

# print(f'- elementos que tienen en comun: {count}')

# # d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.
# print('-eliminando nodos de una lista de a uno a la vez')

# while l1.size() > 0:
#     print(f'eliminando: {l1[0]}')
#     l1.delete_value(l1[0])

# l1.show()



#8. Utilizando una lista doblemente enlazada, cargar una palabra carácter a carácter, y determinar
#si la misma es un palíndromo, sin utilizar ninguna estructura auxiliar.
# l = List()

# palabra = str(input('ingrese una palabra: '))

# for i in palabra:
#     l.append(i)

# izq = 0
# der = l.size() -1
# es_palindromo = True

# while izq < der:
#     if l[izq] != l[der]:
#         es_palindromo = False
#         break
#     izq += 1
#     der -= 1

# if es_palindromo:
#     print(f'{palabra} es palindromo')
# else: 
#     print(f'{palabra} no es palindromo')


#9. Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
# Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con
# la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un
# algoritmo que permita realizar la siguientes actividades:
# a. mostrar los alumnos ordenados alfabéticamente por apellido;
# b. indicar los alumnos que no desaprobaron ningún parcial;
# c. determinar los alumnos que tienen promedio mayor a 8,89;
# d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
# e. mostrar el promedio de cada uno de los alumnos;
# f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
# g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
# h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
# i. mostrar todos los alumnos que rindieron en el año 2020;
# j. debe modificar el TDA para implementar lista de lista.
# alumnos = [
#     {'nombre': 'Ana', 'apellido': 'Perez', 'legajo': 1001, 'parciales': [{'materia': 'Algoritmos y Estructuras de Datos', 'nota': 9, 'fecha': '2020-05-10'}, {'materia': 'Base de Datos', 'nota': 9.50, 'fecha': '2023-05-15'}]},
#     {'nombre': 'Juan', 'apellido': 'Gonzalez', 'legajo': 1002, 'parciales': [{'materia': 'Algoritmos y Estructuras de Datos', 'nota': 6, 'fecha': '2023-06-01'}, {'materia': 'Base de Datos', 'nota': 3, 'fecha': '2023-05-20'}]},
#     {'nombre': 'Maria', 'apellido': 'Lopez', 'legajo': 1003, 'parciales': [{'materia': 'Algoritmos y Estructuras de Datos', 'nota': 7, 'fecha': '2023-06-05'}, {'materia': 'Base de Datos', 'nota': 8, 'fecha': '2023-05-25'}]},
#     {'nombre': 'Pedro', 'apellido': 'Ramirez', 'legajo': 1004, 'parciales': [{'materia': 'Algoritmos y Estructuras de Datos', 'nota': 8, 'fecha': '2023-05-10'}, {'materia': 'Base de Datos', 'nota': 7, 'fecha': '2023-05-15'}]},
#     {'nombre': 'Laura', 'apellido': 'Torres', 'legajo': 1005, 'parciales': [{'materia': 'Algoritmos y Estructuras de Datos', 'nota': 6, 'fecha': '2023-06-01'}, {'materia': 'Base de Datos', 'nota': 9, 'fecha': '2020-05-20'}]},
#     {'nombre': 'Carlos', 'apellido': 'Flores', 'legajo': 1006, 'parciales': [{'materia': 'Ingenieria II', 'nota': 7, 'fecha': '2023-06-05'}, {'materia': 'Base de Datos', 'nota': 2, 'fecha': '2023-05-25'}]}
# ]


# class Alumno:
#     def __init__(self, nombre, apellido, legajo, parciales):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.legajo = legajo
#         self.parciales = parciales
    
#     def __str__(self):
#         return f'{self.nombre} {self.apellido} {self.legajo} {self.parciales}'

# def by_nombre(item):
#     return item.nombre

# def by_apellido(item):
#     return item.apellido

# def by_legajo(item):
#     return item.legajo


# l = List()
# for i in alumnos:
#     l.append(Alumno(i['nombre'], i['apellido'], i['legajo'], i['parciales']))

# l.add_criterion('nombre', by_nombre)
# l.add_criterion('apellido', by_apellido)
# l.add_criterion('legajo', by_legajo)

# l.sort_by_criterion('apellido')
# print('a. mostrar los alumnos ordenados alfabéticamente por apellido:')
# l.show()

# #b. indicar los alumnos que no desaprobaron ningún parcial;
# print(' - indicar los alumnos que no desaprobaron ningún parcial:')
# for alumno in l:
#     aprobo_todos = True
#     for parcial in alumno.parciales:
#         if parcial['nota'] < 6:
#             aprobo_todos = False
#             break
#     if aprobo_todos:
#         print(f'{alumno.nombre} {alumno.apellido} no desaprobo ningun parcial')
# print()

# #c. determinar los alumnos que tienen promedio mayor a 8,89;
# print(' - determinar los alumnos que tienen promedio mayor a 8,89:')
# for alumno in l:
#     suma = 0
#     for parcial in alumno.parciales:
#         suma += parcial['nota']
#     promedio = suma / len(alumno.parciales)
#     if promedio > 8.89:
#         print(f'{alumno.nombre} {alumno.apellido} tiene un promedio mayor a 8.89. Su promedio es: {promedio:.2f}')
# print()
# #d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
# print(' - mostrar toda la información de los alumnos cuyos apellidos comienzan con L:')
# l.filter_start_with('L', 'apellido')
# print()

# #e. mostrar el promedio de cada uno de los alumnos;
# print(' - mostrar el promedio de cada uno de los alumnos:')
# for alumno in l:
#     suma= 0
#     for parcial in alumno.parciales:
#         suma += parcial['nota']
#     promedio = suma / len(alumno.parciales)
#     print(f'{alumno.nombre} {alumno.apellido} tiene un promedio de: {promedio:.2f}')
# print()
# #f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
# print(' - mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”:')
# for alumnos in l:
#     for parcial in alumnos.parciales:
#         if parcial['materia'] == 'Algoritmos y Estructuras de Datos':
#             print(f'{alumnos.nombre} {alumnos.apellido} rindio la catedra "Algoritmos y Estructuras de Datos"')
# print()

# #g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
# print(' - indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario:')
# nombre_buscar = str(input('ingrese el nombre del alumno: '))
# l.sort_by_criterion('nombre')
# pos = l.search(nombre_buscar, 'nombre')

# if pos is None:
#     print(f'No se encontro al Alumno {nombre_buscar}')
# else:
#     alumno = l[pos]
#     aprobados = 0
#     for parcial in alumno.parciales:
#         if parcial['nota'] >= 6:
#             aprobados += 1
#     porcentaje = (aprobados / len(alumno.parciales)) * 100
#     print(f'{alumno.nombre} {alumno.apellido} tiene un porcentaje de {porcentaje}% de parciales aprobados')
# print()

# #h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
# print(' - indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”:')
# aprobados = 0
# desaprobados = 0

# for alumno in l:
#     for parcial in alumno.parciales:
#         if parcial['materia'] == 'Base de Datos':
#             if parcial['nota'] >= 6:
#                 aprobados +=1
#             else:
#                 desaprobados += 1

# print(f'alumnos aprobados en base de datos: {aprobados}')
# print(f'alumnos desaprobados en base de datos: {desaprobados}')
# print()

# # i. mostrar todos los alumnos que rindieron en el año 2020;
# print(' - mostrar todos los alumnos que rindieron en el año 2020:')
# for alumno in l:
#     for parcial in alumno.parciales:
#         if parcial['fecha'][:4] == '2020':
#             print(f'{alumno.nombre} {alumno.apellido} rindio en el año 2020')
#             break

# # j. debe modificar el TDA para implementar lista de lista. #no lo voy hacer, no lo entiendo.




#10. Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artista, 
# duración y cantidad de reproducciones durante el último mes. 
# Desarrollar un algoritmo que permita realizar las siguientes actividades:
# a. obtener la información de la canción más larga;
# b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
# c. obtener todas las canciones de la banda Arctic Monkeys;
# d. mostrar los nombres de las bandas o artistas que solo son de una palabra.
# canciones = [
#     {'nombre': 'Shape of You', 'artista': 'Ed Sheeran', 'duracion': 233, 'reproducciones': 2995000000},
#     {'nombre': 'Blinding Lights', 'artista': 'The Weeknd', 'duracion': 200, 'reproducciones': 3460000000},
#     {'nombre': 'Bohemian Rhapsody', 'artista': 'Queen', 'duracion': 355, 'reproducciones': 1797000000},
#     {'nombre': 'Hotel California', 'artista': 'Eagles', 'duracion': 390, 'reproducciones': 1500000000},
#     {'nombre': '505', 'artista': 'Arctic Monkeys', 'duracion': 482, 'reproducciones': 890000000},
#     {'nombre': 'Smells Like Teen Spirit', 'artista': 'Nirvana', 'duracion': 301, 'reproducciones': 1439000000},
#     {'nombre': 'Sweet Child o Mine', 'artista': "Guns N'Roses", 'duracion': 356, 'reproducciones': 1173000000},
#     {'nombre': 'One More Time', 'artista': 'Daft Punk', 'duracion': 320, 'reproducciones': 753000000},
#     {'nombre': 'Back in Black', 'artista': 'AC/DC', 'duracion': 255, 'reproducciones': 673000000},
#     {'nombre': 'Do I Wanna Know?', 'artista': 'Arctic Monkeys', 'duracion': 183, 'reproducciones': 1034000000}
# ]

# class Cancion:
#     def __init__ (self, nombre, artista, duracion, reproducciones):
#         self.nombre = nombre
#         self.artista = artista
#         self.duracion = duracion
#         self.reproducciones = reproducciones

#     def __str__ (self):
#         return f'nombre: {self.nombre} | artista: {self.artista} | duracion: {self.duracion} | reproducciones: {self.reproducciones}'


# def by_nombre(item): #vemos si sirve
#     return item.nombre

# def by_artista(item):
#     return item.artista

# def by_duracion(item):
#     return item.duracion

# def by_reproducciones(item):
#     return item.reproducciones

# l = List()

# l.add_criterion('nombre', by_nombre)
# l.add_criterion('artista', by_artista)
# l.add_criterion('duracion', by_duracion)
# l.add_criterion('reproducciones', by_reproducciones)

# for i in canciones:
#     l.append(Cancion(i['nombre'], i['artista'], i['duracion'], i['reproducciones']))

# l.show()

# #a. obtener la información de la canción más larga;
# l.sort_by_criterion('duracion')
# mas_larga = l[l.size() -1]
# print(f'a) La cancion mas larga es: {mas_larga}')
# print()

# #b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
# l.sort_by_criterion('reproducciones')
# for top in [5, 10, 40]:
#     print(f'\nb. TOP {top} canciones mas escuchadas: ')
#     for i in range(min(top, l.size())):
#         idx = l.size() -1 - i 
#         cancion = l[idx]
#         print(f'   {i+1}. {cancion.nombre} - {cancion.artista} ({cancion.reproducciones:,} reproducciones)')
# print()

# #c. obtener todas las canciones de la banda Arctic Monkeys;
# print('c. canciones de arctic monkeys: ')
# for cancion in l:
#     if cancion.artista == "Arctic Monkeys":
#         print(cancion)

# #d. mostrar los nombres de las bandas o artistas que solo son de una palabra.
# print('d. bandas o artistas de una palabra: ')
# ya_mostrados = List()

# for cancion in l:
#     if len(cancion.artista.split()) == 1 and cancion.artista not in ya_mostrados:
#         print(f'. {cancion.artista}')
#         ya_mostrados.append(cancion.artista)


# 11. Dada una lista que contiene información de los personajes de la saga de Star Wars con la si-
# guiente información nombre, altura, edad, género, especie, planeta natal y episodios en los que
# apareció, desarrollar los algoritmos que permitan realizar las siguientes actividades:
# a. listar todos los personajes de género femenino;
# b. listar todos los personajes de especie Droide que aparecieron en los primeros seis episo-
# dios de la saga;
# c. mostrar toda la información de Darth Vader y Han Solo;
# d. listar los personajes que aparecen en el episodio VII y en los tres anteriores;
# e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
# f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI;
# g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;
# h. mostrar toda la información de los personajes cuya altura es menor a 70 centímetros;
# i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información.
        
# personajes_starwars = [
    
#     {'nombre': 'Luke Skywalker', 'altura': 172, 'edad': 19, 'genero': 'Masculino', 'especie': 'Humano', 'planeta_natal': 'Tatooine', 'episodios': [4, 5, 6, 7, 8, 9]},
#     {'nombre': 'Leia Organa', 'altura': 150, 'edad': 19, 'genero': 'Femenino', 'especie': 'Humano', 'planeta_natal': 'Alderaan', 'episodios': [4, 5, 6, 7, 8, 9]},
#     {'nombre': 'Han Solo', 'altura': 180, 'edad': 29, 'genero': 'Masculino', 'especie': 'Humano', 'planeta_natal': 'Corellia', 'episodios': [4, 5, 6, 7, 8, 9]},
#     {'nombre': 'Chewbacca', 'altura': 228, 'edad': 200, 'genero': 'Masculino', 'especie': 'Wookiee', 'planeta_natal': 'Kashyyyk', 'episodios': [4, 5, 6, 7, 8, 9]},
#     {'nombre': 'Darth Vader', 'altura': 202, 'edad': 45, 'genero': 'Masculino', 'especie': 'Humano', 'planeta_natal': 'Tatooine', 'episodios': [4, 5, 6, 1, 2, 3]},
#     {'nombre': 'Obi-Wan Kenobi', 'altura': 182, 'edad': 38, 'genero': 'Masculino', 'especie': 'Humano', 'planeta_natal': 'Stewjon', 'episodios': [4, 5, 6, 1, 2, 3]},
#     {'nombre': 'Yoda', 'altura': 66, 'edad': 900, 'genero': 'Masculino', 'especie': 'Desconocido', 'planeta_natal': 'Desconocido', 'episodios': [1, 2, 3, 4, 5, 6]},
#     {'nombre': 'R2-D2', 'altura': 96, 'edad': 10, 'genero': 'Masculino', 'especie': 'Droide', 'planeta_natal': 'Naboo', 'episodios': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
#     {'nombre': 'C-3PO', 'altura': 167, 'edad': 10, 'genero': 'Masculino', 'especie': 'Droide', 'planeta_natal': 'Tatooine', 'episodios': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
#     {'nombre': 'BB-8', 'altura': 67, 'edad': 995, 'genero': 'Masculino', 'especie': 'Droide', 'planeta_natal': 'Desconocido', 'episodios': [7, 8, 9]},
#     {'nombre': 'Rey', 'altura': 170, 'edad': 19, 'genero': 'Femenino', 'especie': 'Humano', 'planeta_natal': 'Jakku', 'episodios': [7, 8, 9]},
#     {'nombre': 'Finn', 'altura': 178, 'edad': 23, 'genero': 'Masculino', 'especie': 'Humano', 'planeta_natal': 'Desconocido', 'episodios': [7, 8, 9]},
#     {'nombre': 'Poe Dameron', 'altura': 178, 'edad': 27, 'genero': 'Masculino', 'especie': 'Humano', 'planeta_natal': 'Desconocido', 'episodios': [7, 8, 9]},
#     {'nombre': 'Kylo Ren', 'altura': 189, 'edad': 23, 'genero': 'Masculino', 'especie': 'Humano', 'planeta_natal': 'Jakku', 'episodios': [4,5,6]},
#     {'nombre': 'Lando Calrissian', 'altura': 177, 'edad': 31, 'genero': 'Masculino', 'especie': 'Humano', 'planeta_natal': 'Corellia', 'episodios': [4, 5, 6, 9]},
#     {'nombre': 'Padmé Amidala', 'altura': 165, 'edad': 14, 'genero': 'Femenino', 'especie': 'Humano', 'planeta_natal': 'Naboo', 'episodios': [1, 2, 3]},
#     {'nombre': 'Anakin Skywalker', 'altura': 185, 'edad': 22, 'genero': 'Masculino', 'especie': 'Humano', 'planeta_natal': 'Tatooine', 'episodios': [1, 2, 3, 4, 5, 6]},
#     {'nombre': 'Palpatine', 'altura': 173, 'edad': 88, 'genero': 'Masculino', 'especie': 'Humano', 'planeta_natal': 'Naboo', 'episodios': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
#     {'nombre': 'Mace Windu', 'altura': 182, 'edad': 52, 'genero': 'Masculino', 'especie': 'Humano', 'planeta_natal': 'Haruun Kal', 'episodios': [1, 2, 3]},
#     {'nombre': 'Captain Phasma', 'altura': 188, 'edad': 29, 'genero': 'Femenino', 'especie': 'Humano', 'planeta_natal': 'Alderaan', 'episodios': [7, 8]}
# ]


# class Personaje_starwars:
#     def __init__(self, nombre, altura, edad, genero, especie, planeta_natal, episodios):
#         self.nombre = nombre
#         self.altura = altura
#         self.edad = edad
#         self.genero = genero
#         self.especie = especie
#         self.planeta_natal = planeta_natal
#         self.episodios = episodios
    
#     def __str__(self):
#         return f'nombre: {self.nombre} | altura: {self.altura} | edad: {self.edad} | genero: {self.genero} | especie: {self.especie} | planeta natal: {self.planeta_natal} | episodios: {self.episodios}'




# def by_nombre(item):
#     return item.nombre

# def by_edad(item):
#     return item.edad

# def by_altura(item):
#     return item.altura

# l = List()
# l.add_criterion('nombre', by_nombre)
# l.add_criterion('edad', by_edad)
# l.add_criterion('altura', by_altura)
# for i in personajes_starwars:
#     l.append(Personaje_starwars(i['nombre'], i['altura'], i['edad'], i['genero'], i['especie'], i['planeta_natal'], i['episodios']))

# # a. listar todos los personajes de género femenino;
# print('a. personajes de genero femenino: ')
# for personaje in l:
#     if personaje.genero == 'Femenino':    
#         print(f'- {personaje.nombre}')
# print()

# #b. listar todos los personajes de especie Droide que aparecieron en los primeros seis episo-
# # dios de la saga;
# print('b. Droide que aparecieron en los primeros 6 episodios: ')
# for personaje in l:
#     if personaje.especie == 'Droide' and any(ep <= 6 for ep in personaje.episodios):
#         print(f'- {personaje.nombre}')
# print()

# #c. mostrar toda la información de Darth Vader y Han Solo;
# print('c. Darth Vader y Han Solo')
# l.sort_by_criterion('nombre')
# Darth_Vader = l.search('Darth Vader', 'nombre')
# Han_solo = l.search('Han Solo', 'nombre')
# if Darth_Vader is not None:
#     print(l[Darth_Vader])
# else:
#     print('Darth Vader no encontrado')
# if Han_solo is not None:
#     print(l[Han_solo])
# else:
#     print('Han Solo no encontrado')
# print()

# # d. listar los personajes que aparecen en el episodio VII y en los tres anteriores;
# print('d. personajes que aparecen en el episodio VII y en los tres anteriores: ')
# for personaje in l:
#     if 7 in personaje.episodios and 4 in personaje.episodios and 5 in personaje.episodios and 6 in personaje.episodios:
#         print(f'- {personaje.nombre}')
# print()

# #e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
# print('e. personajes con edad mayor a 850 años y el mayor: ')
# l.sort_by_criterion('edad')
# for personaje in l:
#     if personaje.edad > 850:
#         print(f'-{personaje.nombre}')
        
# print(f'-el mayor es {l[-1].nombre}')

# #f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI;
# print('f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI:')
# a_eliminar = []
# for personaje in l:
#     solo_456 = True
#     for ep in personaje.episodios:
#         if ep not in [4,5,6]:
#             solo_456 = False
#             break
#     if solo_456:
#         a_eliminar.append(personaje.nombre)

# for nombre in a_eliminar:
#     l.sort_by_criterion('nombre')
#     eliminado = l.delete_value(nombre, 'nombre')
#     print(f'-personaje eliminado: {eliminado.nombre}')

# print(a_eliminar)
# print()

# #g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;
# print('g. personajes de especie humana cuyo planeta de origen es Alderaan: ')
# for personajes in l:
#     if personajes.especie == 'Humano' and personajes.planeta_natal == 'Alderaan':
#         print(f'- {personajes.nombre}')
# print()

# #h. mostrar toda la información de los personajes cuya altura es menor a 70 centímetros;
# print('h. personajes con altura menor a 70 cm:')
# l.sort_by_criterion('altura')
# for personaje in l:
#     if personaje.altura < 70:
#         print(f'- {personaje}')
# print()

# #i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información.
# print('i. episodios en los que aparece Chewbacca')
# l.sort_by_criterion('nombre')
# Chewbacca = l.search('Chewbacca', 'nombre')

# if Chewbacca is not None:
#     print(f" episodios en los que aparece Chewbacca: {l[Chewbacca].episodios}")
#     print(l[Chewbacca])
# else:
#     print('Chewbacca no encontrado')
# print()


#16. Se deben administrar las actividades de un proyecto de software, de estas se conoce su costo,
# tiempo de ejecución, fecha de inicio, fecha de fin estimada, fecha de fin efectiva y persona a
# cargo. Desarrollar un algoritmo que realice las siguientes actividades:
# a. tiempo promedio de tareas;
# b. costo total del proyecto;
# c. actividades realizadas por una determinada persona;
# d. mostrar la información de las tareas a realizar entre dos fechas dadas;
# e. mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo;
# f. indicar cuántas tareas le quedan pendientes a una determinada persona, indicada por
# el usuario.

# actividades = [
#     {'nombre': 'Relevamiento de requisitos',   'costo': 5000,  'tiempo_ejecucion': 10, 'fecha_inicio': '2024-01-05', 'fecha_fin_estimada': '2024-01-15', 'fecha_fin_efectiva': '2024-01-14', 'persona_cargo': 'Ana Lopez'},
#     {'nombre': 'Diseño de base de datos',      'costo': 8000,  'tiempo_ejecucion': 15, 'fecha_inicio': '2024-01-16', 'fecha_fin_estimada': '2024-01-31', 'fecha_fin_efectiva': '2024-02-05', 'persona_cargo': 'Carlos Perez'},
#     {'nombre': 'Desarrollo del backend',       'costo': 20000, 'tiempo_ejecucion': 30, 'fecha_inicio': '2024-02-01', 'fecha_fin_estimada': '2024-03-02', 'fecha_fin_efectiva': '2024-03-01', 'persona_cargo': 'Ana Lopez'},
#     {'nombre': 'Desarrollo del frontend',      'costo': 15000, 'tiempo_ejecucion': 25, 'fecha_inicio': '2024-02-10', 'fecha_fin_estimada': '2024-03-06', 'fecha_fin_efectiva': '2024-03-10', 'persona_cargo': 'Maria Gomez'},
#     {'nombre': 'Testing y QA',                 'costo': 7000,  'tiempo_ejecucion': 12, 'fecha_inicio': '2024-03-07', 'fecha_fin_estimada': '2024-03-19', 'fecha_fin_efectiva': '2024-03-18', 'persona_cargo': 'Carlos Perez'},
#     {'nombre': 'Despliegue en produccion',     'costo': 3000,  'tiempo_ejecucion': 5,  'fecha_inicio': '2024-03-20', 'fecha_fin_estimada': '2024-03-25', 'fecha_fin_efectiva': None,          'persona_cargo': 'Ana Lopez'},
#     {'nombre': 'Capacitacion a usuarios',      'costo': 4000,  'tiempo_ejecucion': 8,  'fecha_inicio': '2024-03-26', 'fecha_fin_estimada': '2024-04-03', 'fecha_fin_efectiva': None,          'persona_cargo': 'Maria Gomez'},
#     {'nombre': 'Documentacion del sistema',    'costo': 2500,  'tiempo_ejecucion': 7,  'fecha_inicio': '2024-01-20', 'fecha_fin_estimada': '2024-01-27', 'fecha_fin_efectiva': '2024-01-30', 'persona_cargo': 'Maria Gomez'},
# ]

# class actividad:
#     def __init__(self, nombre, costo, tiempo_ejecucion, fecha_inicio, fecha_fin_estimada, fecha_fin_efectiva, persona_cargo):
#         self.nombre = nombre
#         self.costo = costo
#         self.tiempo_ejecucion = tiempo_ejecucion
#         self.fecha_inicio = fecha_inicio
#         self.fecha_fin_estimada = fecha_fin_estimada
#         self.fecha_fin_efectiva = fecha_fin_efectiva
#         self.persona_cargo = persona_cargo

#     def __str__(self):
#         return f'nombre: {self.nombre} | costo: {self.costo} | tiempo_ejecucion: {self.tiempo_ejecucion} | fecha_inicio: {self.fecha_inicio} | fecha_fin_estimada: {self.fecha_fin_estimada} | fecha_fin_efectiva: {self.fecha_fin_efectiva} | persona_cargo: {self.persona_cargo}'


# def by_persona_cargo(item):
#     return item.persona_cargo

# def by_fecha_inicio(item):
#     return item.fecha_inicio

# l = List()
# l.add_criterion('persona_cargo', by_persona_cargo)
# l.add_criterion('fecha_inicio', by_fecha_inicio)

# for i in actividades:
#     l.append(actividad(i['nombre'], i['costo'], i['tiempo_ejecucion'], i['fecha_inicio'], i['fecha_fin_estimada'], i['fecha_fin_efectiva'], i['persona_cargo']))

# #a. tiempo promedio de tareas;
# print('a. tiempo promedio de tareas: ')
# suma = 0
# for actividad in l:
#     suma += actividad.tiempo_ejecucion
# promedio = suma / l.size()
# print(f'-el tiempo promedio de tareas es: {promedio} ') 
# print()

# #b. costo total del proyecto;
# print('b. costo total del proyecto:')
# suma = 0
# for actividad in l:
#     suma += actividad.costo
# print(f'- el costo total del proyecto es: ${suma}')
# print()

# #c. actividades realizadas por una determinada persona;
# print('c. actividades realizadas por una determinada persona:')
# nombre_buscar = str(input('ingrese la persona a buscar: '))
# existe = l.search(nombre_buscar, 'persona_cargo')

# if existe is None:
#     print(f'la persona {nombre_buscar} no existe en la lista')
# else:
#     print(f'la persona {nombre_buscar} trabajo en las actividades: ')
#     for actividad in l:
#         if actividad.persona_cargo == nombre_buscar:
#             print(f'-{actividad.nombre}')
# print()

# #d. mostrar la información de las tareas a realizar entre dos fechas dadas;
# fecha_desde = str(input('ingrese la fecha inicio (formato ej: 2024-01-01): '))
# fecha_hasta = str(input('ingrese la fecha fin (formato ej: 2024-01-01): '))

# l.sort_by_criterion('fecha_inicio')
# print(f'tareas entre {fecha_desde} y {fecha_hasta}:')
# for actividad in l:
#     if fecha_desde <= actividad.fecha_inicio <= fecha_hasta:
#         print(f'- {actividad}')
# print()

# #e. mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo;
# print('e. tareas finalizadas en tiempo y fuera de tiempo:')
# print('tareas finalizadas en tiempo: ')
# for actividad in l:
#     if actividad.fecha_fin_efectiva is not None and actividad.fecha_fin_efectiva > actividad.fecha_fin_estimada:
#         print(f'- {actividad.nombre}')


# #f. indicar cuántas tareas le quedan pendientes a una determinada persona, indicada por
# # el usuario.
# print('f. tareas pendientes de cada persona')
# nombre_buscar = str(input('ingrese la persona a buscar: '))
# l.sort_by_criterion('persona_cargo')
# existe = l.search(nombre_buscar, 'persona_cargo')

# if existe is None:
#     print(f'la persona {nombre_buscar} no existe en la lista')
# else:
#     pendientes = 0
#     for actividad in l:
#         if actividad.persona_cargo == nombre_buscar and actividad.fecha_fin_efectiva is None:
#             pendientes += 1
#     print(f'la persona {nombre_buscar} tiene {pendientes} tareas pendientes')
# print()


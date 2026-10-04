from random import randint

from tree import BinaryTree
from queue_ import Queue


# 1.Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea-
# toria– que resuelva las siguientes actividades:
# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.





# Funciones auxiliares (no estan en BinaryTree, se arman por afuera
# usando los atributos publicos de Node: value, left, right)
# def altura(nodo) -> int:
#     """Altura de un (sub)arbol. Arbol vacio = -1, un solo nodo = 0."""
#     if nodo is None:
#         return -1

#     return 1 + max(altura(nodo.left), altura(nodo.right))


# def contar_ocurrencias(nodo, valor: int) -> int:
#     """Cuenta cuantas veces aparece 'valor' recorriendo todo el arbol."""
#     if nodo is None:
#         return 0

#     ocurrencias = 1 if nodo.value == valor else 0
#     ocurrencias += contar_ocurrencias(nodo.left, valor)
#     ocurrencias += contar_ocurrencias(nodo.right, valor)

#     return ocurrencias


# def contar_pares_impares(nodo, pares: int = 0, impares: int = 0):
#     """Recorre todo el arbol y cuenta pares e impares."""
#     if nodo is None:
#         return pares, impares

#     if nodo.value % 2 == 0:
#         pares += 1
#     else:
#         impares += 1

#     pares, impares = contar_pares_impares(nodo.left, pares, impares)
#     pares, impares = contar_pares_impares(nodo.right, pares, impares)

#     return pares, impares


# def recorrido_por_nivel(raiz) -> None:
#     """Recorrido BFS (por nivel) usando la clase Queue del repo."""
#     if raiz is None:
#         return

#     cola = Queue()
#     cola.arrive(raiz)

#     while cola.size() > 0:
#         nodo = cola.attention()
#         print(nodo.value)

#         if nodo.left is not None:
#             cola.arrive(nodo.left)
#         if nodo.right is not None:
#             cola.arrive(nodo.right)

# # ver repo del profe, porque hicimos barrido por nivel. hacer 1 de vuelta.


# arbol = BinaryTree()
# numeros_cargados = []

# for i in range(1000):
#     numero = randint(1, 10000)
#     arbol.insert_node(numero, None)
#     numeros_cargados.append(numero)


# # a. Barridos preorden, inorden, postorden y por nivel

# print('--- PREORDEN ---')
# arbol.preorden()

# print()
# print('--- INORDEN ---')
# arbol.inorden()

# print()
# print('--- POSTORDEN ---')
# arbol.postorden()

# print()
# print('--- POR NIVEL ---')
# recorrido_por_nivel(arbol.root)


# # b. Determinar si un numero esta cargado en el arbol

# print()
# numero_buscado = numeros_cargados[0]
# resultado_busqueda = arbol.search(numero_buscado)

# if resultado_busqueda is not None:
#     print(f'el numero {numero_buscado} SI esta cargado en el arbol')
# else:
#     print(f'el numero {numero_buscado} NO esta cargado en el arbol')


# # c. Eliminar tres valores del arbol

# print()
# valores_a_eliminar = numeros_cargados[:3]

# for valor in valores_a_eliminar:
#     eliminado = arbol.delete_node(valor)
#     print(f'valor eliminado: {eliminado}')



# # d. Altura del subarbol izquierdo y del subarbol derecho

# print()
# altura_izquierda = altura(arbol.root.left)
# altura_derecha = altura(arbol.root.right)

# print(f'altura del subarbol izquierdo: {altura_izquierda}')
# print(f'altura del subarbol derecho: {altura_derecha}')


# # e. Cantidad de ocurrencias de un elemento en el arbol

# print()
# valor_a_contar = numeros_cargados[10]
# cantidad_ocurrencias = contar_ocurrencias(arbol.root, valor_a_contar)
# print(f'el numero {valor_a_contar} aparece {cantidad_ocurrencias} veces en el arbol')


# # f. Cantidad de numeros pares e impares

# print()
# pares, impares = contar_pares_impares(arbol.root)
# print(f'cantidad de numeros pares: {pares}')
# print(f'cantidad de numeros impares: {impares}')


# #5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# # se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# # a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# # leano que indica si es un héroe o un villano, True y False respectivamente;

# # b. listar los villanos ordenados alfabéticamente;
# # c. mostrar todos los superhéroes que empiezan con C;
# # d. determinar cuántos superhéroes hay el árbol;
# # e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# # encontrarlo en el árbol y modificar su nombre;
# # f. listar los superhéroes ordenados de manera descendente;
# # g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# # los villanos, luego resolver las siguiente tareas:
# # I. determinar cuántos nodos tiene cada árbol;
# # II. realizar un barrido ordenado alfabéticamente de cada árbol.


# from super_heroes_data import superheroes
# from tree import BinaryTree

# class MarvelCharacter():

#     def __init__(self, nombre, anio, casa, bio):
#         self.name = nombre
#         self.year = anio
#         self.house = casa
#         self.bio = bio

#     def __str__(self):
#         return f"{self.name} - {self.year} - {self.house}"
    


# arbol_marvel = BinaryTree()

# print(f'cantidad de elementos {len(superheroes)}')
# #A
# for marvel_character in superheroes:
#     arbol_marvel.insert_node(marvel_character['name'], other_value=marvel_character)

# # #B
# # arbol_marvel.inorden_villain()


# # #C
# # arbol_marvel.inorden_hero_star_with('An')

# # #D
# # print(f'cantidad de heroes: {arbol_marvel.count_heroes()}')

# # E
# search_str = input('ingrese lo que quiere buscar: ')
# arbol_marvel.proxy_search(search_str.lower())

# search_str = input('ingrese lo que quiere modificar: ')

# node = arbol_marvel.search(search_str)
# if node is not None:
#     new_name = input('ingrese el nuevo nombre: ')
#     delete_value, delete_other_value = arbol_marvel.delete_node(node.value)
#     delete_other_value['name'] = new_name
#     arbol_marvel.insert_node(new_name, delete_other_value)

# print()
# arbol_marvel.inorden_hero_star_with('D')

# # F
# arbol_marvel.postorden_hero()

#G


# -------------------------------------------------------------------------------------------------













#VAMOS DE VUELTA

# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea-
# toria– que resuelva las siguientes actividades:

# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.

# arbol = BinaryTree()
# numeros = []

# for _ in range(1000):
#     n = randint(1,10000)
#     arbol.insert_node(n)
#     numeros.append(n)

# # a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# arbol.preorden()
# arbol.inorden()
# arbol.postorden()
# arbol.by_level()

# # b. determinar si un número está cargado en el árbol o no;
# valor_buscado = numeros[23]
# nodo = arbol.search(valor_buscado)

# if nodo is not None:
#     print(f'el numero {valor_buscado} si esta cargado en el arbol')
# else:
#     print(f'el numero {valor_buscado} no esta cargado en el arbol')

# # c. eliminar tres valores del árbol;
# valores_a_eliminar = numeros[:3]

# for valor in valores_a_eliminar:
#     eliminado, other_value = arbol.delete_node(valor)
#     print(f'valor eliminado: {eliminado}')
    
# # d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# altura_izq = arbol.height(arbol.root.left)
# altura_der = arbol.height(arbol.root.right)

# print(f'altura del subarbol izquierdo: {altura_izq}')
# print(f'altura del subarbol derecho: {altura_der}')

# # e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# def contar_ocurrencias(nodo, valor):
#     if nodo is None:
#         return 0
#     if valor < nodo.value:
#         return contar_ocurrencias(nodo.left, valor)
#     elif valor > nodo.value:
#         return contar_ocurrencias(nodo.right, valor)
#     else:
#         return 1 + contar_ocurrencias(nodo.right, valor)
    
# valor_a_encontrar = numeros[23]
# cantidad = contar_ocurrencias(arbol.root, valor_a_encontrar)
# print(f'el numero {valor_a_encontrar} aparece {cantidad} veces en el arbol')

# # f. contar cuántos números pares e impares hay en el árbol.
# def contar_pares_impares(nodo, pares=0, impares=0):
#     if nodo is None:
#         return pares, impares
    
#     if nodo.value % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
        
#     pares, impares = contar_pares_impares(nodo.left, pares, impares)
#     pares, impares = contar_pares_impares(nodo.right, pares, impares)
#     return pares, impares

# pares, impares = contar_pares_impares(arbol.root)
# print(f'cantidad de numeros pares: {pares}')
# print(f'cantidad de numeros impares: {impares}')



# 4. Implementar un algoritmo que contemple dos funciones, la primera que devuelva el hijo dere-
# cho de un nodo y la segunda que devuelva el hijo izquierdo.

# def hijo_derecho(nodo):
#     return nodo.right

# def hijo_izquierdo(nodo):
#     return nodo.left

# arbol = BinaryTree()
# for valor in [50, 30, 70, 20, 40, 60, 80]:
#     arbol.insert_node(valor)
    
# arbol.inorden()

# nodo = arbol.search(30)
# derecho = hijo_derecho(nodo)
# izquierdo = hijo_izquierdo(nodo)

# print(f'hijo derecho de 30: {derecho.value if derecho is not None else "no tiene"}')
# print(f'hijo izquierdo de 30: {izquierdo.value if izquierdo is not None else "no tiene"}')


# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;

# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
    # I. determinar cuántos nodos tiene cada árbol;
    # II. realizar un barrido ordenado alfabéticamente de cada árbol.
    
# from super_heroes_data import superheroes

# arbol_marvel = BinaryTree()

# for personaje in superheroes:
#     arbol_marvel.insert_node(personaje['name'], other_value=personaje)
    
    
# # b. listar los villanos ordenados alfabéticamente;
# arbol_marvel.inorden_villain()

# # c. mostrar todos los superhéroes que empiezan con C;
# arbol_marvel.inorden_hero_star_with('C')

# # d. determinar cuántos superhéroes hay el árbol;
# cantidad_heroes = arbol_marvel.count_heroes()
# print(f'- cantidad de heroes: {cantidad_heroes}')

# # e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# # encontrarlo en el árbol y modificar su nombre;
# arbol_marvel.proxy_search('str')

# nodo_encontrado = arbol_marvel.search('Dr Strannnnnge')

# if nodo_encontrado is not None:
#     valor_viejo, datos = arbol_marvel.delete_node(nodo_encontrado.value)
#     datos['name'] = 'Dr Strange'
#     arbol_marvel.insert_node('Dr Strange', datos)

# # f. listar los superhéroes ordenados de manera descendente;
# arbol_marvel.postorden_hero()

# # g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# # los villanos, luego resolver las siguiente tareas:
# arbol_heroes = BinaryTree()
# arbol_villanos = BinaryTree()

# def generar_bosque(nodo):
#     if nodo is None:
#         return
#     if nodo.other_values['is_villain']:
#         arbol_villanos.insert_node(nodo.value, nodo.other_values)
#     else:
#         arbol_heroes.insert_node(nodo.value, nodo.other_values)
#     generar_bosque(nodo.left)
#     generar_bosque(nodo.right)
    
# generar_bosque(arbol_marvel.root)

# # I. determinar cuántos nodos tiene cada árbol;
# def contar_nodos(nodo):
#     if nodo is None:
#         return 0
#     return 1 + contar_nodos(nodo.left) + contar_nodos(nodo.right)

# print(f'nodos en arbol de heroes: {contar_nodos(arbol_heroes.root)}')
# print(f'nodos en arbol de villanos: {contar_nodos(arbol_villanos.root)}')

# # II. realizar un barrido ordenado alfabéticamente de cada árbol.
# arbol_heroes.inorden()
# arbol_villanos.inorden()





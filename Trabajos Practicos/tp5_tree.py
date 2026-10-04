import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from tree import BinaryTree
from super_heroes_data import superheroes



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




# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

from tabla_ejericio_23 import criaturas
tree = BinaryTree()
for c in criaturas:
    tree.insert_node(c["name"], {"derrotado_por": c["derrotado_por"], "descripcion": None, "capturada": None}) #agregamos los campos que pide el punto g

# a. listado inorden de las criaturas y quienes la derrotaron;

def inorden_criaturas(self): #podria ir en el archivo tree.py como hizo el profe con el punto 5.
    
    def __inorden_criaturas(root):
        if root.left is not None:
            __inorden_criaturas(root.left)
        print(root.value, '-', root.other_values['derrotado_por'])
        if root.right is not None:
            __inorden_criaturas(root.right)
    __inorden_criaturas(self.root)

inorden_criaturas(tree) 

# b. se debe permitir cargar una breve descripción sobre cada criatura;
# ingresar_criatura = input(str('ingrese la criatura: '))
# ingresar_descripcion = input(str('ingrese la descripcion: '))

# nodo = tree.search(ingresar_criatura)
# nodo.other_values['descripcion'] = ingresar_descripcion

# # c. mostrar toda la información de la criatura Talos;
# nodo = tree.search('Talos')
# print(nodo.value, nodo.other_values)

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
def inorden_derrotado_por(self, heroe) -> None:
        
    def __inorden_derrotado_por(root, heroe):
        if root.left is not None:
            __inorden_derrotado_por(root.left, heroe)
        if root.other_values['derrotado_por'] == heroe:
            print(root.value)
        if root.right is not None:
            __inorden_derrotado_por(root.right, heroe)

    __inorden_derrotado_por(self.root, heroe)
    
inorden_derrotado_por('Heracles')
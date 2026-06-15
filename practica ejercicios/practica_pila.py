from copy import copy, deepcopy
from typing import Any
from random import randint, choice, random


"""# --- EJERCICIO X: [Título del ejercicio] ---
from tda_pila import Stack # O la clase que te dio tu profe

# 1. Preparación de pilas
pila = Stack()
paux = Stack()

# 2. Carga de datos (o recepción por input)
# ... [Lógica de carga] ...

# 3. Procesamiento (El corazón del ejercicio)
# Si necesitas contar, eliminar, buscar o reemplazar, va aquí:
while pila.size() > 0:
    dato = pila.pop()
    
    # [ACÁ VA LA LÓGICA ESPECÍFICA DEL EJERCICIO]
    # Ejemplo: if dato == valor_buscado: contador += 1
    # Ejemplo: if dato % 2 == 0: paux.push(dato) 
    
    # Si quieres conservar el dato original, lo mandas a paux:
    # paux.push(dato)

# 4. Restauración (Fundamental para no perder los datos)
while paux.size() > 0:
    pila.push(paux.pop())

# 5. Salida de resultados
# print(f"Resultado: {resultado}")"""
class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:
        return self.__elements.pop()
    
    def show(self) -> None:
        stack_aux = Stack()
        stack_aux.__elements = copy(self.__elements)

        while stack_aux.size() > 0: 
            value = stack_aux.pop()
            print(value)
        
        # stack_aux = Stack()

        # while self.size() > 0: 
        #     value = self.pop()
        #     print(value)
        #     stack_aux.push(value)
        
        # while stack_aux.size() > 0: 
        #     value = stack_aux.pop()
        #     self.push(value)
        
    def size(self) -> int:
        return len(self.__elements)
    
    def on_top(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]


#1. Determinar el número de ocurrencias de un determinado elemento en una pila.

# pila = Stack()

# for i in range(randint(1,10)):
#     pila.push(randint(1,10))

# print("pila generada: ")
# pila.show()
# print()

# search_value = int(input("ingrese un valor para buscar en la pila: "))
# contador = 0
# paux = Stack()

# while pila.size() > 0:
#     value = pila.pop()
#     if value == search_value:
#         contador += 1
#     paux.push(value)

# while paux.size() > 0:
#     value = paux.pop()
#     pila.push(value)

# print(f'cantidad de veces que aparece {search_value} en la pila: {contador}')

#2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden nú-
# meros pares.

# pila = Stack()

# for i in range(10):
#     pila.push(randint(1,10))

# print("2. pila generada: ")
# pila.show()
# print()

# paux = Stack()

# while pila.size() > 0:
#     value = pila.pop()

#     if value % 2 == 0:
#         paux.push(value)

# while paux.size() > 0:
#     value = paux.pop()
#     pila.push(value)

# print("Pila resultado: ")
# pila.show()

#3. Reemplazar todas las ocurrencias de un determinado elemento en una pila.
# pila = Stack()

# for i in range(randint(6,10)):
#     pila.push(randint(1,10))

# print("III. pila generada: ")
# pila.show()
# print()

# valor_a_reemplazar = int(input('ingrese el valor a reemplazar: '))
# nuevo_valor = int(input('ingrese el nuevo valor: '))

# paux = Stack()

# while pila.size() >0:
#     value = pila.pop()

#     if value == valor_a_reemplazar:
#         paux.push(nuevo_valor)
#     else:
#         paux.push(value)

# while paux.size() > 0:
#     value = paux.pop()
#     pila.push(value)

# pila.show()

#4. Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.
# pila = Stack()

# for i in range(5):
#     pila.push(randint(1,10))

# print("IV. pila generada: ")
# pila.show()
# print()

# paux = Stack()
# n = pila.size()

# for i in range(n):
#     temp = pila.pop()
#     for j in range(n-1-i):
#         paux.push(pila.pop())
    
#     pila.push(temp)

#     while paux.size() > 0:
#         value = paux.pop()
#         pila.push(value)

# print("pila invertida: ")
# pila.show()

#5. Determinar si una cadena de caracteres es un palíndromo.
# def es_palindromo(cadena:str) -> bool:
#     pila = Stack()

#     cadena_limpia = cadena.lower().replace(" ","") # se limpia la cadena de mayusculas o minusculas y espacios

#     for letra in cadena_limpia: 
#         pila.push(letra) # se cargan las letras en la pila
    
#     for letra in cadena_limpia: 
#         if letra != pila.pop(): # se saca el ultimo elemento de la pila y se compara con la letra actual
#             return False # si la letra no es igual a la que se saca de la pila, no es palindromo
#     return True # si se recorre toda la cadena y no se encontro ninguna diferencia, es palindromo

# texto = input(str('ingrese una frase o palabra para verificar: '))
# if es_palindromo(texto):
#     print(f'{texto} es un palindromo')
# else:
#     print(f'{texto} no es un palindromo')

    
#6. Leer una palabra y visualizarla en forma inversa.
# def inversa_palabra(palabra:str) -> None:
#     pila = Stack()

#     for i in palabra: # se agregan las letras a la pila
#         pila.push(i)

#     palabra_inversa = "" # se inicializa la variable para guardar la palabra inversa

#     while pila.size() > 0: # mientras la pila no este vacia
#         palabra_inversa += pila.pop() # se saca el ultimo elemento de la pila y se agrega a la variable palabra_inversa

#     print(f'Palabra: {palabra}\n Palabra inversa: {palabra_inversa}')

# palabra_user = input(str("iingerse una palabra para invertir: "))
# inversa_palabra(palabra_user)


#7. Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.
# pila = Stack()

# for i in range(randint(1,10)):
#     pila.push(randint(1,10))

# pila.show()

# paux = Stack()
# contador = 1
# i_eliminar = int(input("Ingrese la posicion del elemento a eliminar: "))

# if i_eliminar > pila.size():
#     print("error! la pos es mayor al tamaño de la pila")
# else:
#     while pila.size() > 0:
#         value = pila.pop()

#         if contador == i_eliminar:
#             print(f'eliminando el elemento de la posicion {i_eliminar}')
#         else:
#             paux.push(value)

#         contador += 1

#     while paux.size() > 0:
#         value = paux.pop()
#         pila.push(value)

# pila.show()

#8. Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
# cartas de baraja española–,resolver las siguientes actividades:
# a. generar las cartas del mazo de forma aleatoria;
# b. separar la pila mazo en cuatro pilas una por cada palo;
# c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.

# pila_mazo = Stack()
# palos = ["espada","basto","copa","oro"]

# # a. generar las cartas del mazo de forma aleatoria;
# for i in range(20):
#     numero = randint(1,12)
#     palo = choice(palos)
#     pila_mazo.push((numero, palo))

# print("mazo generado: ")
# pila_mazo.show()

# #b. separar la pila mazo en cuatro pilas una por cada palo;
# pila_espada = Stack()
# pila_oro = Stack()
# pila_basto = Stack()
# pila_copa = Stack()

# while pila_mazo.size() > 0:
#     carta = pila_mazo.pop()
#     palo = carta[1]

#     if palo == "espada":
#         pila_espada.push(carta)
#     elif palo == "oro":
#         pila_oro.push(carta)
#     elif palo == "basto":
#         pila_basto.push(carta)
#     elif palo == "copa":
#         pila_copa.push(carta)

# #c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.

# paux = Stack()
# while pila_espada.size() > 0:
#     temporal = pila_espada.pop()
#     while paux.size() > 0 and paux.on_top()[0] < temporal[0]:
#         pila_espada.push(paux.pop())
#     paux.push(temporal)
# """
#     que es lo que hace? pero sencillo de enteder: 

#     toma el primer elemento de la pila espada y lo guarda en una variable temporal

#     despues pregunta, mientras la pila espada no este vacia y el tope de la pila auxiliar sea menor al temporal

#     entonces
#     saca el elemento de la pila auxiliar y lo agrega a la pila espada

#     despues agrega el temporal a la pila auxiliar

#     esto se hace hasta que la pila espada este vacia
#     luego se agrega el temporal a la pila auxiliar
# """

# while paux.size() > 0:
#     pila_espada.push(paux.pop())

# print("Mazo de espada ordenado: ")
# pila_espada.show()

#9. Resolver el problema del factorial de un número utilizando una pila.
# numero = int(input("Ingrese un numero: "))
# pila = Stack()

# for i in range(1, numero + 1):
#     pila.push(i)
# pila.show()

# resultado = 1
# paux = Stack()

# while pila.size() > 0:
#     value = pila.pop()
#     resultado *= value
#     paux.push(resultado)

# while paux.size() > 0:
#     value = paux.pop()
#     pila.push(value)

# print(f'el factorial de {numero} es: {resultado}')

# # ---- version corregida ----
# # 9. Resolver el factorial (Versión optimizada)
# numero = int(input("Ingrese un numero: "))
# pila = Stack()

# # 1. Carga
# for i in range(1, numero + 1):
#     pila.push(i)

# # 2. Cálculo (sin necesidad de pila auxiliar si no quieres restaurar)
# resultado = 1
# while pila.size() > 0:
#     resultado *= pila.pop()

# print(f'El factorial de {numero} es: {resultado}')


# 10. Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de una
# pila con nombres de dioses griegos.
# pila = Stack()
# dioses = ['Zeus','Hera','Poseidon','Apolo','Ares','Hades']

# for i in range(6):
#     pila.push(dioses[i])

# paux = Stack()
# i_pos = int(input("ingrese la posicion donde quiere insertar a atenea: "))
# contador = 1

# if i_pos > pila.size() + 1:
#     print("error! la posicion es muy grande. ")
# else: 
#     while pila.size() > 0:
#         value = pila.pop()
#         if contador == i_pos:
#             paux.push("Atenea")
        
#         paux.push(value)
#         contador += 1

#     while paux.size() > 0:
#         value = paux.pop()
#         pila.push(value)

# pila.show()

#11. Dada una pila de letras determinar cuántas vocales contiene.
# pila = Stack()
# vocales = ["a","e","i","o","u"]
# contador_vocales = 0

# for i in range(10):
#     pila.push(chr(ord("a") + randint(0,25)))

# pila.show()
# paux = Stack()

# while pila.size() > 0:
#     letra = pila.pop()

#     if letra in vocales:
#         contador_vocales +=1

#     paux.push(letra)

# while paux.size() > 0:
#     value = paux.pop()
#     pila.push(value)

# print(f'la cantidad de vocales que hay en esta pila son: {contador_vocales}')

#12. Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
# que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.
pila =Stack()
personajes = ["luke", "han", "chewbacca", "Obi-Wan", "Darth Vader", "Boba Fett", "Leia Organa"]

for i in personajes:
    pila.push(i)

pila.show()
paux = Stack()
leia_encontrada = False
boba_encontrado = False

while pila.size() > 0:
    value = pila.pop() # 

    if value == "Leia Organa":
        leia_encontrada = True
        
    if value == "Boba Fett":
        boba_encontrado = True
    paux.push(value) 

while paux.size() > 0:
    value = paux.pop()
    pila.push(value)

pila.show()
if leia_encontrada:
    print(f'Leia Organa se encuentra en la pila')
else:
    print(f'Leia Organa no se encuentra en la pila')

if boba_encontrado:
    print(f'Boba Fett se encuentra en la pila')
else:
    print(f'Boba Fett no se encuentra en la pila')


#13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
# verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
# las siguientes actividades:
# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
# además mostrar el nombre de dichas películas;
# b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
# c. eliminar los modelos de los trajes destruidos mostrando su nombre;
# d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
# más de un modelo de traje, estos deben cargarse por separado;
# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
# repetidos en una misma película;
# f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
# “Capitan America: Civil War”.

# pila = Stack()
# trajes_mcu = [
#     {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Destruido"},
#     {"modelo": "Mark XLIV (Hulkbuster)", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"},
#     {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"},
#     {"modelo": "Mark XLVI", "pelicula": "Capitan America: Civil War", "estado": "Dañado"},
#     {"modelo": "Mark XLIV (Hulkbuster)", "pelicula": "Avengers: Infinity War", "estado": "Destruido"}
# ]

# for t in trajes_mcu:
#     pila.push(t)

# paux= Stack()
# peliculas_hulkbuster = []
# Mark_LXXXV = {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Impecable"}
# mark_encontrado = False

# while pila.size() > 0:
#     traje = pila.pop()

#     if traje["modelo"] == "Mark XLIV (Hulkbuster)":
#         peliculas_hulkbuster.append(traje["pelicula"])

    
#     if traje["estado"] == "Dañado":
#         print(f'el modelo {traje["modelo"]} quedo dañado')

#     if traje["pelicula"] == "Spider-Man: Homecoming" or traje["pelicula"] == "Capitan America: Civil War":
#         print(f'{traje["modelo"]} se utilizo en la pelicula {traje["pelicula"]}')

#     if traje["modelo"] == Mark_LXXXV["modelo"] and traje["pelicula"] == Mark_LXXXV["pelicula"]:
#         mark_encontrado = True
    
#     if traje["estado"] == "Destruido":
#         print(f'El nombre es: {traje["modelo"]}')
#     else:
#         paux.push(traje)

    

# while paux.size() > 0:
#     value = paux.pop()
#     pila.push(value)

# print(f"El modelo Hulkbuster fue utilizado en las películas: {peliculas_hulkbuster}")
# if mark_encontrado == False:
#     pila.push(Mark_LXXXV)
#     print(f'se agrego el traje {Mark_LXXXV} a la pila')
# else:
#     print(f'no se agrego el traje a la pila porque ya existe')

# 14. Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden orde-
# nados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra –no se
# pueden utilizar métodos de ordenamiento–.
# pila = Stack()
# paux = Stack()
# for i in range(10):
#     numero = randint(0,10)
#     print(f'intentando agregar {numero}...')

#     while pila.size() > 0 and pila.on_top() < numero:
#         value = pila.pop()
#         paux.push(value)

#     paux.push(numero)

#     while paux.size() > 0:
#         value = paux.pop()
#         pila.push(value)
        
# pila.show()
    
# #15. Realizar el algoritmo de ordenamiento quicksort de manera que funcione iterativamente.
# def particion(lista: list, inicio: int, fin: int) -> tuple:
#     pivote = lista[fin]
#     i = inicio - 1
    
#     for j in range(inicio, fin):
#         if lista[j] <= pivote:
#             i += 1
#             lista[i], lista[j] = lista[j], lista[i]
    
#     lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
#     return i + 1

# def quicksort_iterativo(lista: list) -> None:
#     pila = Stack()
#     pila.push((0,len(lista)-1))

#     while pila.size() >0:
#         inicio, fin = pila.pop()

#         if inicio < fin:
#             indice_pivote = particion(lista, inicio, fin)

#             if indice_pivote - 1 > inicio:
#                 pila.push((inicio, indice_pivote - 1))
            
#             if indice_pivote + 1 < fin:
#                 pila.push((indice_pivote + 1, fin))

# numeros = [randint(1,100) for _ in range(15)]
# print(f'lista original: \n{numeros}\n')

# quicksort_iterativo(numeros)
# print(f'lista ordenada: \n{numeros}\n')


#16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
# bos episodios.

# Definimos las pilas
pila_V= Stack()
pila_VII= Stack()
paux_V= Stack()
paux_VII= Stack()

interseccion = Stack()
personajes_V = ["Luke Skywalker", "Han Solo", "Leia Organa", "Darth Vader", "Yoda", "Lando Calrissian"]
personajes_VII = ["Han Solo", "Leia Organa", "Luke Skywalker", "Chewbacca", "Rey", "Finn"]

for i in personajes_V:
    pila_V.push(i)

for i in personajes_VII:
    pila_VII.push(i)

while pila_V.size() > 0:
    personaje = pila_V.pop()
    encontrado = False

    while pila_VII.size() > 0:
        p_VII = pila_VII.pop()
        if personaje == p_VII:
            encontrado = True
        paux_VII.push(p_VII)

    while paux_VII.size() > 0:
        pila_VII.push(paux_VII.pop())

    if encontrado:
        interseccion.push(personaje)
    paux_V.push(personaje)

while paux_V.size() > 0:
    value = paux_V.pop()
    pila_V.push(value)

print("personajes en ambos episodios: ")
interseccion.show()
        

#17. Dado un párrafo que finaliza en punto, separar dicho párrafo en tres pilas: vocales, consonan-
# tes y otros caracteres que no sean letras (signos de puntuación números, espacios, etc.). Luego

# utilizando las operaciones de pila resolver las siguientes consignas:
# a. cantidad de caracteres que hay de cada tipo (vocales, consonantes y otros);
# b. cantidad de espacios en blanco;

# c. porcentaje que representan las vocales respecto de las consonantes sobre el total de carac-
# teres del párrafo;

# d. cantidad de números;
# e. determinar si la cantidad de vocales y otros caracteres son iguales;
# f. determinar si existe al menos una z en la pila de consonantes.
# 17. Clasificación de caracteres en pilas
# Definimos las pilas
p_vocales = Stack()
p_consonantes = Stack()
p_otros = Stack()

parrafo = "Hola, esto es una prueba con números 123 y letras."

# Clasificamos cada carácter
vocales = "aeiouAEIOU"
consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

for char in parrafo:
    if char in vocales:
        p_vocales.push(char)
    elif char in consonantes:
        p_consonantes.push(char)
    else:
        p_otros.push(char)

# Función para contar elementos de una pila sin perder los datos
def contar_elementos(pila):
    aux = Stack()
    contador = 0
    while pila.size() > 0:
        aux.push(pila.pop())
        contador += 1
    # Restauramos
    while aux.size() > 0:
        pila.push(aux.pop())
    return contador

# Función para contar un carácter específico en una pila sin perder los datos
def contar_caracter(pila, objetivo):
    aux = Stack()
    contador = 0
    while pila.size() > 0:
        char = pila.pop()
        if char == objetivo:
            contador += 1
        aux.push(char)
    while aux.size() > 0:
        pila.push(aux.pop())
    return contador

# a. Cantidad de cada tipo
cant_v = contar_elementos(p_vocales)
cant_c = contar_elementos(p_consonantes)
cant_o = contar_elementos(p_otros)
print(f"a. Cantidades: Vocales={cant_v}, Consonantes={cant_c}, Otros={cant_o}")

# b. Cantidad de espacios
print(f"b. Cantidad de espacios: {contar_caracter(p_otros, ' ')}")

# c. Porcentaje de vocales respecto de las consonantes sobre el total
total = cant_v + cant_c + cant_o
if (cant_v + cant_c) > 0:
    porcentaje = ((cant_v + cant_c) / total) * 100
    print(f"c. Porcentaje (Vocales+Consonantes) sobre total: {porcentaje:.2f}%")

# d. Cantidad de números
total_nums = 0
for i in "0123456789":
    total_nums += contar_caracter(p_otros, i)
print(f"d. Cantidad de números: {total_nums}")

# e. ¿Cantidad vocales == cantidad otros?
print(f"e. ¿Cantidad de vocales y otros son iguales?: {cant_v == cant_o}")

# f. ¿Existe al menos una 'z' en consonantes?
existe_z = contar_caracter(p_consonantes, 'z') > 0 or contar_caracter(p_consonantes, 'Z') > 0
print(f"f. ¿Existe al menos una 'z' en consonantes?: {existe_z}")



# 18. Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejem-
# plo monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso –del
# objeto más liviano al más pesado–. Solo pueden utilizar pilas auxiliares como estructuras ex-
# tras, no se pueden utilizar métodos de ordenamiento.
objeto = [{"nombre": "monitor", "peso": 1}, {"nombre": "teclado", "peso": 0.25}, {"nombre": "silla", "peso": 7}]
pila_original = Stack()
pila_ordenada = Stack()
paux = Stack()


for i in objeto:
    pila_original.push(i)

while pila_original.size() > 0:
    objeto_actual = pila_original.pop()

    while pila_ordenada.size() > 0 and pila_ordenada.on_top()["peso"] > objeto_actual["peso"]:
        objeto_aux = pila_ordenada.pop()
        paux.push(objeto_aux)
    pila_ordenada.push(objeto_actual)

    while paux.size() > 0:
        pila_ordenada.push(paux.pop())

pila_ordenada.show()


# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de es-
# treno, desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los nombre películas estrenadas en el año 2014;
# b. indicar cuántas películas se estrenaron en el año 2018;
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

peliculas = [{"titulo": "pelicula 1", "estudio": "estudio 1", "anio": 2014}, 
            {"titulo": "pelicula 2", "estudio": "estudio 2", "anio": 2018}, 
            {"titulo": "pelicula 3", "estudio": "Marvel Studios", "anio": 2016}]

pila_peliculas = Stack()
paux = Stack()


for i in peliculas:
    pila_peliculas.push(i)

contador_2018 = 0

while pila_peliculas.size() > 0:
    pelicula_actual = pila_peliculas.pop()

    if pelicula_actual['anio'] == 2014:
        print(f'Pelicula del 2014: {pelicula_actual['titulo']}')
    
    if pelicula_actual['anio'] == 2018:
        contador_2018 +=1

    if pelicula_actual['estudio'] == "Marvel Studios" and pelicula_actual['anio'] == 2016:
        print(f'Pelicula de Marvel Studios esrtenadas en 2016: {pelicula_actual['titulo']}')
    
    paux.push(pelicula_actual)

while paux.size() >0:
    value = paux.pop()
    pila_peliculas.push(value)

print(f'cantidad de peliculas estrenadas en 2018: {contador_2018}')

#20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.
pila_movimientos = Stack()
print('direcciones validas: \n 1. norte\n 2. sur\n 3. este\n 4. oeste\n 5. noreste\n 6. noroeste\n 7. sureste\n 8. suroeste')
opuestos = {
        "norte" : "sur",
        "sur" : "norte",
        "este" : "oeste",
        "oeste" : "este",
        "noreste" : "suroeste",
        "noroeste" : "sureste",
        "sureste" : "noroeste",
        "suroeste" : "noreste"
    }

while True:
    direccion = input('ingrese direccion (o presione S para finalizar): ').lower()

    if direccion == 's':
        break

    pasos = int(input("ingrese cantidad de pasos: "))

    pila_movimientos.push({"pasos": pasos, "direccion": direccion})
    print('movimiento registrado')
    
while pila_movimientos.size() > 0:
    mov_actual = pila_movimientos.pop()

    direccion_regreso = opuestos[mov_actual["direccion"]]
    pasos_regreso = mov_actual["pasos"]

    print(f'-> Mover {pasos_regreso} pasos hacia el {direccion_regreso}')

print("el robot llego a la base.")

# 22. Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The
# Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada
# misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó,
# costo de la recompensa. Resolver las siguientes actividades:
# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno
# de los cazzarrecompensas;
# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos
# quien obtuvo mayor fortuna;
# c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la
# que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

pila_boba = Stack()
pila_din = Stack()

misiones_boba = [
    {"planeta": "Kamino", "captura": "Nadie", "costo": 0},          # Fondo (Misión 1)
    {"planeta": "Tatooine", "captura": "Han Solo", "costo": 50000}, # Medio (Misión 2)
    {"planeta": "Geonosis", "captura": "Droide", "costo": 10000}    # Cima  (Misión 3)
]

misiones_din = [
    {"planeta": "Nevarro", "captura": "Mythrol", "costo": 5000},    # Fondo (Misión 1)
    {"planeta": "Arvala-7", "captura": "El Niño", "costo": 100000}, # Medio (Misión 2)
    {"planeta": "Tatooine", "captura": "Fennec", "costo": 20000}    # Cima  (Misión 3)
]

for m in misiones_boba:
    pila_boba.push(m)

for m in misiones_din:
    pila_din.push(m)

def procesar_bitacora(pila: Stack, nombre_cazador: str) -> tuple:
    paux =Stack()
    creditos_totales = 0
    capturas_totales = 0

    while pila.size() >0:
        mision = pila.pop()

        if mision['captura'].lower() != 'nadie':
            capturas_totales += 1
        creditos_totales += mision["costo"]

        paux.push(mision)

    print(f"bitacora de {nombre_cazador}:") 
    print("a. planetas visitados: ")
    nro_mision =1
    while paux.size() >0:
        mision = paux.pop()
        print(f"{nro_mision}. {mision['planeta']}")
        if mision["captura"] == "Han Solo":
            print(f'Han Solo fue capturado en la mision nro {nro_mision}')

        pila.push(mision)
        nro_mision += 1

    return creditos_totales, capturas_totales

creditos_boba, capturas_boba = procesar_bitacora(pila_boba, 'boba fett')
creditos_din, capturas_din = procesar_bitacora(pila_din, 'din djarin')

print(f'b. Creditos de boba fett: {creditos_boba}, capturas: {capturas_boba}')
print(f'b. Creditos de din djarin: {creditos_din}, capturas: {capturas_din}')

if creditos_boba > creditos_din:
    print('b. Boba fett obtuvo mayor fortuna')
else:
    print('b. Din djarin obtuvo mayor fortuna')
            

#23. Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril,
# obtener la siguiente información sin perder los datos:
# a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
# b. calcular el promedio de temperatura (o media) del total de valores;
# c. determinar la cantidad de valores por encima y por debajo de la media.

pila_temperaturas = Stack()
paux = Stack()

for _ in range(30):
    pila_temperaturas.push(random.randint(10, 35))

min_temp = float('inf')
max_temp = float('-inf')
suma_temp = 0
total_dias = 0

print("temperaturas del mes de abril:")

while pila_temperaturas.size() >0:
    temp = pila_temperaturas.pop()

    if temp < min_temp:
        min_temp = temp
    if temp > max_temp:
        max_temp = temp

    suma_temp += temp
    total_dias += 1

    paux.push(temp)

if total_dias > 0:
    promedio = suma_temp / total_dias
else:
    promedio = 0
    
dias_sobre_media = 0
dias_bajo_media = 0

while paux.size() >0:
    temp = paux.pop()

    if temp > promedio:
        dias_sobre_media += 1

    if temp < promedio:
        dias_bajo_media += 1

    pila_temperaturas.push(temp)

print("RESPUESTAS: ")
print( f' rango de temperatura es ({min_temp}, {max_temp})')
print(f'el promedio de temperatura del mes de abril es: {promedio:.2f} C°')

print(f' cantidad de dias con temperatura mayor a la media: {dias_sobre_media}')
print(f' cantidad de dias con temperatura menor a la media: {dias_bajo_media}')
    

#24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
# ción uno la cima de la pila;

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# car la cantidad de películas en la que aparece;

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

personajes = [{"nombre" : 'thor', "peliculas" : 9},
             {"nombre" : 'groot', "peliculas" : 5},
             {"nombre" : 'rocket racoon', "peliculas" : 6},
             {"nombre" : 'black widow', "peliculas" : 6},
             {"nombre" : 'captain america', "peliculas" : 7},
             {"nombre" : 'doctor strange', "peliculas" : 4},
             {"nombre" : 'gamora', "peliculas" : 6},
             {"nombre" : 'drax', "peliculas" : 5},
             {"nombre" : 'spiderman', "peliculas" : 7},
             ]

pila = Stack()
paux = Stack()

for i in personajes:
    pila.push(i)

posicion = 1 #porque es la posicion 1 desde la cima
pos_rocket = -1 #porque no lo encontre todavia
pos_groot = -1 # porque no lo encontre todavia
peliculas_negra = 0 # contador de peliculas viuda negra

while pila.size() > 0:
    personaje = pila.pop()

    #a. 
    if personaje["nombre"] == 'rocket racoon':
        pos_rocket = posicion
    elif personaje["nombre"] == 'groot':
        pos_groot = posicion

    #b. 
    if personaje["peliculas"] > 5:
        print(f' los personajes que participaron en mas de 5 peliculas son: {personaje["nombre"]} con {personaje["peliculas"]}')
 
    #c
    if personaje["nombre"] == 'black widow':
        peliculas_negra = personaje["peliculas"]
        

    #d
    inicial = personaje["nombre"][0].upper()
    if inicial in ['C', 'D', 'G']:
        print(f'los personajes cuyos nombres comienzan con C, D o G son: {personaje["nombre"]}')

    paux.push(personaje)
    posicion += 1

while paux.size() > 0:
    value = paux.pop()
    pila.push(value)

print("respuestas: ")
if pos_rocket != -1:
    print(f'rocket racoon se encuentra en la posicion {pos_rocket}')
else:
    print('rocket racoon no se encuentra en la pila')

if pos_groot != -1: 
    print(f'groot se encuentra en la posicion {pos_groot}')
else: print('groot no se encuentra en la pila')

if peliculas_negra > 0:
    print(f'la viuda negra participo en {peliculas_negra} peliculas')
else:
    print('la viuda negra no participo en ninguna pelicula')
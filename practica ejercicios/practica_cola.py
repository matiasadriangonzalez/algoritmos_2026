import sys
import os

# Le enseñamos a Python a mirar en la carpeta de arriba
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos tu clase con el nombre correcto
from queue_ import Queue
from stack import Stack
from random import randint
# ============================================================
# 2. PILA (Stack)
# ============================================================
# LIFO: Last In, First Out (el ultimo en entrar es el primero
# en salir). Como una pila de platos.
#
# Operaciones principales:
#   push(valor)  -> agrega en la cima
#   pop()        -> extrae de la cima
#   on_top()     -> consulta la cima sin sacarla
#   size()       -> cantidad de elementos
#   show()       -> muestra de cima a base


# ============================================================
# 3. COLA (Queue)
# ============================================================
# FIFO: First In, First Out (el primero en entrar es el primero
# en salir). Como una fila en el banco.
#
# Operaciones principales:
#   arrive(valor)   -> agrega al final
#   attention()     -> atiende (extrae) del frente
#   on_front()      -> consulta el frente sin extraerlo
#   move_to_end()   -> mueve el frente al final (rotar)
#   size()          -> cantidad de elementos
#   show()          -> muestra todos usando move_to_end

#1. Eliminar de una cola de caracteres todas las vocales que aparecen.

# queue_letras = Queue()

# vocales = ["a","e","i","o","u"]

# for i in range(6):
#     queue_letras.arrive(chr(randint(97, 122)))

# queue_letras.show()
# print()

# for i in range(queue_letras.size()):
#     if queue_letras.on_front() in vocales:
#         queue_letras.attention()
#     else: 
#         queue_letras.move_to_end()

# queue_letras.show()

#2. Utilizando operaciones de cola y pila, invertir el contenido de una cola. EJEMPLO BUENO DE PILA Y COLA <--
# queue_invertido = Queue()
# pila = Stack()
# for i in range(5): # Llenamos la cola con numeros aleatorios
#     queue_invertido.arrive(randint(1,10)) 

# queue_invertido.show() # Mostramos la cola original
# print() 

# # Vaciamos la cola en la pila (el primero de la cola queda en el fondo de la pila)
# for i in range(queue_invertido.size()): # Pasamos los elementos de la cola a la pila
#     pila.push(queue_invertido.attention()) # de esta manera la pila tiene los elementos invertidos

# # Devolvemos a la cola (el último en entrar a la pila es el primero en salir)
# while pila.size() > 0: # y ahora pasamos los elementos de la pila a la cola
#     queue_invertido.arrive(pila.pop()) # de esta manera la cola tiene los elementos invertidos

# queue_invertido.show() # Mostramos la cola invertida

#3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar si es un palíndromo.
# queue_caracteres = Queue()
# pila = Stack()

# texto = input(str("Ingrese una frase o palabra: "))
# cadena_limpia = texto.lower().replace(" ", "")

# for i in cadena_limpia:
#     queue_caracteres.arrive(i)
#     pila.push(i)

# es_palindromo = True

# while queue_caracteres.size() > 0:
#     if queue_caracteres.attention() != pila.pop():
#         es_palindromo = False
#         break

# if es_palindromo: 
#     print("es palindromo")
# else:
#     print("no es palindromo")

#4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
# queue = Queue()

# for i in range(10):
#     queue.arrive(randint(1,20))

# queue.show()
# print()

# for i in range(queue.size()):
#     value = queue.on_front()

#     es_primo = True
#     if value <= 1:
#         es_primo = False
#     else:
#         for j in range(2, value):
#             if value % j == 0:
#                 es_primo = False
#                 break

#     if es_primo:
#         queue.move_to_end()
#     else:
#         queue.attention()

# print("cola sin primos: ")
# queue.show()

#5. Utilizando operaciones de cola y pila, invertir el contenido de una pila.
# pila_invertida = Stack()
# cola = Queue()

# for i in range(10):
#     pila_invertida.push(randint(1,10))

# pila_invertida.show()
# print()

# #llevamos los elementos de la pila a la cola para que el orden se invierta
# for i in range(pila_invertida.size()):
#     cola.arrive(pila_invertida.pop())


# #volvimos a llevar los elementos de la cola a la pila para invertir el orden
# while cola.size() > 0:
#     pila_invertida.push(cola.attention())

# pila_invertida.show()

#6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ningu-
# na estructura auxiliar.

# queue = Queue()

# for i in range(10):
#     queue.arrive(randint(1,10))

# queue.show()
# print()


# search_value = int(input("ingrese un numero a buscar: "))
# contador = 0

# for i in range(queue.size()):
#     if queue.on_front() == search_value:
#         contador += 1
#     queue.move_to_end()

# print(f'la cantidad de ocurrencias de {search_value} es: {contador} veces')

#7. Eliminar el i-ésimo elemento después del frente de la cola.

# queue = Queue()

# for i in range(10):
#     queue.arrive(randint(1,10))
# queue.show()
# print()
# eliminar_value = int(input("ingrese un valor a eliminar:"))
# tamanio = queue.size() # guardamos el tamanio porque va a cambiar

# for i in range(tamanio): # recoremos el tamaño real de la cola
#     if i == eliminar_value: #si llegamos al valor a eliminar
#         queue.attention() #lo sacamos
#     else:
#         queue.move_to_end() # si no, lo movemos al final

# queue.show()

#8. Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando
# solo una cola como estructura auxiliar.
# queue = Queue()
# qaux = Queue()

# num = int(input("ingrese un numero: "))
# for i in range(10):
#     queue.arrive(randint(1,10))

# queue.show()
# print()

# cola_ordenada = Queue()

# # Mientras queden elementos en la cola desordenada
# while queue.size() > 0:
#     num = queue.attention()
    
#     # Insertamos num en la cola_ordenada usando la lógica que ya hiciste
#     qaux = Queue()
#     # Despejamos los menores
#     while cola_ordenada.size() > 0 and cola_ordenada.on_front() < num:
#         qaux.arrive(cola_ordenada.attention())
    
#     qaux.arrive(num) # Insertamos el nuevo
    
#     # Pasamos los mayores
#     while cola_ordenada.size() > 0:
#         qaux.arrive(cola_ordenada.attention())
        
#     # Restauramos la cola_ordenada
#     while qaux.size() > 0:
#         cola_ordenada.arrive(qaux.attention())

# queue = cola_ordenada
# queue.show()

#9. Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.
# queue = Queue()
# for i in range(10):
#     queue.arrive(randint(-10,10))

# queue.show()
# print()

# primer_elemento = queue.on_front()
# min = primer_elemento
# max = primer_elemento
# cont_negativos = 0

# for _ in range(queue.size()):
#     valor = queue.on_front()

#     if valor > max:
#         max = valor

#     if valor < min:
#         min = valor

#     if valor < 0:
#         cont_negativos += 1

#     queue.move_to_end()

# rango = max - min

# print(f' el rango es: {rango}')
# print(f'la cantidad de temperaturas negativas es: {cont_negativos}')
# print(f'la temperatura maxima es: {max} y la minima es: {min}')

#10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

notificacion = [{'hora': '10:00', 'app': 'Facebook', 'mensaje': 'nueva publicacion'}, 
{'hora': '11:00', 'app': 'Twitter', 'mensaje': 'nuevo tweet'}, 
{'hora': '11:42', 'app': 'Facebook', 'mensaje': 'hola'},
{'hora': '12:01', 'app': 'Facebook', 'mensaje': 'buenos dias'},
{'hora': '11:00', 'app': 'Twitter', 'mensaje': 'nuevo tweet'},
{'hora': '13:00', 'app': 'Twitter', 'mensaje': 'Python es lo mejor'},
{'hora': '14:00', 'app': 'Twitter', 'mensaje': 'Python es lo maximo'},
{'hora': '15:57', 'app': 'Twitter', 'mensaje': 'Python es genial'},
{'hora': '16:00', 'app': 'Facebook', 'mensaje': 'buenisimo'},
{'hora': '11:00', 'app': 'Instagram', 'mensaje': 'nuevo post'},
]

queue = Queue()
pila = Stack()

for i in notificacion:
    queue.arrive(i)

queue.show()
print()

#a. eliminar de la cola todas las notificaciones de facebook
def eliminar_facebook(queue: Queue):
    for _ in range(queue.size()):
        noti = queue.on_front()
        if noti["app"] == 'Facebook':
            queue.attention()
        else:
            queue.move_to_end()
    
    return queue

def mostrar_notificaciones_python(queue: Queue):
    for _ in range(queue.size()):
        noti = queue.on_front()
        if noti["app"] == 'Twitter' and 'Python' in noti["mensaje"]:
            print(noti)
        queue.move_to_end()

def rango_notifiaciones(queue: Queue):
    paux = Stack()
    contador = 0

    for _ in range(queue.size()):
        noti = queue.on_front()
        if '11:43' <= noti['hora'] <= '15:57':
            paux.push(queue.attention())
            contador +=1
        else:
            queue.move_to_end()
    
    print(f'hubo {contador} notificaciones entre las 11:43 y las 15:57')
    return contador
print("cola sin facebook:")
queue = eliminar_facebook(queue)
queue.show()
print()
print("notificaciones de twitter con python:")
mostrar_notificaciones_python(queue)
print()
print("rango de notificaciones:")
rango_notifiaciones(queue)
    
#22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos los datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

personajes = [{'personaje': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'}, 
{'personaje': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'}, 
{'personaje': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'}, 
{'personaje': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'}, 
{'personaje': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'}, 
{'personaje': 'Stephen Strange', 'superheroe': 'Doctor Strange', 'genero': 'M'}, 
{'personaje': 'Thor', 'superheroe': 'Thor', 'genero': 'M'}, 
{'personaje': 'Wanda Maximoff', 'superheroe': 'Scarlet Witch', 'genero': 'F'}, 
{'personaje': 'Tchalla', 'superheroe': 'Black Panther', 'genero': 'M'}, 
{'personaje': 'Peter Parker', 'superheroe': 'Spider-Man', 'genero': 'M'}, ]

queue = Queue()

for i in personajes:
    queue.arrive(i)

#a. determinar el nombre del personaje de la superhéroe Capitana Marvel
def nombre_capitana_marvel(queue: Queue) -> str:
    for _ in range(queue.size()):
        personaje = queue.on_front()

        if personaje['personaje'] == 'Carol Danvers':
            nombreCapitana = personaje['personaje']
        queue.move_to_end()

    return nombreCapitana

#b. mostrar los nombres de los superhéroes femeninos
def nombres_femeninos(queue: Queue) -> list:
    nombresFemeninos = []

    for _ in range(queue.size()):
        personaje = queue.on_front()

        if personaje['genero'] =='F':
            nombresFemeninos.append(personaje['personaje'])
        queue.move_to_end()
    
    return nombresFemeninos

#c mostrar los nombres de los personajes masculinos
def nombre_masculinos(queue: Queue) -> list:
    nombresMasculinos = []

    for _ in range(queue.size()):
        personaje = queue.on_front()
        if personaje['genero'] == 'M':
            nombresMasculinos.append(personaje['personaje'])
        queue.move_to_end()

    return nombresMasculinos

#d determinar el nombre del superhéroe del personaje Scott Lang
def nombre_scott(queue: Queue)-> str:
    nombre_de_scott = None
    for _ in range(queue.size()):
        personaje = queue.on_front()

        if personaje['personaje'] == 'Scott Lang':
            nombre_de_scott = personaje['superheroe']
        queue.move_to_end()

    return nombre_de_scott

#e mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
def nombre_empiezan_s(queue: Queue) -> list:
    nombresS = []

    for _ in range(queue.size()):
        personaje = queue.on_front()
        if personaje['personaje'][0] == 'S':
            nombresS.append(personaje)
        queue.move_to_end()
    
    return nombresS

#f determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de
# superhéroes.
def carol_danvers_existe(queue: Queue) -> str:
    for _ in range(queue.size()):
        personaje = queue.on_front()
        if personaje['personaje'] == 'Carol Danvers':
            nombreSuperheroe = personaje['superheroe']
        queue.move_to_end()
    return nombreSuperheroe

print(f'a. nombre de capitana marvel: {nombre_capitana_marvel(queue)}')
print(f'b. nombres de superhéroes femeninos: {nombres_femeninos(queue)}')
print(f'c. nombres de personajes masculinos: {nombre_masculinos(queue)}')
print(f'd. nombre del superheroe de scott lang: {nombre_scott(queue)}')
print(f'e. nombre de personajes que empiezan con s: {nombre_empiezan_s(queue)}')
print(f'f. nombre del superheroe de carol danvers: {carol_danvers_existe(queue)}')

        


        







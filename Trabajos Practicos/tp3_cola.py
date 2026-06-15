import sys
import os

# Le enseñamos a Python a mirar en la carpeta de arriba
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos tu clase con el nombre correcto
from queue_ import Queue
from stack import Stack
from random import randint

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
print()



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

        


        







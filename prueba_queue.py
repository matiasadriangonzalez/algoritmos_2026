from queue import Queue
from random import randint

# ejercicio 1
# queue_letters = Queue()
# vowels = ['a', 'e', 'i', 'o', 'u']


# for i in range(15):
#     queue_letters.arrive(chr(randint(97, 122)))

# queue_letters.show()
# print()

# for i in range(queue_letters.size()):
#     if queue_letters.on_front() in vowels:
#         queue_letters.attention()
#     else:
#         queue_letters.move_to_end()

#     # value = queue_letters.attention()
#     # if value not in vowels:
#     #     queue_letters.arrive(value)


# queue_letters.show()


#ejercicio 6
queue_numbers = Queue()

for i in range(20):
    queue_numbers.arrive(randint(0,20))

queue_numbers.show()
counter = 0
search_value = int(input('ingrese un numero para determinar la cantidad de ocurrencias: '))

for i in range(queue_numbers.size()):
    value = queue_numbers.on_front()
    if value == search_value:
        counter += 1
    queue_numbers.move_to_end() 

print(f'la cantidad de ocurrencias de {search_value} en la cola es {counter}')

#PODEMOS HACER TODOS MENOS LO QUE DIGA COLA DE PRIORIDAD COMO EL 16

# Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:
# 1. Listado ordenado de manera ascendente por nombre de los personajes.
# 2. Determinar en que posicion esta The Thing y Rocket Raccoon.
# 3. Listar todos los villanos de la lista.
# 4. Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
# 5. Listar los superheores que comienzan con  Bl, G, My, y W.
# 6. Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# 7. Listado de superheroes ordenados por fecha de aparación.
# 8. Modificar el nombre real de Ant Man a Scott Lang.
# 9. Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
# 10. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

from list_ import List
from queue_ import Queue
from super_heroes_data import superheroes

class superheroe:
    def __init__(self, name, alias, real_name, bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.bio = bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f'{self.name} - {self.alias} - {self.real_name} - {self.bio} - {self.first_appearance} - {self.is_villain}'

l = List()
for hero in superheroes:
    l.append(superheroe(hero['name'], hero['alias'], hero['real_name'], hero['short_bio'], hero['first_appearance'], hero['is_villain']))

l.show()
print(l.size())
print()
        
def by_name(item):
    return item.name

def by_real_name(item):
    return item.real_name if item.real_name is not None else ''

def by_first_appearance(item):
    return item.first_appearance

l.add_criterion('name', by_name)
l.add_criterion('real_name', by_real_name)
l.add_criterion('first_appearance', by_first_appearance)


print('1. Listado ordenado de manera ascendente por nombre de los personajes.')
l.sort_by_criterion('name')
l.show()
print()

print('2. Determinar en que posicion esta The Thing y Rocket Raccoon.')
thing = l.search('The Thing', 'name')
rocket = l.search('Rocket Raccoon', 'name')

if thing is not None:
    print(f'The Thing esta en la posicion {thing}')
else:
    print('The Thing no esta en la lista')

if rocket is not None:
    print(f'Rocket Raccoon esta en la posicion {rocket}')
else:
    print('Rocket Raccoon no esta en la lista')
print()


print('3. Listar todos los villanos de la lista.')
for hero in l:
    if hero.is_villain:
        print(hero)
print()

print('4. Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.')
villanos_q = Queue()
for hero in l:
    if hero.is_villain:
        villanos_q.arrive(hero)
villanos_q.show()
print()

print('Villanos que aparecieron antes de 1980:')
for i in range(villanos_q.size()):
    value = villanos_q.on_front()
    if value.first_appearance < 1980:
        print(value)
    villanos_q.move_to_end()
print()


print('5. Listar los superheores que comienzan con  Bl, G, My, y W.')
l.filter_start_with(('Bl', 'G', 'My', 'W'), 'name')
print()

print('6. Listado de personajes ordenado por nombre real de manera ascendente de los personajes.')
l.sort_by_criterion('real_name')
l.show()
print()

print('7. Listado de superheroes ordenados por fecha de aparación.')
l.sort_by_criterion('first_appearance')
for hero in l:
    if not hero.is_villain:
        print(f'{hero.name} - fecha aparicion: {hero.first_appearance}')
print()

print('8. Modificar el nombre real de Ant Man a Scott Lang.')
antman = l.search('Ant Man', 'name')
if antman is not None:
    l[antman].real_name = 'Scott Lang'
    print(l[antman])
print()


print('9. Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.')
l.filter_contain_on_bio(['time-traveling', 'suit'])
print()

print('10. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.')
deleted_electro = l.delete_value('Electro', 'name')
deleted_baron = l.delete_value('Baron Zemo', 'name')
l.show()
print()

print('Datos Eliminados:')
if deleted_electro is not None:
    print(f'Electro: {deleted_electro}')
else:
    print('Electro no esta en la lista')

if deleted_baron is not None:
    print(f'Baron Zemo: {deleted_baron}')
else:
    print('Baron Zemo no esta en la lista')
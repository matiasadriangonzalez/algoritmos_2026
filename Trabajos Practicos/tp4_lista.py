# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
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


from superheroes import superheroes
from list_ import List

class Superheroes:
    
    def __init__(self, nombre, anio_aparicion, casa_comic, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia

    def __str__(self):
        return (f'Nombre:    {self.nombre}\n'
                f'Aparicion: {self.anio_aparicion}\n'
                f'Casa:      {self.casa_comic}\n'
                f'Biografia: {self.biografia}\n')

def by_nombre(item):
    return item.nombre

def by_anio_aparicion(item):
    return item.anio_aparicion

def by_casa(item):
    return item.casa_comic



l = List() 
l.add_criterion('nombre', by_nombre)
l.add_criterion('anio_aparicion', by_anio_aparicion)
l.add_criterion('casa', by_casa)

for s in superheroes:
    l.append(Superheroes(s['nombre'], s['anio_aparicion'], s['casa'], s['biografia']))

# #a) eliminar el nodo que contiene la información de Linterna Verde;
print('eliminando a Linterna Verde')
deleted = l.delete_value("Linterna Verde", "nombre")
print(f'dato eliminado: {deleted}')
print()
#b) mostrar el año de aparición de Wolverine;
wolverine = l.search('Wolverine', 'nombre')
print(f'año de aparicion de wolverine: {l[wolverine].anio_aparicion}')
print()

# # c. cambiar la casa de Dr. Strange a Marvel;
dr_strange = l.search('Dr. Strange', 'nombre')

if dr_strange is not None:
        l[dr_strange].casa_comic = 'Marvel'

print(f'{l[dr_strange].nombre} es de la casa {l[dr_strange].casa_comic}')
print()

# # d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# # “traje” o “armadura”;
print('superheroes con traje o armadura')
l.filter_contain_on_bio(["traje", "armadura"])
print()

# #e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# # sea anterior a 1963;
print('Superheroes anteriores a 1963:')
for hero in l:
    if hero.anio_aparicion < 1963:
        print(f'SuperHeroe: {hero.nombre} - Casa: {hero.casa_comic} - Año: {hero.anio_aparicion}')
print()

# # f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
CapiMarvel = l.search('Capitana Marvel', 'nombre')
MujerMaravilla = l.search('Mujer Maravilla', 'nombre')

if CapiMarvel is not None and MujerMaravilla is not None:
    print(f'casa de capitana marvel: {l[CapiMarvel].casa_comic}')
    print(f'casa de mujer maravilla: {l[MujerMaravilla].casa_comic}')
else:
    print('no se encontro a capitana marvel o mujer maravilla')
print()

# # g. mostrar toda la información de Flash y Star-Lord;
flash = l.search('Flash', 'nombre')
starLoad = l.search('Star-Lord', 'nombre')
print('informacion de flash y star-lord: ')
print(f'{l[flash]}')
print(f'{l[starLoad]}')

# # h. listar los superhéroes que comienzan con la letra B, M y S;
# print('superheroes que comienzan con B, M y S:')
l.filter_start_with(('B', 'M', 'S'), 'nombre')
print()

# # i. determinar cuántos superhéroes hay de cada casa de comic.
print(f'Marvel: {l.count_by("casa", "Marvel")}')
print(f'DC: {l.count_by("casa", "DC")}')


# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;

from pokemon_entrenadores import entrenadores

class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = List()
    
    def porcentaje_ganado(self):
        total = self.batallas_ganadas + self.batallas_perdidas
        return self.batallas_ganadas / total * 100 if total else 0


    def __str__(self):
        return (f'Nombre: {self.nombre}\n'
                f'Torneos ganados: {self.torneos_ganados}\n'
                f'Batallas perdidas: {self.batallas_perdidas}\n'
                f'Batallas ganadas: {self.batallas_ganadas}\n')
    
class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return (f'Nombre: {self.nombre}\n'
                f'Nivel: {self.nivel}\n'
                f'Tipo: {self.tipo}\n'
                f'Subtipo: {self.subtipo}\n')

def by_nombre_entrenador(item):
    return item.nombre

def by_nombre_pokemon(item):
    return item.nombre

def by_torneos_ganados(item):
    return item.torneos_ganados

def by_nivel(item):
    return item.nivel


l_entrenadores = List()
l_entrenadores.add_criterion('nombre_entrenador', by_nombre_entrenador)
l_entrenadores.add_criterion('torneos_ganados', by_torneos_ganados)

for e in entrenadores:
    entrenador = Entrenador(e['nombre'], e['torneos_ganados'], e['batallas_perdidas'], e['batallas_ganadas'])
    entrenador.pokemons.add_criterion('nombre_pokemon', by_nombre_pokemon)
    entrenador.pokemons.add_criterion('nivel', by_nivel)

    for p in e['pokemons']:
        entrenador.pokemons.append(Pokemon(p['nombre'], p['nivel'], p['tipo'], p['subtipo']))

    l_entrenadores.append(entrenador)

#l_entrenadores.show()

# # a. obtener la cantidad de Pokémons de un determinado entrenador;
# buscar_entrenador = input('ingrese nombre del entrenador: ')
pos = l_entrenadores.search(buscar_entrenador, 'nombre_entrenador')

if pos is not None:
    print(f'cantidad de pokemon de {buscar_entrenador}: {l_entrenadores[pos].pokemons.size()}')
else:
    print(f'no se encontro al entrenador {buscar_entrenador}')
print()

# # b. listar los entrenadores que hayan ganado más de tres torneos;
for entrenador in l_entrenadores:
    if entrenador.torneos_ganados > 3:
        print(entrenador)
print()

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
l_entrenadores.sort_by_criterion('torneos_ganados')

l_entrenadores[-1].pokemons.sort_by_criterion('nivel')

print(f'el pokemon de mayor nivel del entrenador {l_entrenadores[-1].nombre} es {l_entrenadores[-1].pokemons[-1].nombre}')
print()

# d. mostrar todos los datos de un entrenador y sus Pokémos;
buscar_entrenador = input('ingrese nombre del entrenador: ')
pos = l_entrenadores.search(buscar_entrenador, 'nombre_entrenador')

if pos is not None:
    print(l_entrenadores[pos])
    print('- pokemons: ')
    l_entrenadores[pos].pokemons.show()
else:
    print(f'no se encontro al entrenador {buscar_entrenador}')
print()

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
for entrenador in l_entrenadores:
    if entrenador.porcentaje_ganado() > 79:
        print(entrenador)
print()

# # f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# # (tipo y subtipo);
for entrenador in l_entrenadores:
    for pokemon in entrenador.pokemons:
        if (pokemon.tipo == 'fuego' and pokemon.subtipo == 'planta') or (pokemon.tipo == 'agua' and pokemon.subtipo == 'volador'):
            print(entrenador)
            break
print()

# # g. el promedio de nivel de los Pokémons de un determinado entrenador;
buscar_entrenador = input('ingrese nombre del entrenador: ')
pos= l_entrenadores.search(buscar_entrenador, 'nombre_entrenador')

if pos is not None:
    suma = 0
    for pokemon in l_entrenadores[pos].pokemons:
        suma += pokemon.nivel
    p = suma / l_entrenadores[pos].pokemons.size()
    print(f'promedio de nivel de los pokemons de {buscar_entrenador}: {p:2.2f}')
else:
    print(f'no se encontro al entrenador {buscar_entrenador}')
print()
    
# # h. determinar cuántos entrenadores tienen a un determinado Pokémon;
buscar_pokemon = input('ingrese nombre del pokemon: ')
cont= 0

for entrenador in l_entrenadores:
    pos = entrenador.pokemons.search(buscar_pokemon, 'nombre_pokemon')
    if pos is not None:
        cont += 1

print(f'cantidad de entrenadores con {buscar_pokemon}: {cont}')
print()

# # i. mostrar los entrenadores que tienen Pokémons repetidos;
for entrenador in l_entrenadores:
    entrenador.pokemons.sort_by_criterion('nombre_pokemon')
    for i in range(entrenador.pokemons.size() - 1):
        if entrenador.pokemons[i].nombre == entrenador.pokemons[i+1].nombre:
            print(entrenador)
            break
print()

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;
for entrenador in l_entrenadores:
    for pokemon in entrenador.pokemons:
        if pokemon.nombre == 'Tyrantrum' or pokemon.nombre == 'Terrakion' or pokemon.nombre == 'Wingull':
            print(entrenador)
            break
print()

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
nombre_entrenador = input('ingrese nombre del entrenador: ')
nombre_pokemon = input('ingrese nombre del pokemon: ')

pos_entrenador = l_entrenadores.search(nombre_entrenador, 'nombre_entrenador')

if pos_entrenador is not None:
    pos_pokemon = l_entrenadores[pos_entrenador].pokemons.search(nombre_pokemon, 'nombre_pokemon')
    if pos_pokemon is not None:
        print(l_entrenadores[pos_entrenador])
        print(l_entrenadores[pos_entrenador].pokemons[pos_pokemon])
    else:
        print(f'el entrenador {nombre_entrenador} no tiene al pokemon {nombre_pokemon}')
else:
    print(f'no se encontro al entrenador {nombre_entrenador}')


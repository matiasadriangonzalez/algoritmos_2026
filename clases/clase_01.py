
print("hola mundo", "desde python")

# name = input('ingrese su nombre: ')
# print("su nombre es:", name)

# TIPOS DE DATOS PRIMITIVOS STR, INT, FLOAT, BOOL, NONE

variable = "Ana"
print(type(variable))
variable = 1234
print(type(variable))
variable = 12.5
print(type(variable))
variable = True
print(type(variable))
variable = None
print(type(variable))

# number = int(input('ingrese un numero: '))
# print(number + 100)

# funciones de conversion int, str, flot, boolinput('ingrese un numero: ')

# funciones aritmeticas +, -, *, /, //, %, **
# print(5 + 2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(5 ** 2)

# asignacion = -->  a = 10

# secuencial
# condicional
# if-else | case
# operadores de control >, <, >=, <=, ==, != 
num = 5
if num > 5:
    print('es mayor')

    print('dentro del if')
print('fuera del if')

if num > 5:
    print('es mayor')
elif num < 5:
    print('es menor')
else:
    print('es 5')

control = True
if not control:
    print('se cumple el control')

# operadores logicos and or not ^
if num >= 5 and num <= 10:
    print('el numero esta entre 5 y 10')

num = 4
match num:

    case 1: print('es uno')
    case 5: print('5')

    case _: print('otro')


# ciclo
#     for | while
# num = 1
# while num < 5:
#     print(num)
#     num += 1 # num = num + 1

nums = [1, 2, 3, 4, 5]
nums.append(100)
# for i in range(len(nums)-1, 0, -1):
#     print(nums[i])
# for i in range(len(nums)):
#     print(nums[i])
# for index, elemento in enumerate(nums):
#     print('posicion:', index, 'valore:', elemento)
nums.reverse()
for num in nums:
    print(num)


# estruturas de datos list, dic, tuple


# num_list = [None] * 10
num_list =[]

print(type(num_list))
print(len(num_list))

num_list.append(1)
num_list.append(3)
num_list.append(7)
num_list.append(3)

# num_list.clear()
# print(num_list)
# print(num_list.count(9))
# # print(num_list.index(9))
# num_list.insert(21, 9)
# print(num_list)

# # print(num_list.pop(15))
# # print(num_list.remove(2))
# num_list.sort(reverse=True)
# num_list[4] = 100
# print(num_list)
# print(num_list[4])


# funciones y modulo
# var_global = 45

# def mi_funcion(num1, num2, otro = 'hola mundo', nuevo='otro valor'):
#     var_global = 123
#     print(otro)
#     print(nuevo)
#     print(var_global)
#     return num1 + num2, num1 - num2

# num1 = 5
# num2 = 3
# lista_nums = [1, 2, 3, 4]
# suma, diferencia = mi_funcion(num1, num2, nuevo='pepito')
# print(suma, diferencia)
# print(var_global)

# import
# import math

# from math import sqrt, factorial
from math import sqrt as raiz_cuadrada, factorial

from mi_modulo import suma, diferencia

print(raiz_cuadrada(16))
print(suma(1, 3))
print(factorial(5))


# diccionarios clave -> valor.   
dic = {32: "juan", 45: "ana", 12: "pepe"}
print(type(dic))

print(dic.get(32)) # devuelve el valor asociado a la clave 32, si la clave no existe devuelve None

print(dic.keys()) # devuelve una lista con las claves del diccionario
print(dic.values()) # devuelve una lista con los valores del diccionario
print(dic.items()) # devuelve una lista de tuplas con las claves y valores del diccionario


dic[99] = "nuevo valor" # agrega un nuevo par clave-valor al diccionario
dic[45] = "nuevo valor" # actualiza el valor asociado a la clave 45

dic.pop(12) # elimina el par clave-valor asociado a la clave 12

print(dic)


# CLASES: son moldes para crear objetos, los objetos son instancias de las clases
class MiClase:

    def __init__(self, name: str, size: int = None): # __init__ es el constructor de la clase, es decir, es la funcion que se llama cuando se crea una instancia de la clase
        self.__name = name # __name es un atributo privado de la clase MiClase, es decir, es un atributo que solo se puede acceder desde la clase MiClase
        self.__size = size
    
    def saludar(self): # self (convecion del lenguaje) es una referencia a la instancia de la clase, es decir, a si mismo. tiene que estar siempre pero nunca se pasa, se pasa automaticamente lo llamma el interprete.
        print("hola", self.__name)    

    def get_name(self):
        return self.__name

    def set_name(self, new_name: str):
        self.__name = new_name



f_1 = MiClase("juan", 10)
f_2 = MiClase("ana", 20)
f_3 = MiClase("pepe")

f_1.set_name("matias")


print(f_1.get_name())
f_1.saludar()
f_2.saludar()


f = MiClase() # f es una instancia de la clase MiClase
f.name = "juan"
f.size = 10
print(f.name, f.size)
f.saludar() # se llama al metodo saludar de la instancia f

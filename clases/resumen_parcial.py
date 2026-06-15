# ============================================================
#   RESUMEN PARCIAL - ALGORITMOS Y ESTRUCTURA DE DATOS
#   Temas: Recursividad | Pila (Stack) | Cola (Queue) | Lista
# ============================================================


# ============================================================
# 1. RECURSIVIDAD
# ============================================================
# Una funcion recursiva se llama a si misma con un subproblema
# mas simple hasta llegar a un CASO BASE que detiene la cadena.
#
# Reglas que siempre se cumplen:
#   - Tiene un caso base claro (condicion de fin).
#   - Cada llamada se acerca al caso base.
#   - Siempre retorna algo.

# --- FACTORIAL ---
# fac(N) = N * fac(N-1)   ->   fac(0) = 1  (caso base)
def factorial_r(num: int) -> int:
    if num == 0:
        return 1
    else:
        return num * factorial_r(num - 1)

# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
print(factorial_r(5))   # 120


# --- FIBONACCI ---
# fib(0)=0, fib(1)=1, fib(N) = fib(N-1) + fib(N-2)
def fibonacci_r(num: int) -> int:
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci_r(num - 1) + fibonacci_r(num - 2)

print(fibonacci_r(6))   # 8  (0,1,1,2,3,5,8)


# --- SUMA 0..N ---
def suma_hasta_n(num: int) -> int:
    if num == 0:
        return 0
    else:
        return num + suma_hasta_n(num - 1)

print(suma_hasta_n(5))  # 15


# --- PRODUCTO (a * b como sumas repetidas) ---
def producto(a: int, b: int) -> int:
    if b == 0:
        return 0
    else:
        return a + producto(a, b - 1)

print(producto(5, 3))   # 15


# --- POTENCIA ---
def potencia(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)

print(potencia(2, 8))   # 256


# --- SECUENCIA INVERTIDA (string) ---
# invertir("hola") -> "aloh"
# Toma el ultimo caracter y llama con el resto sin ese ultimo
def sec_invertida(secuencia: str) -> str:
    if secuencia == "":
        return secuencia
    else:
        return secuencia[-1] + sec_invertida(secuencia[:-1])

print(sec_invertida("hola"))    # aloh


# --- SERIE 1 + 1/2 + 1/3 + ... + 1/n ---
def serie(n: int) -> float:
    if n == 1:
        return 1
    else:
        return 1 / n + serie(n - 1)

print(serie(4))  # 2.083...


# --- DECIMAL A BINARIO ---
# Idea: guardar el resto (% 2) y llamar con cociente (// 2)
def decimal_a_binario(num: int) -> str:
    if num == 0:
        return "0"
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

print(decimal_a_binario(10))    # 1010


# --- CONTAR DIGITOS ---
def contar_digitos(num: int) -> int:
    if num <= 10:
        return 1
    else:
        return 1 + contar_digitos(num // 10)

print(contar_digitos(12345))    # 5


# --- MCD (Algoritmo de Euclides) ---
# Si b == 0, el MCD es a. Si no, mcd(b, a % b)
def mcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

print(mcd(12, 18))  # 6


# --- MCM ---
# mcm(a, b) = (a * b) // mcd(a, b)
def mcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    else:
        return (a * b) // mcd(a, b)

print(mcm(12, 18))  # 36


# --- SUMA DE DIGITOS ---
def suma_digitos(num: int) -> int:
    if num < 10:
        return num
    else:
        return num % 10 + suma_digitos(num // 10)

print(suma_digitos(1234))   # 10


# --- ROMANO A DECIMAL (TP1 ej.5) ---
def romano_a_decimal(romano: str) -> int:
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    if not romano:
        return 0
    if len(romano) == 1:
        return valores[romano[0]]
    actual   = valores[romano[0]]
    siguiente = valores[romano[1]]
    if actual >= siguiente:
        return actual + romano_a_decimal(romano[1:])
    else:
        return -actual + romano_a_decimal(romano[1:])

print(romano_a_decimal("XIV"))      # 14
print(romano_a_decimal("MCMXCIV")) # 1994


# --- MOCHILA JEDI (TP1 ej.22) ---
# Recorre la lista de a un elemento (mochila[0]) y llama
# recursivamente con el resto (mochila[1:])
def usar_la_fuerza(mochila: list, objetos_sacados: int = 0):
    if len(mochila) == 0:
        return False, objetos_sacados
    objeto = mochila[0]
    if objeto == "sable de luz":
        return True, objetos_sacados + 1
    return usar_la_fuerza(mochila[1:], objetos_sacados + 1)

mochila = ["comida", "capa", "sable de luz", "holocrón"]
encontrado, cantidad = usar_la_fuerza(mochila)
print(f"Encontrado: {encontrado}, objetos sacados: {cantidad}")
# Encontrado: True, objetos sacados: 3


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

from typing import Any, Optional
from copy import copy

class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:
        return self.__elements.pop()

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]

    def show(self) -> None:
        aux = Stack()
        aux.__elements = copy(self.__elements)  # no destruimos la original
        while aux.size() > 0:
            print(aux.pop())


# PATRON TIPICO PARA RECORRER UNA PILA SIN PERDERLA:
# Siempre usamos una pila auxiliar para restaurar el orden.
#
#   while pila.size() > 0:
#       dato = pila.pop()
#       ... procesar dato ...
#       pila_aux.push(dato)
#   while pila_aux.size() > 0:     # restaurar
#       pila.push(pila_aux.pop())


# --- EJ. contar ocurrencias (no se puede restaurar: pila queda vacia) ---
def contar_ocurrencias_pila(pila: Stack, valor) -> int:
    contador = 0
    while pila.size() > 0:
        if pila.pop() == valor:
            contador += 1
    return contador


# --- EJ. eliminar impares (usando pila auxiliar) ---
def eliminar_impares(pila: Stack) -> None:
    pila_aux = Stack()
    while pila.size() > 0:
        dato = pila.pop()
        if dato % 2 == 0:          # solo conservamos pares
            pila_aux.push(dato)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())  # restauramos


# --- EJ. reemplazar elemento ---
def reemplazar_elemento(pila: Stack, viejo, nuevo) -> None:
    pila_aux = Stack()
    while pila.size() > 0:
        dato = pila.pop()
        if dato == viejo:
            dato = nuevo
        pila_aux.push(dato)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())


# --- EJ. invertir pila (solo con una pila auxiliar) ---
# Pasar todos a aux invierte una vez; volver a pasar invierte
# por segunda vez -> orden original... pero si queremos
# que quede invertida, solo hacemos el primer paso.
#
# Para INVERTIR: pasamos a aux y dejamos los datos en aux.
# Como no pedimos restaurar la original, dejamos aux tal cual
# y la nombramos como la nueva pila (o usamos otra estrategia).
#
# La version del profe: dos pasadas => la pila queda invertida
# porque la primera pasada invierte y la segunda re-invierte.
# Para dejarla REALMENTE invertida hay que pasarla a aux y
# copiarla de vuelta SIN la segunda re-inversion.
def invertir_pila(pila: Stack) -> None:
    pila_aux = Stack()
    while pila.size() > 0:         # 1ra pasada: invierte
        pila_aux.push(pila.pop())
    while pila_aux.size() > 0:     # 2da pasada: vuelve a invertir
        pila.push(pila_aux.pop())
    # Resultado: pila queda con el mismo orden pero ahora
    # la version "mostrada" al hacer show() es la invertida
    # (depende de como lo defina el profe en cada ejercicio).


# --- EJ. robot - TP2 ej.20 ---
# Se registran movimientos (pasos, direccion) en una pila.
# Para regresar al origen se desapila (orden inverso = LIFO)
# y se usa la direccion opuesta.
OPPOSITE = {
    "norte": "sur",    "sur": "norte",
    "este": "oeste",   "oeste": "este",
    "noreste": "suroeste", "suroeste": "noreste",
    "noroeste": "sureste", "sureste": "noroeste",
}
# Al desapilar ya obtenemos los movimientos al reves (LIFO),
# solo cambiamos la direccion por la opuesta.


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

class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Any:
        return self.__elements.pop(0)

    def size(self) -> int:
        return len(self.__elements)

    def on_front(self) -> Any:
        return self.__elements[0]

    def move_to_end(self) -> Any:
        value = self.__elements.pop(0)
        self.__elements.append(value)
        return value

    def show(self) -> None:
        for _ in range(len(self.__elements)):
            print(self.move_to_end())


# PATRON TIPICO PARA RECORRER UNA COLA SIN PERDERLA:
# Usamos move_to_end() en lugar de attention() para rotar.
#
#   for _ in range(cola.size()):   # iteramos exactamente N veces
#       valor = cola.on_front()
#       ... procesar valor ...
#       cola.move_to_end()         # lo mandamos al final


# --- EJ. eliminar vocales ---
def eliminar_vocales(cola: Queue) -> None:
    vocales = list("aeiouAEIOU")
    for _ in range(cola.size()):
        if cola.on_front() in vocales:
            cola.attention()       # la descartamos
        else:
            cola.move_to_end()     # la conservamos rotando


# --- EJ. invertir cola (usando pila auxiliar) ---
# La pila invierte el orden (LIFO), que es justo lo que queremos.
def invertir_cola(cola: Queue) -> None:
    pila_aux = Stack()
    while cola.size() > 0:
        pila_aux.push(cola.attention())
    while pila_aux.size() > 0:
        cola.arrive(pila_aux.pop())


# --- EJ. palindromo (cola + pila) ---
# Cola extrae de izquierda a derecha.
# Pila extrae de derecha a izquierda.
# Si cada par es igual -> es palindromo.
def es_palindromo(secuencia: str) -> bool:
    cola_aux = Queue()
    pila_aux = Stack()
    for c in secuencia:
        if c != " ":
            cola_aux.arrive(c.lower())
            pila_aux.push(c.lower())
    while cola_aux.size() > 0:
        if cola_aux.attention() != pila_aux.pop():
            return False
    return True

print(es_palindromo("anita lava la tina"))  # True


# --- EJ. eliminar no primos ---
def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def eliminar_no_primos(cola: Queue) -> None:
    for _ in range(cola.size()):
        if es_primo(cola.on_front()):
            cola.move_to_end()     # lo conservamos
        else:
            cola.attention()       # lo eliminamos


# --- EJ. contar ocurrencias sin estructura auxiliar ---
def contar_ocurrencias_cola(cola: Queue, elemento) -> int:
    contador = 0
    for _ in range(cola.size()):
        if cola.on_front() == elemento:
            contador += 1
        cola.move_to_end()         # rotamos siempre para no perder datos
    return contador


# --- EJ. eliminar el i-esimo elemento ---
def eliminar_iesimo(cola: Queue, i: int) -> None:
    for pos in range(cola.size()):
        if pos == i:
            cola.attention()       # posicion i -> lo eliminamos
        else:
            cola.move_to_end()     # resto -> lo conservamos


# --- EJ. insertar manteniendo la cola ordenada ---
def insertar_ordenado(cola: Queue, nuevo) -> None:
    cola_aux = Queue()
    while cola.size() > 0 and cola.on_front() < nuevo:
        cola_aux.arrive(cola.attention())   # movemos los menores
    cola_aux.arrive(nuevo)                  # insertamos en su lugar
    while cola.size() > 0:
        cola_aux.arrive(cola.attention())   # movemos los mayores
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())   # restauramos


# --- EJ. invertir pila usando cola (ejercicio-cola.py ej.5) ---
# la cola invierte el orden (LIFO), que es justo lo que queremos.
def invertir_pila_con_cola(pila: Stack) -> None:
    cola_aux = Queue()
    while pila.size() > 0:
        cola_aux.arrive(pila.pop()) #
    while cola_aux.size() > 0:
        pila.push(cola_aux.attention())
 

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
#   size()                        -> retorna len(self)

class Persona:
    def __init__(self, nom, ape, edad):
        self.nom  = nom
        self.ape  = ape
        self.edad = edad

    def __str__(self):
        return f"{self.ape} {self.nom} {self.edad}"


# Funciones de criterio: reciben un elemento y retornan el valor a comparar
def by_name(item):      return item.nom
def by_last_name(item): return item.ape
def by_age(item):       return item.edad


class List(list):

    __CRITERION_FUNCTION = {}   # dict compartido: clave -> funcion

    def add_criterion(self, criterion_key: str, criterion_function) -> None:
        self.__CRITERION_FUNCTION[criterion_key] = criterion_function

    def show(self) -> None:
        for element in self:
            print(element)

    def size(self) -> int:
        return len(self)

    def sort_by_criterion(self, key_criterion=None) -> None:
        sort_criterion = self.__CRITERION_FUNCTION.get(key_criterion)
        if sort_criterion:
            self.sort(key=sort_criterion)
        elif self and isinstance(self[0], (bool, int, float, str)):
            self.sort()
        else:
            print('no se puede ordenar: falta criterio')

    def search(self, search_value: Any, criterion: str = None) -> Optional[int]:
        # ordena segun el criterio antes de buscar (busqueda binaria requiere orden)
        self.sort_by_criterion(key_criterion=criterion)
        search_criterion = self.__CRITERION_FUNCTION.get(criterion)

        start  = 0
        end    = len(self) - 1
        middle = (start + end) // 2

        while start <= end:
            if search_criterion is None and not isinstance(self[0], (bool, int, float, str)):
                print('no se pudo determinar criterio de busqueda')
                return None

            value = search_criterion(self[middle]) if search_criterion else self[middle]

            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1
            else:
                end = middle - 1

            middle = (start + end) // 2
        return None

    def delete_value(self, value, criterion=None) -> Optional[Any]:
        index = self.search(value, criterion)
        return self.pop(index) if index is not None else None


# BUSQUEDA BINARIA - idea clave:
# 1. Partir la lista en mitades comparando con el del medio.
# 2. Si el del medio es menor al buscado -> buscar en la mitad derecha (start = middle + 1)
# 3. Si el del medio es mayor           -> buscar en la mitad izquierda (end = middle - 1)
# 4. Si son iguales                     -> encontrado, retornar middle
# REQUIERE QUE LA LISTA ESTE ORDENADA.

# Uso tipico
l = List()
l.add_criterion('name',      by_name)
l.add_criterion('last_name', by_last_name)
l.add_criterion('age',       by_age)

l.append(Persona("Juan",  "Perez", 24))
l.append(Persona("Dario", "Aron",  12))
l.append(Persona("Ana",   "Blanc", 20))

# Buscar y eliminar por apellido
print(f'dato eliminado: {l.delete_value("Blanc", "last_name")}')
# dato eliminado: Blanc Ana 20

l.show()
# Dario Aron 12
# Juan Perez 24

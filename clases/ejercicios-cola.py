from queue import Queue
from stack import Stack

# 1. Eliminar de una cola de caracteres todas las vocales que aparecen.
def eliminar_vocales(cola: Queue):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    # Iteramos exactamente la cantidad de elementos que tiene la cola
    for _ in range(cola.size()):
        if cola.on_front() in vocales:
            cola.attention() # La eliminamos
        else:
            cola.move_to_end() # La conservamos y la enviamos al final

# 2. Utilizando operaciones de cola y pila, invertir el contenido de una cola.
def invertir_cola(cola: Queue):
    pila_aux = Stack()
    
    # Pasamos todo de la cola a la pila
    while cola.size() > 0:
        pila_aux.push(cola.attention())
        
    # Devolvemos los elementos a la cola (saldrán invertidos)
    while pila_aux.size() > 0:
        cola.arrive(pila_aux.pop())


# 3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar si es un palíndromo.
def es_palindromo(secuencia: str) -> bool:
    cola_aux = Queue()
    pila_aux = Stack()
    
    # Cargamos la secuencia ignorando los espacios vacíos
    for caracter in secuencia:
        if caracter != ' ': 
            cola_aux.arrive(caracter.lower())
            pila_aux.push(caracter.lower())
            
    # Comparamos extrayendo de ambas estructuras
    palindromo = True
    while cola_aux.size() > 0 and palindromo:
        if cola_aux.attention() != pila_aux.pop():
            palindromo = False
            
    return palindromo

# 4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.

def es_primo(numero: int) -> bool:
    """Determina si un número entero positivo es primo o no."""
    if numero <= 1:
        return False
    cont = 0
    for i in range(2, numero + 1):
        if numero % i == 0:
            cont += 1
    if cont == 1:
        return True
    else:
        return False # [1]

def eliminar_no_primos(cola: Queue):
    for _ in range(cola.size()):
        if es_primo(cola.on_front()):
            cola.move_to_end() # Es primo, lo conservamos
        else:
            cola.attention()   # No es primo, lo eliminamos


# 5. Utilizando operaciones de cola y pila, invertir el contenido de una pila.
def invertir_pila(pila: Stack):
    cola_aux = Queue()
    
    # Vaciamos la pila en la cola
    while pila.size() > 0:
        cola_aux.arrive(pila.pop())
        
    # Devolvemos los elementos a la pila original
    while cola_aux.size() > 0:
        pila.push(cola_aux.attention())

# 6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar.
def contar_ocurrencias(cola: Queue, elemento_buscado) -> int:
    contador = 0
    
    for _ in range(cola.size()):
        # Si el elemento en el frente es el que buscamos, sumamos 1
        if cola.on_front() == elemento_buscado:
            contador += 1
        
        # Siempre lo enviamos al final para mantener la cola intacta
        cola.move_to_end()
        
    return contador

# 7. Eliminar el i-ésimo elemento después del frente de la cola.
def eliminar_iesimo(cola: Queue, i: int):
    # Verificamos que la posición sea válida
    if i < 0 or i >= cola.size():
        print("Índice fuera de rango")
        return
        
    for pos in range(cola.size()):
        if pos == i:
            cola.attention() # Es la posición i, lo eliminamos
        else:
            cola.move_to_end() # No es la posición, lo conservamos

# 8. Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando solo una cola como estructura auxiliar.
def insertar_ordenado(cola: Queue, elemento_nuevo):
    cola_aux = Queue()
    
    # Pasamos a cola_aux todos los elementos que sean menores al nuevo
    while cola.size() > 0 and cola.on_front() < elemento_nuevo:
        cola_aux.arrive(cola.attention())
        
    # Insertamos el nuevo elemento en su posición ordenada
    cola_aux.arrive(elemento_nuevo)
    
    # Pasamos a cola_aux el resto de los elementos (mayores o iguales)
    while cola.size() > 0:
        cola_aux.arrive(cola.attention())
        
    # Restauramos la cola original
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())

# 9. Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.
def rango_y_negativos(cola: Queue):
    if cola.size() == 0:
        return 0, 0 # Manejo de seguridad si la cola está vacía
        
    # Inicializamos con el primer elemento
    minimo = cola.on_front()
    maximo = cola.on_front()
    negativos = 0
    
    for _ in range(cola.size()):
        valor = cola.on_front()
        
        # Chequeos de extremos y negatividad
        if valor < minimo:
            minimo = valor
        if valor > maximo:
            maximo = valor
        if valor < 0:
            negativos += 1
            
        cola.move_to_end()
        
    rango = maximo - minimo
    return rango, negativos

# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

def procesar_notificaciones(cola: Queue):
    pila_temporales = Stack()
    
    # Recorremos la cola según su tamaño inicial
    for _ in range(cola.size()):
        notificacion = cola.on_front()
        
        # a. Eliminar las de Facebook
        if notificacion['app'] == 'Facebook':
            cola.attention()
            continue # Avanzamos al siguiente ciclo sin enviarla al final de la cola
            
        # b. Mostrar las de Twitter con la palabra 'Python' sin perder datos
        if notificacion['app'] == 'Twitter' and 'Python' in notificacion['mensaje']:
            print(f"Twitter ({notificacion['hora']}): {notificacion['mensaje']}")
            
        # c. Guardar en pila las que están entre 11:43 y 15:57
        if "11:43" <= notificacion['hora'] <= "15:57":
            pila_temporales.push(notificacion)
            
        # Retornamos la notificación al final de la cola
        cola.move_to_end()
        
    # Retornamos la cantidad de notificaciones en el rango de hora
    return pila_temporales.size()
from random import randint

from stack import Stack

# 1. Determinar el número de ocurrencias de un determinado elemento en una pila.
# pila = Stack()

# for i in range(10):
#     pila.push(randint(1, 10))

# print()
# pila.show()
# print()

# search_value = int(input('ingrese un numero para contar ocurrencias '))
# counter = 0

# while pila.size() > 0:
#     value = pila.pop()
#     if value == search_value:
#         counter += 1
    
# print(f'cantidad de ocurrencias de {search_value} en la pila: {counter}')

# 2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.
pila = Stack()

for i in range(10):
    pila.push(randint(1, 10))

print()
pila.show()
print()

pila_aux = Stack()

while pila.size() > 0:
    value = pila.pop()
    if value % 2 == 0:
        pila_aux.push(value)

while pila_aux.size() > 0:
    value = pila_aux.pop()
    pila.push(value)

pila.show()

# 3. Reemplazar todas las ocurrencias de un determinado elemento en una pila.
def reemplazar_elemento(pila: Stack, elemento_viejo: any, elemento_nuevo: any) -> None:
    """Reemplaza todas las ocurrencias de un determinado elemento en una pila."""
    pila_aux = Stack()
    
    # 1. Desapilamos buscando el elemento a reemplazar
    while pila.size() > 0:
        dato = pila.pop()
        if dato == elemento_viejo:
            dato = elemento_nuevo  # Reemplazo
        pila_aux.push(dato)
        
    # 2. Reconstruimos la pila original para mantener el orden
    while pila_aux.size() > 0:
        dato = pila_aux.pop()
        pila.push(dato)


# --- PRUEBA ---
if __name__ == "__main__":
    mi_pila = Stack()
    
    # Cargamos la pila (el último en entrar queda en la cima)
    mi_pila.push(10)
    mi_pila.push(5)
    mi_pila.push(20)
    mi_pila.push(5)
    mi_pila.push(8)
    
    print("ESTADO INICIAL (cima a base):")
    mi_pila.show()
    
    print("\nReemplazando todos los '5' por '99'...")
    reemplazar_elemento(mi_pila, 5, 99)
    
    print("\nESTADO FINAL (cima a base):")
    mi_pila.show()


# 4. Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.


# --- SOLUCIÓN DEL EJERCICIO 4 ---
def invertir_pila(pila: Stack) -> None:
    """Invierte el contenido de una pila usando solo una pila auxiliar."""
    pila_aux = Stack()
    
    # 1. Pasamos todos los elementos de la pila original a la auxiliar.
    # Esto invierte el orden una vez.
    while pila.size() > 0:
        dato = pila.pop()
        pila_aux.push(dato)
        
    # 2. Pasamos todos los elementos de la auxiliar de vuelta a la original.
    # Esto invierte el orden por segunda vez, logrando la inversión total.
    while pila_aux.size() > 0:
        dato = pila_aux.pop()
        pila.push(dato)


# --- PRUEBA ---
if __name__ == "__main__":
    mi_pila = Stack()
    
    # Cargamos la pila
    mi_pila.push(10)
    mi_pila.push(20)
    mi_pila.push(30)
    mi_pila.push(40)
    
    print("ESTADO INICIAL (cima a base):")
    mi_pila.show()
    
    print("\nInvirtiendo la pila...")
    invertir_pila(mi_pila)
    
    print("\nESTADO FINAL (cima a base):")
    mi_pila.show()

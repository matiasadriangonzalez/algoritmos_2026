#1. Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.
def fibonacci(num: int) -> int:
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(30))

#2. Implementar una función que calcule la suma de todos los números enteros comprendidos
# entre cero y un número entero positivo dado.
#caso base es si n == 0 return 0

def suma(num: int) -> int:
    if num == 0:
        return num
    else:
        return num + suma(num -1)

print(suma(2))

#3. Implementar una función para calcular el producto de dos números enteros dados.
def producto (a:int, b:int) -> int:
    if b == 0:
        return 0
    else: 
        return a + producto(a, b-1)

print(producto(5, 3))

#4. Implementar una función para calcular la potencia dado dos números enteros, el primero re-
# presenta la base y segundo el exponente.
def potencia(base:int, exponente:int) -> int:
    if exponente == 0:
        return 1
    else: 
        return base * potencia(base, exponente - 1)

print(potencia(2,0))

#5 Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not romano:
        """
        CASO BASE: si la cadena está vacía, no hay más números
        para procesar, y retornamos 0.
        """
        return 0

    if len(romano) == 1:
        """
        CASO BASE: si queda un solo caracter, devolvemos su valor
        sin hacer más restas.
        """
        return valores[romano[0]] 

    if valores[romano[0]] >= valores[romano[1]]:
        return valores[romano[0]] + romano_a_decimal(romano[1:])
    else:
        return -valores[romano[0]] + romano_a_decimal(romano[1:])

print(romano_a_decimal("XIC"))

#6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.
def secuencia_invertida(secuencia:str) -> str:
    if secuencia == "":
        return secuencia
    else: 
        return secuencia[-1] + secuencia_invertida(secuencia[:-1])

print(secuencia_invertida("matias"))

#7. Desarrollar un algoritmo que permita calcular la siguiente serie:
# 1+1/2+1/3+1/4+1/5+...+1/n
def serie(n:int) -> float:
    if n == 1: 
        return 1
    else: 
        return 1/n + serie(n-1)    

print(serie(3))

# 8. Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a siste-
# ma binario.
def convertir_decimal_binario(num:int) -> str:
    if num < 2:
        return str(num)
    else: 
        return convertir_decimal_binario(num // 2) + str(num % 2)

print(convertir_decimal_binario(0))

#9. Implementar una función para calcular el logaritmo entero de número n en una base b. Re-
# cuerde que:

def log(n:int, b:int) -> int: 
    if n < b: 
        return 0
    else: 
        return 1 + log(n//b, b)

print(log(18,3))

#10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.
def contar_digitos(num:int) -> int:
    if num < 10:
        return 1
    else:
        return 1 + contar_digitos(num//10)

print(contar_digitos(1253))

#11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.
def invertir(num:int, invertido:int=0) -> int:
    if num == 0:
        return invertido 
    else: 
        return invertir( num //10, invertido * 10 + num %10)

print(invertir(531))

#12. Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos
#número entero.
def mcd(a:int, b:int) -> int:
    if b == 0:
        return a
    else: 
        return mcd(b, a%b)

print(mcd(20,2))

#13. Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM)
# de dos número entero.

def mcm(a:int, b:int) -> int:
    if a == 0 or b == 0:
        return 0
    else:
        return (a*b) // mcd(a, b)

print(mcm(20,2))

#14. Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no
# se puede convertir el número a cadena.
def suma(num:int) -> int:
    if num == 0:
        return 0
    else:
        return num % 10 + suma(num//10)

print(suma(149))

#15. Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero.
# Puede utilizar una función auxiliar para que la función principal solo reciba como parámetro
# el número a calcular su raíz.
def _raiz_auxiliar(num: int, i:int) -> int:
    if i*i == num:
        return i
    elif i*i > num:
        return i-1
    else:
        return _raiz_auxiliar(num, i+1)

def raiz_cuadrada(num:int) -> int:
    if num <= 0:
        return 0
    else:
        return _raiz_auxiliar(num,1)

print(raiz_cuadrada(49))

#16. Implementar un función recursiva que permita obtener el valor de an en una sucesión geomé-
# trica (o progresión geométrica) con un valor a1= 2 y una razón r = -3. Además desarrollar un
# algoritmo que permita visualizar todos los valores de dicha sucesión desde a1 hasta an.

def valor_an(n: int) -> int:
    if n==1:
        return 2
    else:
        return valor_an(n-1) * -3

def visualizar_todos_los_valores(n:int) -> None:
    print(f'- susecion geometrica hasta a_{n}: ')
    for i in range(1, n+1):
        resultado= valor_an(i)
        print(f'a_{i} = {resultado}')

visualizar_todos_los_valores(5)

#17. Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.
mi_vector = [1,2,3,4,5]

def inverso_vector(vector: list) -> None:
    if vector == []:
        return
    else:
        print(vector[-1])
        inverso_vector(vector[:-1])
print("vector: ",mi_vector)
inverso_vector(mi_vector)

#18. Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.
def recorrer_matriz(matriz:list, f:int =0, c:int =0) -> None:
    if f == len(matriz):
        return
    elif c == len(matriz[f]):
        recorrer_matriz(matriz, f+1, 0)
    else:
        print(matriz[f][c])
        recorrer_matriz(matriz, f, c+1)

matriz = [[1,2,3], [4,5,6], [7,8,9]]
print("recorrer matriz:")
recorrer_matriz(matriz)

#19. Dada la siguiente definición de sucesión recursiva, realizar una función recursiva que permita
# calcular el valor de un determinado número en dicha sucesión.

def sucesion(n:int) -> float:
    if n == 1:
        return 2
    else:
        return n + (1 / sucesion(n-1))
print('susecion: ')
print(sucesion(2))

#20. Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de
#manera recursiva, y permita determinar si un valor dado está o no en dicha lista.
def busqueda_secuencial(lista: list, valor_buscado: int, indice: int=0) -> bool:
    if indice == len(lista):
        return False
    
    if lista[indice] == valor_buscado:
        return True
    else:
        return busqueda_secuencial(lista, valor_buscado, indice + 1)

lista = [1,3,5,7,9,10,13,15,17,19]
valor_buscado = 11
if busqueda_secuencial(lista, valor_buscado):
    print(f'el valor {valor_buscado} se encuentra en la lista')
else:
    print(f'el valor {valor_buscado} no se encuentra en la lista')


#21. Dada una lista de valores ordenadas, desarrollar un algoritmo que modifique el método de
# búsqueda binaria para que funcione de forma recursiva, y permita determinar si un valor dado
# está o no en dicha lista.
lista = [1,2,3,4,5,6,7,8,9,10]
buscado = 0

def busqueda_binaria(lista: list, buscado:int, izq:int, der:int) -> bool:
    if izq > der:
        return False

    medio = (izq + der) // 2
    if lista[medio] == buscado:
        return True
    elif lista[medio] < buscado:
        return busqueda_binaria(lista, buscado, medio +1, der)
    else:
        return busqueda_binaria(lista, buscado, izq, medio - 1)

print(busqueda_binaria(lista, buscado, 0, len(lista)-1))

#22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c. Utilizar un vector para representar la mochila.
        

def usar_la_fuerza(mochila: list, objeto_sacado:int = 0) -> tuple:
    if mochila == []:
        return False, objeto_sacado
    
    if mochila[0] == 'sable de luz':
        return True, objeto_sacado +1
    else:
        return usar_la_fuerza(mochila[1:], objeto_sacado + 1)

mochila_luke = ["ropa", "comida", "agua", "cuchillo", "sable de luz"]
encontrado, cantidad = usar_la_fuerza(mochila_luke)

if encontrado:
    print(f'sable encontrado! se tuvieron que sacar {cantidad} de objetos de la mochila!')
else:
    print(f'no se encontro el sable de luz! se sacaron {cantidad} de objetos de la mochila')


#23. Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
# matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
# y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
# y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
# avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.
# Unificamos el parámetro a "matriz" para que coincida con el interior
def salida_laberinto(matriz: list, f:int, c:int) -> bool:
    n = len(matriz)
    
    if f<0 or f >= n or c<0 or c>= n:
        return False
        
    if matriz[f][c] == 1 or matriz[f][c] == 'X':
        return False
        
    if f== n-1 and c == n-1:
        matriz[f][c] = 'X' # Agregamos la marca final antes de ganar
        return True

    matriz[f][c] = 'X'

    if salida_laberinto(matriz, f+1, c):
        return True
    if salida_laberinto(matriz, f, c+1):
        return True
    if salida_laberinto(matriz, f-1, c):
        return True
    if salida_laberinto(matriz, f, c-1):
        return True
        
    matriz[f][c] = 0
    return False

def imprimir_matriz_recursiva(matriz:list, f:int=0, c:int=0) -> None:
    if f == len(matriz):
        return
    elif c == len(matriz[f]):
        print()
        imprimir_matriz_recursiva(matriz, f+1, 0)
    else:
        print(matriz[f][c], end=' \t')
        imprimir_matriz_recursiva(matriz, f, c+1)

laberinto = [
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 0, 0, 0], 
    [1, 1, 1, 0]
]

print("Laberinto inicial: ")
imprimir_matriz_recursiva(laberinto)
print("\n") # Un salto de línea para separar

# Arrancamos en la fila 0, columna 0
if salida_laberinto(laberinto, 0, 0):
    print("¡Camino encontrado!")
    imprimir_matriz_recursiva(laberinto)
else:
    print("Camino no encontrado")

#24. En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una
# plataforma de bronce sobre la cual había tres agujas de diamante. En la primera aguja estaban
# apilados setenta y cuatro discos de oro, cada una ligeramente menor que la que estaba debajo.
# A los sacerdotes se les encomendó la tarea de pasarlos todos desde la primera aguja a la tercera,

# con dos condiciones, solo puede moverse un disco a la vez, y ningún disco podrá ponerse en-
# cima de otro más pequeño. Se dijo a los sacerdotes que, cuando hubieran terminado de mover

# los discos, llegaría el fin del mundo. Resolver este problema de la Torre de Hanói.
def torre_de_hanoi(n: int, origen: str, destino: str, auxiliar: str) -> None:
    if n == 1:
        print(f'mover el disco de {origen} a {destino}')
        return

    torre_de_hanoi(n-1, origen, auxiliar, destino)
    print(f'mover el disco de {origen} a {destino}')
    torre_de_hanoi(n-1, auxiliar, destino, origen)

torre_de_hanoi(2, 'palo origen', 'palo destino', 'palo auxiliar')

#25. Desarrollar una función recursiva que permita calcular y mostrar por pantalla el triángulo de
#Pascal, para n filas utilizando una matriz auxiliar para guardar los resultados parciales.

def triangulo_pascal(f:int, c:int, matriz: list) -> int:
    if c == 0 or f == c:
        return 1
    
    if matriz[f][c] != 0:
        return matriz[f][c]

    resultado = triangulo_pascal(f-1,c-1, matriz) + triangulo_pascal(f-1,c, matriz)
    
    matriz[f][c] = resultado
    return resultado

def mostrar_pascal(total_filas:int, matriz: list, f:int=0, c:int=0) -> None:
    if f == total_filas:
        return

    if c == f:
        print(matriz[f][:f+1])
        mostrar_pascal(total_filas, matriz, f + 1, 0)
    else:
        mostrar_pascal(total_filas, matriz, f, c+1)

total_filas = 7
matriz_pascal = [[0 for _ in range(total_filas)] for _ in range(total_filas)]
triangulo_pascal(total_filas-1, 0, matriz_pascal)
mostrar_pascal(total_filas, matriz_pascal)


#26. Resuelva el problema de colocar las 8 reinas sobre un tablero de ajedrez sin que las mismas
# se amenacen.
def es_segura(tablero: list, fila_nueva:int, col_nueva:int) -> bool:
    """es_segura: Usa una función interna (verificar) que recorre las columnas anteriores de forma recursiva hasta llegar a la actual."""
    # Función interna recursiva para revisar ataques
    def verificar(col_vieja):
        if col_vieja == col_nueva:
            return True
        
        fila_vieja = tablero[col_vieja]
        # Regla de fila y regla de diagonal
        if fila_vieja == fila_nueva or abs(fila_nueva - fila_vieja) == abs(col_nueva - col_vieja):
            return False
        
        return verificar(col_vieja + 1)
    
    return verificar(0)

def colocar_reinas(tablero: list, col:int = 0) -> bool:
    """colocar_reinas: Es el motor principal. Si encuentra un lugar seguro, se llama a sí misma para la col + 1."""

    # CASO BASE: Si llegamos a la columna 8, ganamos
    if col == 8:
        print("¡Solución encontrada!")
        print("Ubicaciones (columna: fila):", tablero)
        return True

    # Función interna recursiva para probar filas (reemplaza al for)
    def probar_fila(fila_actual: int) -> bool:
        """probar_fila: Es la clave para eliminar el for. Si no encuentra solución en la fila actual, se vuelve a llamar a sí misma con fila_actual + 1. 
        Si llega a 8, devuelve False y "retrocede" (hace el backtracking) para que la columna anterior busque una nueva posición."""
        # Caso base: se acabaron las filas para esta columna
        if fila_actual == 8:
            return False
        
        # Si es seguro, intentamos avanzar a la siguiente columna
        if es_segura(tablero, fila_actual, col):
            tablero[col] = fila_actual
            if colocar_reinas(tablero, col + 1):
                return True
        
        # Si no funcionó, pasamos a la siguiente fila recursivamente
        return probar_fila(fila_actual + 1)

    return probar_fila(0)

# --- Ejecución ---
# Tablero inicial: cada índice es una columna, el valor es la fila
tablero_inicial = [0] * 8
colocar_reinas(tablero_inicial)


#27. El valor 1 376 256 pertenece a una sucesión geométrica cuya razón es 4, implementar un algorit-
#mo para mostrar todos los valores de la sucesión hacia atrás hasta el valor de a1= 5,25.

def mostrar_sucesion_atras(valor_actual: float, limite: float, razon: float) -> None:
    print(valor_actual)
    
    if valor_actual <= limite:
        return

    mostrar_sucesion_atras(valor_actual/razon, limite, razon)

valor_inicial: float = 1376256.0
valor_limite: float = 5.25
razon: float = 4.0

print("generando sucesion hacia atras: ")
mostrar_sucesion_atras(valor_inicial, valor_limite, razon)

#28. Dada la siguiente definición de sucesión recursiva, realizar una función recursiva que permita
# calcular el valor de un determinado número en dicha sucesión.
def sucesion_recursiva(n:int) -> int:
    if n == 1:
        return 3
    
    return sucesion_recursiva(n-1) + (2 * n)

posicion= 4
resultado = sucesion_recursiva(posicion)
print("el valor de la posicion ", posicion, " es: ", resultado)


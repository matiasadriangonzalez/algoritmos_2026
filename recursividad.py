# # factorial(5) = 5 * 4 * 3 * 2 * 1 

# #fac(5) = 5 * fac(4)
# #fac(4) = 4 * fac(3)
# #fac(3) = 3 * fac(2)
# #fac(2) = 2 * fac(1)
# #fac(1) = 1

# #fac(N) = N * fac(N-1) -> fac(0) = 1 # si logramos encontrar esto en la moayoria de ejercicios ya tienen el ejercicio resuelto, porque a partird de aqui solo es cuestion de llamar a la funcion con el numero que queremos calcular y la funcion se va a encargar de hacer el resto del trabajo, es decir, llamar a la funcion con el numero anterior hasta llegar al caso base que es fac(0) = 1

# def factorial_r(num: int) -> int:
#     print(f'calculando factorial de {num}')
#     a = input()
#     if num == 0:
#         print('se alcanzo condiocion de fin, devolver valor por defecto')
#         a = input()
#         return 1
#     else:
#         print(f'resolucion parcial para {num}, hacer llamada recursiva con {num - 1}')
#         a = input()
#         temporal = num * factorial_r(num-1) # lo mismo que tenemos mas arriba, siempre tiene que tener un return.
#         print(f'se obtuvo resultado parcial {temporal} para {num}')
#         a = input()
#         return temporal
# #debe tener una condicion clara de fin y llamarse a si misma


# def factorial(num: int) -> int:
#     result = 1
#     for i in range(1, num + 1):
#         result = result * i
        
#     return result

# print(factorial(5))
# print(factorial_r(5))   

# #fibonacci recursiva
# def fibonacci_r(num: int) -> int:
#     if num == 0 or num == 1:
#         return num
#     else:
#         return fibonacci_r(num - 1) + fibonacci_r(num - 2)

# #fibonacci iterativa
# def fibonacci(num):
#     fib_1 = 0
#     fib_2 = 1
#     for i in range(2, num + 1):
#         temporal = fib_1 + fib_2
#         fib_1 = fib_2
#         fib_2 = temporal
#     return fib_2    
    
    

#ACTIVIDADES RECURSIVIDAD
# 2.Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.
# def suma(num:int) -> int:
#     if num == 0:
#         return num
#     else:
#         return num + suma(num - 1)  
# print(suma(5))

# 3.Implementar una función para calcular el producto de dos números enteros dados.
# def producto(a:int, b:int) -> int:
#     if b == 0:
#         return 0
#     else:
#         return a + producto(a, b - 1)
# print(producto(5, 3)) 

#4. Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.
# def potencia(base:int, exp:int) -> int:
#     if exp == 0:
#         return 1
#     else: 
#         return base * potencia(base, exp-1)
# print(potencia(2, 0))

#5.   

#6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.
#invertir(hola) = a + invertir(hol) = a + l + invertir(ho) = a + l + o + invertir(h) = a + l + o + h + invertir("") = a + l + o + h + "" = aloh
def sec_invertida(secuencia:str) -> str:
    if secuencia == "": #porque usamos len? porque es la forma de saber si la secuencia esta vacia, es decir, si no hay mas caracteres para invertir
        return secuencia
    else:
        return secuencia[-1] + sec_invertida(secuencia[:-1])
print(sec_invertida("hola"))

# 7.  Desarrollar un algoritmo que permita calcular la siguiente serie: 1 + 1/2 + 1/3 + ... + 1/n
# def serie(n:int) -> float:
#     if n == 1:
#         return 1
#     else:
#         return 1/n + serie(n - 1)
# print(serie(5))

#8. Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
# def convertir_decimal_binario(num:int) -> str:
#     if num ==0:
#         return "0"
#     else: 
#         return convertir_decimal_binario(num // 2) + str(num % 2) # explicame toda esta linea que es exactamente lo que hace: 
#         #1. num // 2: es la division entera, es decir, que se descarta el resto de la division
#         #2. str(num % 2): es el resto de la division, es decir, que se convierte en string
#         #3. +: es la concatenacion, es decir, que se une el resultado de la division entera con el resto de la division
#         #4. convertir_decimal_binario(num // 2): es la llamada recursiva, es decir, que se llama a la funcion con el resultado de la division entera
#         #5. str(): es la conversion a string, es decir, que se convierte en string
#         #6. return: es la devolucion del resultado, es decir, que se devuelve el resultado de la concatenacion
# print(convertir_decimal_binario(10))

#9. 

#10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.
def contar_digitos(num:int) -> int:
    if num <= 10:
        return 1
    else: 
        return 1 + contar_digitos(num // 10)
print(contar_digitos(12345))

#11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena. ??? 
def invertir_entero(num:int) -> int:
    if num < 10:
        return num
    else:
        return invertir_entero(num // 10) + num % 10
print(invertir_entero(530)) 

#12 Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos número entero.
def mcd(a:int, b:int) -> int:
    if b == 0:
        return a
    else: 
        return mcd(b, a % b)
print(mcd(12, 18))


#13. Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM) de dos número entero.
def mcd(a:int, b:int) -> int:
    if b == 0:
        return a
    else: 
        return mcd(b, a % b)
print(mcd(12, 18))

def mcm(a:int, b:int) -> int:
    if a == 0 or b == 0:
        return 0
    else:
        return (a*b) // mcd(a,b)
print(mcm(12, 18))


#14. Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no se puede convertir el número a cadena.
def suma(num:int) -> int:
    if num < 10:
        return num
    else: 
        return num % 10 + suma(num // 10)
print(suma(12))

#15. Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero.
# Puede utilizar una función auxiliar para que la función principal solo reciba como parámetro
# el número a calcular su raíz.


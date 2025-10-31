# Ejercicio 0

def factorial(num: int) -> int:
    """
    Funcion que toma un numero entero positivo
    y devuelve el factorial del mismo
    """
    if(num < 1): 
        return 1

    return num * factorial(num - 1)

#print(factorial(-1))

# Ejercicio 1

# 1
def repite_hola(n: int) -> None:
    """
    Funcion que recibe un entero positivo
    e imprime en pantalla n veces el mensaje "Hola"
    """
    
    if(n < 1):
        return
    
    print("Hola")
    return repite_hola(n - 1)
    
#repite_hola(-1)

# 2 

def repite_hola_concat(n: int) -> str:
    """
    """
    if(n < 1):
        return ""
    
    return "Hola" + repite_hola_concat(n - 1)

#print(repite_hola_concat(4))

# Ejercicio 2

def fibonacci(n: int) -> int: 

    if(n == 0):
        return 0
    if(n == 1):
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)

#print(fibonacci(5))

# Ejercicio 3

def print_string(n: int, s: str) -> None:
    if(n < 1):
        return None
    
    print(s)
    return print_string(n - 1, s)

def repeat_string(n: int, s: str) -> str:

    if(n == 0):
        return ''
    
    return s + repeat_string(n - 1, s)

#print_string(4, "Hola")
#print(repeat_string(4, "Test"))


# Ejercicio 4

""" Convierta la siguiente función iterativa a una definición recursiva. """

def iterativa(l: list[int]) -> int:
    c = 1
    for i in l:
        c = c * i
    return c



def recursiva(l: list[int]) -> int:

    if(not l):
        return 1
    
    return l[0] * recursiva(l[1:])

#print(iterativa([1,4,5,3,1]))
#print(recursiva([1,4,5,3,1]))

# Ejercicio 5

def find_max(intList: list[int]) -> int:
    
    if(len(intList) == 1):
        return intList[0]
    
    if(intList[0] > intList[1]):
        intList[1] = intList[0]

    return find_max(intList[1:])

#print(find_max([2,4,211,34,23,42,21,1,4]))

# Ejercicio 6

def power(a: int, b: int) -> int:

    if(b == 0):
        return 1 
    
    return a * power(a, b - 1)

#print(power(5,5))

# Ejercicio 7

def count_digits(num: int) -> int:

    cociente = num // 10
    
    if(cociente == 0):
        return 1
    
    return 1 + count_digits(cociente)

#print(count_digits(0))

# Ejercicio 8

def reverse_string_iterative(s: str) -> str:

    reversed_string = ""

    for i in range(len(s), 0, -1):
         reversed_string = reversed_string + s[i - 1]
    
    return reversed_string


def reverse_string_recursive(s: str) -> str:

    if(len(s) == 1):
        return s[0]
    
    return s[-1] + reverse_string_recursive(s[:-1])


#print(reverse_string_recursive("Agustin"))
#print(reverse_string_iterative("Agustin"))

# Ejercicio 9

def replicate(l: list[int], n: int) -> list[int]:

    if(not l):
        return []
    
    return [l[0]] * n + replicate(l[1:], n)

#print(replicate([1,2,2,4,2],3)) 

# Ejercicio 10 

def is_palindrome(s: str) -> bool:

    if(s == ''):
        return True
    return s[0].lower() == s[-1].lower() and is_palindrome(s[1:-1])   

#print(is_palindrome("Neuquen"))

# Ejercicio 11

def mystery(a: int, b: int) -> int:

    if (b == 0):
      return a
    
    return mystery(2 * a, b - 1)


#print(mystery(7,3))

#1. ¿Qué muestra por pantalla el siguiente código? Intente deducirlo sin ejecutarlo.
#>>> print(mystery(7, 3))
#>>> 56

#2. ¿Cuántas veces se invoca recursivamente mystery en la llamada del item anterior?
# Se invoca recursivamente 3 veces.

#3. De manera general: ¿qué muestra por pantalla la llamada f(x, 3) para un x cualquiera? y ¿qué
# muestra por pantalla la llamada f(x, y) para x, y cualesquiera?
#
# La llamada f(x, 3) muestra por pantalla el resultado de la operacion (2 * ( 2 * ( 2 * x))) = 8 * x
# Y f(x, y) cada llamada duplica a x y disminuye a y hasta llegar al caso base y retornar el valor. x * (2 ** y)


# Ejercicio 12

def potencia(a: int, b: int) -> int:
    
    if(b >= 0):
        return power(a,b)
    else:
        positiveB = b * -1
        return 1 / power(a, positiveB)

#print(potencia(-8,-2))

# Ejercicio 13

def aux(lista: list[int]) -> tuple[int, float]:
    
    if(not lista):
        return (0,0)
    
    suma, cantidad = aux(lista[1:])

    suma = suma + lista[0]
    cantidad += 1

    return (suma, cantidad)

def average(lista: list[float]) -> float:

    suma, cantidad = aux(lista)
    return suma / cantidad

#print(aux([1,2,3,4]))

# Ejercicio 14

def posicion(a: str, b: str) -> int:

    lenA = len(a)
    lenB = len(b)

    if(lenA < lenB):
        return False

    if(a[:lenB] == b):
        return True
    
    return posicion(a[1:], b)
    
#print(posicion("posicion", "si"))

# Ejercicio 15

memo: dict[int, int] = { 0: 0, 1: 1 }


def fibonacci_memo_global(n: int) -> int:
    """
    Devuelve el n-esimo numero de la sucesion de fibonacci por ejemplo
    n = 4 la funcion retorna 3
    recordatorio sucesion fibonacci [0,1,1,2,3,5,8,13,21... ]
    """
    if(n in memo):
        return memo[n]
    

    memo[n] = fibonacci_memo_global(n - 2) + fibonacci_memo_global(n - 1)
    
    return memo[n]

def fibonacci_memo_aux(n: int, memo: dict[int, int]) -> tuple[int, dict[int, int]]:

    if(n in memo):
        return memo[n] , memo
    
    memo[n] = fibonacci_memo_aux(n - 2, memo)[0] + fibonacci_memo_aux(n - 1, memo)[0]
    
    return memo[n], memo

def fibonacci_memo(n: int) -> int:

    ret, memo = fibonacci_memo_aux(n, { 0: 0, 1: 1 })
    
    return ret
    


""" import time


start_time = time.time()
print(fibonacci(50)) 
end_time = time.time()
total = end_time - start_time
print(f"{total:.5f}") """

#print(fibonacci(80))
#print(fibonacci_memo_global(100))
#print(fibonacci_memo(100, { 0: 0, 1: 1 }))
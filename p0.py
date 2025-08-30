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

#print_string(1, "Hola")


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
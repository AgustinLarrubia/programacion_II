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

print(repite_hola_concat(4))

# Ejercicio 2


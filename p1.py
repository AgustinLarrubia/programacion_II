# Practica 1 - Programacion Orientada a Objetos

import math

# Ejercicio 1
# Ejercicio 2

class Point:        
    """ representación de un punto en un plano cartesiano 2D """
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
         return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
    
    def distancia(self, other) -> float:
       
        dx = other.x - self.x
        dy = other.y - self.y

        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia

       

class Rectangle:

    def __init__(self, width: float, height: float, corner: Point) -> None:
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self) -> str:
        return '( ' + str(self.width) + ', ' + str(self.height) + ', ' + str(self.corner) + ' )'
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
       
        return self.width == other.width and self.height == other.height and self.corner == other.corner
    
    def mover_rectangulo_pura(self, dx: float, dy: float): 
       
        width = self.width
        height = self.height

        x = self.corner.x + dx
        y = self.corner.y + dy

        corner = Point(x,y)

        return Rectangle(width, height, corner)

    def mover_rectangulo_modificadora(self, dx: float, dy: float) -> None:
        self.corner.x += dx
        self.corner.y += dy

     

       
    

""" rectangle = Rectangle(5,10,Point(2,3)) # Instancia objeto Rectangle y se almacena en rectangle
rectangle.mover_rectangulo_modificadora(3,2) # Modifica el objeto
new_rectangle = rectangle.mover_rectangulo_pura(2,3) # Devuelve una nueva instancia y se almacena en new_rectangle
print(rectangle)
print(new_rectangle)
print(rectangle is new_rectangle) # False porque son dos objetos diferentes (distintas instancias del mismo objeto) """

""" A = Point(2,5)
B = Point(4,3)

print(A.distancia(B)) # 2.8284271247461903 """


# Ejercicio 3

class Automovil:
   
    def __init__(self, patente: str, marca: str, km_recorridos: float = 0, litros_nafta: float = 0) -> None:
        self.patente = patente
        self.marca = marca
        self.km_recorridos = km_recorridos
        self.litros_nafta = litros_nafta
    
    def __str__(self) -> str:
        return f"Patente: {self.patente}, Marca: {self.marca}, Kilometros Recorridos: {self.km_recorridos}, Litros de nafta: {self.litros_nafta}"
    
    def tiene_nafta(self) -> bool:
        return self.litros_nafta > 0
    
    def tiene_nafta_km(self, kilometros) -> bool:
        nafta_necesaria = kilometros * 8.8 / 100
        return  nafta_necesaria <= self.litros_nafta

    def avanzar(self, kilometros: float) -> None:
        if not self.tiene_nafta_km(kilometros):
            print("Es necesario cargar nafta para recorrer la cantidad indicada de kilómetros.")
            return

        self.km_recorridos += kilometros
        self.litros_nafta -= kilometros * 8.8 / 100

    def cargar_nafta(self, litros: float) -> None:
        self.litros_nafta += litros

""" auto = Automovil("AA123ZZ", "Ford", 10, 8.8)
print(auto) 
auto.avanzar(100)
print(auto)
auto.avanzar(1)
print(auto) """

auto = Automovil("AEF-202", "Peugeot")
auto.cargar_nafta(10)
print(auto.km_recorridos)  # 0
print(auto.litros_nafta)   # 10

auto.avanzar(50)
print(auto.km_recorridos)  # 50
print(auto.litros_nafta)   # 5.6

auto.avanzar(100)          # Es necesario cargar nafta para recorrer la cantidad indicada de kilómetros

auto.avanzar(40)
print(auto.km_recorridos)  # 90
print(auto.litros_nafta)   # 2.08
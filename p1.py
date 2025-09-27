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

""" auto = Automovil("AEF-202", "Peugeot")
auto.cargar_nafta(10)
print(auto.km_recorridos)  # 0
print(auto.litros_nafta)   # 10

auto.avanzar(50)
print(auto.km_recorridos)  # 50
print(auto.litros_nafta)   # 5.6

auto.avanzar(100)          # Es necesario cargar nafta para recorrer la cantidad indicada de kilómetros

auto.avanzar(40)
print(auto.km_recorridos)  # 90
print(auto.litros_nafta)   # 2.08 """

# Ejercicio 4

# Robot que se mueve en plano cartesiano x y infinito
# Movimientos
#  - Avanzar (A)
#  - Retroceder  (R)
#  - Avanzar hacia la izquierda (I) o la derecha (D)
# Metodos
# Mueve(orden (Movimientos)), posicion_actual(Coordenada))
# El robot se inicializara en (0,0)

# Ejercicio 5
# Ahora mover puede recibir uno o una secuencia de movimientos. Ejemplo: "A" o "RRAARDDI"
# ATENCION: si la secuencia de movimientos contiene un movimiento invalido, debe informarlo antes de realizar cualquier movimiento
# Agregar metodo obtener_historico_de_movimientos que devuelva el historial de movimientos que realizo el robot
# Agregar un metodo como_volver que indique la secuencia de movimientos necesarios para volver al origen ( (0,0) )

class Robot():

    def __init__(self) -> None:
        self.x: float = 0
        self.y: float = 0
        self.movimientos: dict[str , tuple[float, float]] = {
            'A': (0,1),
            'R': (0,-1),
            'I': (-1,0),
            'D': (1,0)
        }
        self.historial: str = ""

    def mover(self, movimiento: tuple[float, float]) -> None:
        dx, dy = movimiento
        self.x += dx
        self.y += dy

    def posicion_actual(self) -> tuple[float, float]:

        return (self.x, self.y)
    
    
    def obtener_historico_de_movimientos(self) -> str:

        return self.historial
    
    def registrar_historico(self, orden: str) -> str:
        self.historial += orden
        return self.historial
    

    def limpiar_historial(self) -> None:
        self.historial = ""

    def invertir_movimiento(self, orden: str) -> str:
        opuestos = {
            'A': 'R',
            'R': 'A',
            'D': 'I',
            'I': 'D'
        }
        return opuestos[orden]

    def como_volver(self) -> str:
        ordenes_volver = ""
        for orden in reversed(self.historial):
            ordenes_volver += self.invertir_movimiento(orden)

        self.limpiar_historial()

        return ordenes_volver
    
    def check_ordenes(self, ordenes: str) -> tuple[str, str]:

        ordenes_validas: str = "".join(char for char in ordenes if char in self.movimientos)
        ordenes_invalidas: str = "".join(char for char in ordenes if char not in self.movimientos)

        if(len(ordenes_invalidas) > 0):
            print(f"Se encontraron ordenes no validas {ordenes_invalidas}. El programa continuara su ejecucion")

        return ordenes_validas, ordenes_invalidas

    def mueve(self, ordenes: str) -> None :

        ordenes = ordenes.upper() # Formateo las ordenes para que todas esten en mayus

        ordenes_validas, ordenes_invalidas = self.check_ordenes(ordenes)

        for orden in ordenes_validas:
            movimiento: tuple[float, float] = self.movimientos[orden]
            self.mover(movimiento)
            self.registrar_historico(orden)
        
        return self.posicion_actual()


# TEST Ejercicio 4
""" mi_robot = Robot()
orden = input("Introduce la orden: ")
while orden != 'fin':
    mi_robot.mueve(orden)
    print(mi_robot.posicion_actual())
    orden = input("Introduce la orden: ") """

# TEST Ejercicio 5
mi_robot = Robot()
orden = input("Introduce la orden, volver para regresar al origen y fin para terminar: ")
while orden != 'fin':

    if(orden.upper() == 'VOLVER'):
        orden = mi_robot.como_volver()
    
    print(orden)
    mi_robot.mueve(orden)
    print(mi_robot.posicion_actual())
    orden = input("Introduce la orden: ")

print(mi_robot.obtener_historico_de_movimientos())
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
""" mi_robot = Robot()
orden = input("Introduce la orden, volver para regresar al origen y fin para terminar: ")
while orden != 'fin':

    if(orden.upper() == 'VOLVER'):
        orden = mi_robot.como_volver()
    
    print(orden)
    mi_robot.mueve(orden)
    print(mi_robot.posicion_actual())
    orden = input("Introduce la orden: ")

print(mi_robot.obtener_historico_de_movimientos()) """

# Composición y Herencia

# Ejercicio 6

class Materia():

    def __init__(self, codigo: str, nombre: str, creditos: int) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.creditos: int = creditos

    def __str__(self) -> str:
        return f"{self.codigo} {self.nombre} ({self.creditos})"


class Carrera():
    
    def __init__(self, materias: list[Materia]) -> None:
        self.materias: list[Materia] = materias
        self.materias_aprobadas: list[tuple[str, float]] = []
        self.materias_aprobadas_dict: dict[str, tuple[Materia, float]] = {} #TODO Implementar diccionario
    
    def get_creditos(self) -> str:
        total_creditos: float = 0
        for materia in self.materias:
            for aprobada in self.materias_aprobadas:
                if(aprobada[0] == materia.codigo):
                    total_creditos += int(materia.creditos)

        return str(total_creditos)
    
    def get_promedio(self) -> str:
        total_notas: float = 0
        cant_materias: float = 0

        if(len(self.materias_aprobadas) < 1):
            return "N/A"

        for materia in self.materias_aprobadas:
            total_notas += materia[1]
            cant_materias += 1
        
        return str(total_notas / cant_materias)
    
    def get_materias_aprobadas(self) -> Materia:
        materias_aprobadas = ""
        for materia in self.materias:
            for aprobada in self.materias_aprobadas:
                if(aprobada[0] == materia.codigo):
                    materias_aprobadas += f" {materia}"
        
        return materias_aprobadas
    
    def materia_existe(self, codigo: str) -> bool:
        for materia in self.materias:
            if(codigo == materia.codigo ):
                return True
        return False
    
    def aprobar(self, codigo: str, nota: float) -> None:
        existe: bool = self.materia_existe(codigo)
        if(not existe):
            print(Exception("Error: La materia 75.14 no es parte del plan de estudios"))
            return
        self.materias_aprobadas.append((codigo, nota))

    
    def __str__(self) -> str:
        return f"Créditos: {self.get_creditos()} -- Promedio: {self.get_promedio()} -- Materias Aprobadas: {self.get_materias_aprobadas()}"


""" analisis2 = Materia("61.03", "Análisis 2", 8)
fisica2 = Materia("62.01", "Física 2", 8)
algo1 = Materia("75.40", "Algoritmos 1", 6)

c = Carrera([analisis2, fisica2, algo1])

print(c)
# >>> Créditos: 0 -- Promedio: N/A -- Materias aprobadas:

c.aprobar("95.14", 7)
# >>> Error: La materia 75.14 no es parte del plan de estudios
c.aprobar("75.40", 10)
c.aprobar("62.01", 7)
print(c)
# >>> Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas: 75.40 Algoritmos 1 (10) 62.01 Física 2 (7) """


# Ejercicio 7

# Encontrar los errores en el siguiente código y proponer soluciones:
""" 
class Cosa:
    def __init__(self, valor):
        self.valor = valor

class Coleccion:
    def __init__(self):
        self.coleccion = []

    def agregar_cosa(cosa: Cosa):
        coleccion.append(cosa) # (2) Se quiere acceder a coleccion pero no se paso self como parametro y no se esta haciendo referencia al mismo.

cosa = Cosa() # (1) Cosa se esta instanciando sin un valor y este es necesario
coleccion = Coleccion()
coleccion.agregar_cosa(cosa) 
"""


class Cosa:
    def __init__(self, valor = 0): # (1) Una posible solucion es colocar un valor por defecto
        self.valor = valor
    
    def __str__(self) -> str:
        return str(self.valor)

class Coleccion:
    def __init__(self):
        self.coleccion = []

    def agregar_cosa(self, cosa: Cosa):
        self.coleccion.append(cosa) # (2) La solucion es colocar self como parametro para asi poder acceder a los atributos de la clase

    def __str__(self) -> str:
        return ", ".join(str(cosa) for cosa in self.coleccion)

""" cosa = Cosa() # (1) Cosa se esta instanciando sin un valor y este es necesario
coleccion = Coleccion()
coleccion.agregar_cosa(cosa)
print(coleccion) """

# Ejercicio 8

""" 
Considere la siguiente jerarquía de clases:

                          |--- Felinos
Animales --- Mamíferos ---|--- Cánidos
                          |--- Primates --- Hacker

  Programe un conjunto de seis clases que modele esta taxonomía utilizando clases. Luego, agregue un
método speak a cada clase imprimiendo un mensaje apropiado a cada clase (por ejemplo, una instancia
de animal podría imprimir "Soy un animal").

  Luego, agregue un método talk a la clase Animal, que simplemente delegue el funcionamiento en
speak. ¿Qué ocurre al llamar a talk en una subclase? ¿Qué ocurre si borramos el método speak de la
clase Hacker? 

"""

class Animal():
    def __init__(self) -> None:
        pass

    def speak(self) -> None:
        print("Soy un animal.")
    
    def talk(self) -> None:
        self.speak()

class Mamifero(Animal):
    def __init__(self) -> None:
        super().__init__()

    def speak(self) -> None:
        print("Soy un mamifero")

class Felino(Mamifero):
    def __init__(self) -> None:
        super().__init__()

    def speak(self) -> None:
        print("Soy un felino")

class Canido(Mamifero):
    def __init__(self) -> None:
        super().__init__()

    def speak(self) -> None:
        print("Soy un canido")

class Primate(Mamifero):
    def __init__(self) -> None:
        super().__init__()

    def speak(self) -> None:
        print("Soy un primate")

class Hacker(Primate):
    def __init__(self) -> None:
        super().__init__()

    def speak(self) -> None:
        print("Soy un kaker") # hacker T!


""" animal = Animal()
mamifero = Mamifero()
felino = Felino()
canido = Canido()
primate = Primate()
hacker = Hacker()

animal.speak()
mamifero.speak()
felino.speak()
canido.speak()
primate.speak()
hacker.speak() """

# ¿Qué ocurre al llamar a talk en una subclase? 

""" primate.talk() """

"""
  Al invocar talk en una subclase esta llama a el metodo speak correspondiente a 
la subclase que lo invoco.
  En este caso se imprime en consola el mensaje que contiene el metodo speak en la clase primate.

>>> Soy un primate
"""

# ¿Qué ocurre si borramos el método speak de la clase Hacker? 

"""
Si borramos el metodo speak de la clase hacker se llamara al metodo
del mismo nombre definido en su clase padre (Si es que este esta definido) sino buscar siempre en la clase 
superior la existencia de la misma.
"""


# Ejercicio 9

""" 
  Complete la funcionalidad de la clase Jugador, implementando los siguientes métodos:
    • golpeado: quita vida al jugador.
    • golpear: quita vida al enemigo y lo agrega a la lista de enemigos golpeados. 
"""
class Entidad:
    def __init__(self, vida_inicial: int):

        self.vida = vida_inicial

class Enemigo(Entidad):
    
    def __str__(self) -> str:
        return f"Enemigo: Vida: {self.vida}"

class Jugador(Entidad):
    def __init__(self, vida_inicial: int):
        super().__init__(vida_inicial)
        self.enemigos_golpeados = []

    def golpeado(self, cuanto: int):
        if(cuanto > self.vida):
            self.vida = 0
        else:
            self.vida -= cuanto

    def golpear(self, enemigo: Enemigo, cuanto: int):
        self.enemigos_golpeados.append(enemigo)
        if(cuanto > enemigo.vida):
            enemigo.vida = 0
        else:
            enemigo.vida -= cuanto

    def __str__(self) -> str:
        return f"Estadisticas: Vida: {self.vida} Enemigos golpeados: {self.enemigos_golpeados}" # Direcion en memoria de los enemigos golepados


""" player1 = Jugador(100)
enemigo = Enemigo(100)
player1.golpeado(20)
print(player1)
player1.golpear(enemigo, 50)
print(enemigo)
print(player1)
player1.golpeado(50)
print(player1)
player1.golpear(enemigo, 60)
print(enemigo) """

# Ejercicio 10

class Billetera:
    """
    Faltaria implementar una variable y metodo que maneje el 
    reinicio del reintegro cada mes.
    """
    # Variables de clase.
    PORCENTAJE_DE_REINTEGRO: float = 30
    MONTO_MAXIMO_DE_REINTEGRO: float = 5000

    def __init__(self, nro_cuenta: str) -> None:
        self.nro_cuenta = nro_cuenta
        self.saldo = 0
        self.reintegro_restante = self.MONTO_MAXIMO_DE_REINTEGRO

    def cargar(self, monto: float) -> None:
        self.saldo += monto

    def calcular_descuento(self, monto: float) -> float:
        return (monto * self.PORCENTAJE_DE_REINTEGRO) / 100
    
    def pagar(self, monto: float) -> None:

        if(monto > self.saldo):
            print("Fondos insuficientes")
            return
        
        descuento: float = self.calcular_descuento(monto)

        if(descuento > self.reintegro_restante): # Importante validar antes de descontar
            descuento = self.reintegro_restante

        self.reintegro_restante -= descuento

        total: float = monto - descuento
        print(f"Total a pagar: {total}")
        self.saldo -= total
    
    def monto_descuento_pendiente(self) -> float:
        return self.reintegro_restante

billetera1 = Billetera("123")
billetera1.cargar(100000)
billetera1.pagar(10000)
print(billetera1.monto_descuento_pendiente())
billetera1.pagar(10000)
print(billetera1.monto_descuento_pendiente())

# Ejemplo practica
cuenta = Billetera("1202")
cuenta.cargar(15000)
cuenta.pagar(15000)
print(cuenta.monto_descuento_pendiente())
# >>> 500
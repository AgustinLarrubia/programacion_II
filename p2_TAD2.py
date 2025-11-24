from typing import Any

class Stack:
    """ 
    Ejercicio 1
        Defina una clase Pila que implemente el TAD Pila utilizando listas de Python
      
    Representa una pila con operaciones de apilar , desapilar y
    verificar si está vacía. 
    """

    def __init__(self) -> None:
        """ Crea una pila vacia """
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        """ Apila un elemento a la pila """
        self.items.append(item)

    def pop(self) -> Any:
        """ 
          Des - apila un elemento y lo devuelve .
        Si la pila esta vacía, imprime un mensaje de error y retorna
        inmediatamente 
        """
        if self.isEmpty():
            print("La pila esta vacia.")
            return 
        
        return self.items.pop()

    def isEmpty(self) -> bool:

        return (self.items == [])
    

""" p = Stack()
print(p.isEmpty())
#True
p.push(1)
print(p.isEmpty())
#False
p.push(5)
p.push("+")
p.push(22)
print(p.pop())
#22
q = Stack()
q.pop()
#La pila esta vacía """

class _Node:

    def __init__(self, data: Any | None = None, next: "_Node" = None) -> None:

        self.data = data
        self.next = next

class LinkedStack:
    """
    Ejercicio 2
    
        Defina una clase PilaEnlazada que implemente el TAD Pila utilizando una estructura enlazada.
    """

    def __init__(self) -> None:

        self.first: _Node | None = None
        self.len: int = 0

    def __str__(self) -> str:
        
        if(self.first is None):
            return str(None)
        
        n_act = self.first
        stack: str = ""

        while n_act is not None:

            data = n_act.data

            stack += f'{str(data)}\n'
            
            n_act = n_act.next

        return stack

            
    
    def isEmpty(self) -> bool:
        return self.first is None
    
    def push(self, x: Any) -> None:

        new_node = _Node(x)

        new_node.next = self.first
        self.first = new_node

        self.len += 1

    def pop(self) -> Any:

        if(self.isEmpty()):
            print("La pila esta vacia")
            return
        
        data = self.first.data
        to_delete_node = self.first


        self.first = to_delete_node.next

        to_delete_node.next = None

        self.len -= 1

        return data
        
        

""" s = LinkedStack()
print(s.isEmpty())
#True
s.push(1)
print(s.isEmpty())
#False
s.push(5)
s.push("+")
s.push(22)
print(s.pop())
#22
q = LinkedStack()
q.pop()
#La pila esta vacía """

class LinkedStackWithMax():
    """
    Ejercicio 3

        Defina una clase PilaConMaximo que implemente las operaciones de Pila (push(item) y pop()) y el
    método obtener_maximo() que devuelva el elemento máximo de la Pila, sin sacarlo de la misma y que
    funcione en tiempo constante.

        Ayuda: usar dos pilas, una para guardar los elementos y otra para guardar los máximos.
    """

    def __init__(self) -> None:

        self.stack: LinkedStack = LinkedStack()
        self.max_stack: LinkedStack = LinkedStack()
    
    def get_max(self) -> Any | None:

        if(self.max_stack.isEmpty()):
            return None
        
        return self.max_stack.first.data
    
    def set_max(self, x: Any) -> None:

        self.max_stack.push(x)
    
    def push(self, x: Any) -> None:

        if isinstance(x, int) and (self.get_max() is None or x >= self.get_max()):
            self.set_max(x)

        self.stack.push(x)
    
    def pop(self) -> Any:

        if(self.stack.isEmpty()):
            print("La pila esta vacia")
            return
        
        data = self.stack.pop()     

        if(self.get_max() == data):
            self.max_stack.pop()
        
        return data


""" s = LinkedStackWithMax()
print(s.stack.isEmpty())
#True
print(s.max_stack.isEmpty())
#True
print(s.get_max())
#None
s.pop()
#La pila esta vacia
s.push(1)
print(s.stack.isEmpty())
#False
print(s.max_stack.isEmpty())
#False
s.push(5)
s.push("+")
s.push(22)
print(s.pop())
#22
q = LinkedStackWithMax()
q.push(20)
q.push(5)
q.push(53)
q.push(522)
q.push(52)
q.push(2)
print(q.get_max())
print(q.pop())
#La pila esta vacía """


def balanceado(exp: str) -> bool:
    """
    Ejercicio 4

        Escriba una función balanceado que reciba una expresión matemática (en forma de string) y devuelve
    True si los paréntesis (), corchetes [] y llaves {} están correctamente balanceados, False en caso
    contrario.
    """

    expStack: LinkedStack = LinkedStack()
    orderExp: dict[str] = {'}': '{', ']': '[', ')': '('}
    openExp: list[str] = ['{', '[', '(']

    for char in exp:

        popped = "ok"

        if(char in openExp):
            expStack.push(char)
        elif(char in orderExp):

            if(expStack.isEmpty()):
                return False

            popped = expStack.pop()

            
        if(char in orderExp and orderExp[char] != popped):
            return False
    
    isBalanced: bool = expStack.isEmpty()

    return isBalanced
        

""" print(balanceado('(x+y)/2'))
#True
print(balanceado('[8*4(x+y)]+{2/5}'))
#True
print(balanceado('(x+y]/2'))
#False
print(balanceado('1+)2(+3'))
#False
print(balanceado('(1+[2+35)]'))
#False """


class Queue:
    """
    Ejercicio 5

        Defina una clase Cola que implemente el TAD Cola utilizando listas de Python.
    """

    def __init__(self) -> None:

        self.items = []

    def insert(self, item: Any) -> None:

        self.items.append(item)

    def remove(self) -> Any:
        
        if self.isEmpty():

            print("La cola esta vacia.")
            return
        
        return self.items.pop(0)

    def isEmpty(self) -> bool:
        
        return self.items == []
    
""" q = Queue()
print(q.isEmpty())
#True
q.insert(1)
q.insert(2)
q.insert(5)
print(q.isEmpty())
#False
print(q.remove())
#1
print(q.remove())
#2
q.insert(8)
print(q.remove())
#5 """


class LinkedQueue:
    """
    Ejercicio 6

        Defina una clase ColaEnlazada que implemente el TAD Cola utilizando una estructura enlazada.
    """
    def __init__(self):
        
        self.first: _Node | None = None
        #self.last para reducir el costo de la operacion insert se puede agregar un nodo last
        self.len: int = 0
        pass
    def __len__(self):
        return self.len
    
    def isEmpty(self) -> bool:
        return self.first is None
    
    def insert(self, x: Any) -> None:
        
        new_node = _Node(x)
        n_act = self.first

        if n_act is None:
            self.first = new_node
        else:

            while n_act.next is not None:

                n_act = n_act.next
        
            n_act.next = new_node 
            
        self.len += 1

    def remove(self) -> Any:

        if(self.isEmpty()):
            print("La cola esta vacia")
            return
        
        to_delete_node = self.first
        data = to_delete_node.data

        self.first = to_delete_node.next
        to_delete_node.next = None

        self.len -= 1

        return data
    
""" q = LinkedQueue()
print(q.isEmpty())
#True
q.insert(1)
q.insert(2)
q.insert(5)
print(q.isEmpty())
#False
print(q.remove())
#1
print(q.remove())
#2
q.insert(8)
print(q.remove())
#5 """

# Cola Generalizada

"""
    Ejercicio 7

        Hace un montón de años había una viejísma sucursal del correo que tenía un cartel que decía “No
    se recibirán más de 5 cartas por persona”. Es decir, la gente entregaba sus cartas (hasta la cantidad
    permitida) y luego tenía que volver a hacer la cola si tenía más cartas para despachar.
        Modelar una cola de correo generalizada, donde en la inicialización se indica la cantidad (no necesariamente 5) de cartas que se reciben por persona
"""

class Cliente:
    def __init__(self, nombre: str, cant_cartas: int = 1) -> None:
        self.nombre = nombre
        self.cant_cartas = cant_cartas

class ColaGeneralizada:


    def __init__(self, cartas_x_persona: int = 5) -> None:
        
        self.first: _Node | None = None
        self.cartas_x_persona = cartas_x_persona
        self.len: int = 0

    def isEmpty(self) -> bool:
        return self.first is None

    def push(self, cliente: Cliente) -> None:
        
        nuevo_cliente = _Node(cliente)

        if self.first is None:

            self.first = nuevo_cliente
        else:
            
            n_act = self.first

            while n_act.next is not None:

                n_act = n_act.next

            n_act.next = nuevo_cliente

        self.len += 1

    def remove(self) -> Cliente:

        if self.isEmpty():
            print("La cola esta vacia")
            return
        
        cliente_atendido = self.first      
        data: Cliente = cliente_atendido.data

        if data.cant_cartas > self.cartas_x_persona:

            cartas_a_entregar = self.cartas_x_persona
        else:
            cartas_a_entregar = data.cant_cartas

        data.cant_cartas -= cartas_a_entregar

        if data.cant_cartas > 0:
             self.push(data) # Vuelve a formar la fila

        self.first = cliente_atendido.next
        cliente_atendido.next = None

        self.len -= 1

        print(f"Atendido cliente {data.nombre}, despachadas {cartas_a_entregar} cartas")
        return cliente_atendido.data

        


"""
correo = ColaGeneralizada()
correo.push(Cliente("Ana", 1))
correo.push(Cliente("Facu", 1))
correo.push(Cliente("Seba", 2))
correo.push(Cliente("Joe", 6))
correo.push(Cliente("Pablo", 9))
correo.push(Cliente("Ana", 1))
correo.push(Cliente("Facu", 1))
correo.push(Cliente("Seba", 2))

while not correo.isEmpty():
    correo.remove()
"""

""" 
>>> Atendido cliente Ana, despachadas 1 cartas
>>> Atendido cliente Facu, despachadas 1 cartas
>>> Atendido cliente Seba, despachadas 2 cartas
>>> Atendido cliente Joe, despachadas 5 cartas
>>> Atendido cliente Pablo, despachadas 5 cartas
>>> Atendido cliente Ana, despachadas 1 cartas
>>> Atendido cliente Facu, despachadas 1 cartas
>>> Atendido cliente Seba, despachadas 2 cartas
>>> Atendido cliente Joe, despachadas 1 cartas
>>> Atendido cliente Pablo, despachadas 4 cartas 
"""

# Ejercicios adicionales

def sort_stack(even_stack: LinkedStack, odd_stack: LinkedStack) -> LinkedStack:

    sorted_stack = LinkedStack()


    while not odd_stack.isEmpty():
        data = odd_stack.pop()
        sorted_stack.push(data)

    while not even_stack.isEmpty():
        data = even_stack.pop()
        sorted_stack.push(data)

    return sorted_stack

def reordenar_pares_impares(stack: LinkedStack) -> LinkedStack | None:
    """
    Ejercicio 7

        Dado un Stack de números, reordenarlos para que estén abajo los impares y arriba los pares, pero que
    entre números del mismo tipo preserven el orden.
    
        Ayuda: utilizar dos Stacks auxiliares de números pares e impares respectivamente.
    """
    if(stack.isEmpty()):
        print("La pila esta vacia")
        return None
    
    stack_pares: LinkedStack = LinkedStack()
    stack_impares: LinkedStack = LinkedStack()

    while not stack.isEmpty():
        
        number = stack.pop()

        if  number % 2 == 0:
            stack_pares.push(number)
        else:
            stack_impares.push(number)


    return sort_stack(stack_pares, stack_impares)

s = LinkedStack()
s.push(1)
s.push(2)
s.push(9)
s.push(5)
s.push(8)
s.push(4)

print(reordenar_pares_impares(s))

"""     
Ejemplo:
4    4
8    8
5 => 2
9    5
2    9
1    1 
"""

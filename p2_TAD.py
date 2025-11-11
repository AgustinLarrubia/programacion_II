from hmac import new
from typing import Any

class _Node:
    
    def __init__(self, data: Any = None, next: "_Node" = None) -> None:
        self.data: Any = data
        self.next: _Node = next

    def __str__(self) -> str:
        return str(self.data)
    

def see_list(nodo: _Node) -> None:
    while nodo is not None:
        print(nodo)
        nodo = nodo.next

""" nodo3 = _Node("datos...")
nodo2 = _Node("mas datos...", nodo3)
nodo1 = _Node("muchos datos", nodo2)
see_list(nodo1) """

class LinkedList:
    
    def __init__(self) -> None:
        self.first: _Node | None = None
        self.len: int = 0

    def __str__(self) -> str:
        
        n_act = self.first
        linkedList = ""
        if(n_act is None):
            return str(None)

        while n_act is not None:
            linkedList += (str(n_act.data) + ", ") if n_act.next is not None else (str(n_act.data) + ".")
            n_act = n_act.next

        return linkedList
    
    def __len__(self) -> int:
        return self.len
    

    def append(self, x: Any) -> None:
        """ 
          Agrega un elemento al final de la lista. 
        """

        new_node = _Node(x)

        if(self.first is None):

            self.first = new_node
        else:
            
            n_act = self.first

            while n_act.next is not None:

                n_act = n_act.next

            
            n_act.next = new_node
        
        self.len += 1
        

    def insert(self,  i: int, x: Any) -> None:
        """
          Inserta el elemento x en la posición i.
        Si la posición es inválida, imprime un error y retorna inmediatamente.
        """

        if( i < 0 or i > self.len):
            print("Posicion invalida.")
            return
        
        new_node = _Node(x)

        if(i == 0):
            new_node.next = self.first
            self.first = new_node

        else:
            n_prev = self.first

            for _ in range(1, i):
                n_prev = n_prev.next

            new_node.next = n_prev.next
            n_prev.next = new_node
        
        self.len += 1
    
    def pop(self, i: int | None = None) -> Any:
        """
          Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se muestra un mensaje de error y se
        retorna inmediatamente. Si no se recibe la posición, devuelve el
        último elemento.
        """

        if(i is None):
            i = self.len - 1

        if(i < 0 or i >= self.len):
            print("Posicion invalida.")
            return
        
        if(i == 0):
            data: Any = self.first.data
            self.first = self.first.next

        else:
            n_prev = self.first
            n_act = self.first.next

            for _ in range(1, i):
                n_prev = n_prev.next
                n_act = n_act.next

            data: Any = n_act.data
            n_prev.next = n_act.next


        self.len -= 1
        return data
    
    def remove(self, x: Any) -> None:
        """
          Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, imprime un mensaje de error y retorna
        inmediatamente.
        """
        if(self.len == 0):
            print("Lista vacia.")
            return
        
        if(self.first.data == x):

            self.first = self.first.next
        else:
            n_prev = self.first
            n_act = self.first.next

            while n_act is not None and n_act.data != x:

                n_prev = n_act
                n_act = n_act.next
            
            if(n_act is None):
                print("El valor no esta en la lista.")
                return
            
            n_prev.next = n_act.next
            
        self.len -= 1
    
    def index(self, x: Any) -> int | None:
        """         
          Devuelve la posición de la primera aparición de x en la lista 
        (si x no se encuentra presente, imprimirá un error y detendrá la ejecución inmediatamente.) 
        """
        
        pos = 0
        n_act = self.first

        while n_act is not None:

            if(n_act.data == x):
                return pos
            pos += 1
            n_act = n_act.next


        print(f"Error: {x} no se encuentra en la lista.")
        return
    
    def extend(self, newList: 'LinkedList') -> None:
        """
        Ejercicio 2

          Agregue a ListaEnlazada un método extend que reciba una ListaEnlazada y agregue a la lista actual
        los elementos que se encuentran en la lista recibida. ¿Puede estimar la complejidad de este método?
        """
        n_act = newList.first

        while n_act is not None:

            data = n_act.data

            self.append(data)

            n_act = n_act.next
    
    def remove_all(self, element: Any) -> int:
        """
        Ejercicio 3

          Implemente el método remover_todos(elemento) de ListaEnlazada, que recibe un elemento y remueve de la lista todas las apariciones del mismo, devolviendo la cantidad de elementos removidos. La
        lista debe ser recorrida una sola vez.
        """
        itemRemoved: int = 0

        while self.first is not None and self.first.data == element:

            self.first = self.first.next
            itemRemoved += 1

        if(self.first is None):
            return itemRemoved
        
        n_prev = self.first
        n_act = self.first.next

        while n_act is not None:

            data = n_act.data

            if(data == element):
                n_prev.next = n_act.next
                itemRemoved += 1
            else:

                n_prev = n_prev.next
            n_act = n_prev.next

        return itemRemoved
        # Version profe:
        """
        Si bien en el caso anterior recorremos la lista una vez
        tenemos que usar dos whiles.

        El profe propuso inicializar n_prev = None para solo utilizar uno.
        """

    def duplicate(self, element: Any) -> None:
        """       
        Ejercicio 4

          Implemente el método duplicar(elemento) de ListaEnlazada, que recibe un elemento y duplica
        todas las apariciones del mismo.

          En este caso no voy a usar el insert...
        """
        n_act = self.first

        while n_act is not None:

            if(n_act.data == element):

                new_node = _Node(element)

                n_next = n_act.next
                n_act.next = new_node

                new_node.next = n_next

                n_act = n_act.next.next
            else:
                n_act = n_act.next 

    def invert(self) -> None:
        """
        Ejercicio 5
        
          Escriba un método de la clase ListaEnlazada que invierta el orden de la lista (es decir, el primer
        elemento queda como último y viceversa).
        """
        n_prev = None
        n_act = self.first
        
        while n_act is not None:

            next_node = n_act.next

            n_act.next = n_prev

            n_prev = n_act

            n_act = next_node
        
        self.first = n_prev







# Ejercicio 1

""" linkedList = LinkedList()
linkedList.insert(0, 3)
linkedList.insert(0, 5)
linkedList.insert(0, 8)
linkedList.append(89)

print(linkedList)
print(linkedList.index(3))
linkedList.remove(3)
print(linkedList) """

# Ejercicio 2

""" linkedList1 = LinkedList()
linkedList1.insert(0, 3)
linkedList1.insert(0, 2)
linkedList1.insert(0, 1)
linkedList2 = LinkedList()
linkedList2.insert(0, 6)
linkedList2.insert(0, 5)
linkedList2.insert(0, 4)
print(f'linkedList1: {linkedList1}')
print(f'linkedList2: {linkedList2}')

linkedList1.extend(linkedList2) #Importante en el motodo extend crear un nuevo nodo para no vincular las dos listas



# Ejemplo:

#  Eliminar el ultimo nodo de linkedList2 no afecta
# a linkedList1 extends linkedList2 porque
# se crearon nuevos nodos al hacerse append.

linkedList2.pop() 
print(f'linkedList1 extends linkedList2: {linkedList1}')
print(f'linkedList2: {linkedList2}') """

# Ejercicio 3
""" linkedList1 = LinkedList()
linkedList1.insert(0, 1)
linkedList1.insert(0, 1)
linkedList1.insert(0, 1)
linkedList1.insert(0, 3)
linkedList1.insert(0, 2)
linkedList1.insert(0, 1)
linkedList1.insert(0, 6)
linkedList1.insert(0, 1)
linkedList1.insert(0, 1)
linkedList1.insert(0, 4)
linkedList1.insert(0, 1)
linkedList1.insert(0, 1)
linkedList1.insert(0, 1)

print(linkedList1)
print(linkedList1.remove_all(1))
print(linkedList1) """

# Ejercicio 4
""" linkedList1 = LinkedList()
linkedList1.insert(0, 8)
linkedList1.insert(0, 2)
linkedList1.insert(0, 8)
linkedList1.insert(0, 8)
linkedList1.insert(0, 5)
linkedList1.insert(0, 1)


print(linkedList1)
linkedList1.duplicate(8)
print(linkedList1) """

# Ejercicio 5

""" linkedList1 = LinkedList()
linkedList1.insert(0, 1)
linkedList1.insert(0, 1)
linkedList1.insert(0, 3)
linkedList1.insert(0, 2)
linkedList1.insert(0, 1)
linkedList1.insert(0, 6)
linkedList1.insert(0, 1)
linkedList1.insert(0, 1)
linkedList1.insert(0, 4)
linkedList1.insert(0, 1)
linkedList1.insert(0, 1)
linkedList1.insert(0, 1)

print(linkedList1)
linkedList1.invert()
print(linkedList1) """

# Ejercicio 6

class _DoubleNode:

    def __init__(self, data: Any = None, next: '_DoubleNode' = None, prev: '_DoubleNode' = None) -> None:

        self.data: Any = data
        self.next: _DoubleNode = next
        self.prev: _DoubleNode = prev

    def __str__(self) -> str:

        return str(self.data)
    

        

class DoublyLinkedList:

    def __init__(self) -> None:

        self.first: _DoubleNode | None = None
        self.last: _DoubleNode | None = None
        self.len = 0

    def __str__(self) -> str:
        
        n_act = self.first

        if(n_act is None):
            return str(None)
        
        linkedList: str = ''
        
        while n_act is not None:
            linkedList += f"{n_act.data}, " if n_act.next is not None else f"{n_act.data}."
            n_act = n_act.next

        return linkedList



    def __len__(self) -> int:
        return self.len

    def append(self, x: Any) -> None:

        new_node = _DoubleNode(x)

        if(self.first is None and self.last is None):

            self.first = new_node

            self.last = new_node
        else:
            self.last.next = new_node

            new_node.prev = self.last
            self.last = new_node

        self.len += 1
            

    def insert(self, i: int, x: Any) -> None:

        if(i < 0 or i > self.len):
            print("Posicion Invalida.")
            return
        
        new_node = _DoubleNode(x)

        if(i == 0):

            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node

        elif(i == self.len):

            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
        
        else:

            n_prev = self.first

            for _ in range(1, i):

                n_prev = n_prev.next

            new_node.prev = n_prev
            new_node.next = n_prev.next
            n_prev.next.prev = new_node
            n_prev.next = new_node

        self.len += 1


            
            
            




            
            

    def pop(self, x) -> Any:
        pass

# Implementar raise ValueError


doubleLinkedList = DoublyLinkedList()


doubleLinkedList.append(1)
doubleLinkedList.append(2)
doubleLinkedList.append(5)
doubleLinkedList.append(79)


#print(doubleLinkedList)

doubleLinkedList.insert(3, 7)

print(doubleLinkedList)

class Stack:
    """ 
    Representa una pila con operaciones de apilar , desapilar y
    verificar si est á vacía. 
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
        Si la pila esta vac ía, imprime un mensaje de error y retorna
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

class Queue:

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

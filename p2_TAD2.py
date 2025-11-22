from typing import Any

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


class _Node:

    def __init__(self, data: Any | None = None, next: "_Node" = None) -> None:

        self.data = data
        self.next = next

class LinkedStack:

    def __init__(self) -> None:

        self.first: _Node | None = None
        self.len: int = 0
    
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
        
        

s = LinkedStack()
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
#La pila esta vacía

        


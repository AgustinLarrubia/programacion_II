from typing import Any
import math

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

    def filtar_primos(self) -> 'LinkedList | None':
        """
        Ejercicio 7

          Implemente el método filtrar_primos() en la clase ListaEnlazada, que devuelve una nueva lista
        enlazada con los elementos que sean números primos. La nueva lista debe ser construida recorriendo
        los nodos una sola vez (es decir, no se puede llamar a append!). Ejemplo:
          L = 1 -> 5 -> 8 -> 8 -> 2 -> 8
          L.filtrar_primos() -> L2 = 5 -> 2
        """

        if(self.first is None):
            return None
        
        new_list: 'LinkedList' = LinkedList()
        n_act = self.first

        while n_act is not None:

            data = n_act.data
            if isinstance(data, int) and es_primo(data):

                new_node = _Node(data)

                if(len(new_list) == 0):

                    new_list.first = new_node
                    last_node = new_list.first
                else:

                    last_node.next = new_node
                    last_node = last_node.next 

                new_list.len += 1   

            n_act = n_act.next

        return new_list
            






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
            return None
        
        new_node = _DoubleNode(x)

        if(i == 0):

            if(self.first is None):

                self.first = new_node
                self.last = new_node
            else:
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


    def pop(self, i: int | None = None) -> Any:

        if(i is None):
            i = self.len - 1

        if(i < 0 or i >= self.len):
            print("Posicion invalida")
            return
        
        if(self.len == 1):

            data: Any = self.first.data
            self.first = None
            self.last = None

            self.len -= 1
            return data
        
        if(i == 0):

            data: Any = self.first.data
            self.first = self.first.next
        elif(i == self.len - 1):

            data: Any = self.last.data
            self.last.prev.next = None
            self.last = self.last.prev
        else:

            n_act = self.first.next
            
            for _ in range(1, i):
                n_act = n_act.next

            data: Any = n_act.data
            n_act.prev.next = n_act.next
            n_act.next.prev = n_act.prev

        
        self.len -= 1
        return data
            

    def remove(self, x: Any) -> None:
        
        if(self.first is None):

            return None
        
        n_act = self.first
    
        while n_act is not None and n_act.data != x:

            n_act = n_act.next

        if(n_act is None):
            print("El valor no esta en la lista.")
            return
        
        hasNext: bool = n_act.next is not None
        hasPrev: bool = n_act.prev is not None

        if(not hasNext and not hasPrev):
            self.first = None
            self.last = None
            self.len -= 1
            return

        if(hasNext and not hasPrev):
            self.first = self.first.next
            self.first.prev = None
            self.len -= 1
            return

        if(not hasNext and hasPrev):
            self.last = self.last.prev
            self.last.next = None
            self.len -= 1
            return

        n_act.prev.next = n_act.next
        n_act.next.prev = n_act.prev

        self.len -= 1


    def index(self, x: Any) -> int | None:

        if(self.first is None):
            print(f"Error: {x} no se encuentra en la lista.")
            return None
        
        pos: int = 0
        n_act = self.first
    
        while n_act is not None:

            if(n_act.data == x):
                return pos
            pos += 1
            n_act = n_act.next

        print("El valor no esta en la lista.")
        return
            

# Implementar raise ValueError


""" doubleLinkedList = DoublyLinkedList()


doubleLinkedList.append(1)
doubleLinkedList.append(2)
doubleLinkedList.append(5)
doubleLinkedList.append(79)


print(doubleLinkedList)

doubleLinkedList.insert(0, 7)
popped = doubleLinkedList.pop(3)
print(popped)
print(doubleLinkedList) """


# Ejercicio 7
def es_primo(n: int) -> bool:

    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    limite = int(math.sqrt(n)) + 1
    
    for i in range(3, limite, 2):
        if n % i == 0:
            return False 
            
    return True

""" linkedList1 = LinkedList()
linkedList1.append(1)
linkedList1.append(5)
linkedList1.append(8)
linkedList1.append(8)
linkedList1.append(2)
linkedList1.append(8)
linkedList1.append(7)

print(linkedList1)
primos = linkedList1.filtar_primos()
print(primos) """

# Ejercicio 8
def  insertar_palabra_despues(lista: LinkedList,palabra_objetivo: str, palabra_insertar: str) -> 'LinkedList | None':
    """
    Ejercicio 8

      Se tiene una lista enlazada L de palabras, y se quiere insertar la palabra “mundo” despues de
    todas las apariciones de la palabra “hola”. Defina una función insertar_palabra_despues(lista,
    palabra_objetivo, palabra_insertar) que dada una lista, una palabra objetivo (hola) y una palabra
    a insertar (mundo) devuelva una nueva lista enlazada donde se agrega la nueva palabra cada vez que se
    encuentra la palabra objetivo.
    Por ejemplo:
    L = “Planificacion” -> “Hola” -> “de” -> “Trece”
    insertar_palabra_despues(L, “Hola”, “Mundo”) -> L2 = “Planificacion” -> “Hola” -> “Mundo” ->
    “de” -> “Trece”
    """
    if(lista.first is None):
        print("Lista vacia.")
        return None
    
    new_list: 'LinkedList' = LinkedList()
    n_act = lista.first

    while n_act is not None:

        data = n_act.data

        if data == palabra_objetivo:
            old_node = _Node(palabra_objetivo)
            new_node = _Node(palabra_insertar)
            if len(new_list) == 0:
                new_list.first = old_node
                new_list.first.next = new_node
                last_node = new_list.first.next
            else:
                last_node.next = old_node
                last_node.next.next = new_node
                last_node = last_node.next.next
            
            new_list.len += 2
        else:
            new_node = _Node(data)
            if len(new_list) == 0:
                new_list.first = new_node
                last_node = new_list.first   
            else:
                last_node.next = new_node
                last_node = last_node.next
            new_list.len += 1

        n_act = n_act.next

    return new_list

""" linkedList1 = LinkedList()

linkedList1.append("Primero")
linkedList1.append("Hola")
linkedList1.append("Segundo")
linkedList1.append("Francia")

print(linkedList1)
listaModificada = insertar_palabra_despues(linkedList1, "Hola", "Mundo")
print(listaModificada) """

# Ejercicio 9

def eliminar_palabras_con(lista: LinkedList, char: str) -> 'LinkedList | None':
    """
    Ejercicio 9

      Se tiene una lista enlazada L de palabras, y se desea eliminar todas las palabras que contengan una
    ñ. Defina una función eliminar_palabras_con(lista, carácter) que dada una lista y un carácter,
    devuelva una nueva lista enlazada donde se eliminaron las apariciones de palabras conteniendo dicho
    carácter.
    Por ejemplo:
    L = “Ocho” -> “Veinte” -> “Veinticuatro” -> “Hoy”
    eliminar_palabras_con(L, “V”) -> L2 = “Ocho” -> “Hoy”
    """
    if(lista.first is None):
        print("Lista Vacia.")
        return None
    
    new_list = LinkedList()
    n_act = lista.first

    while n_act is not None:
        dato = n_act.data
        if isinstance(dato, str) and char not in dato:
            new_node = _Node(dato)
            if new_list.len == 0:

                new_list.first = new_node
                last_node = new_list.first
            else:

                last_node.next = new_node
                last_node = last_node.next
        
            new_list.len += 1
        n_act = n_act.next
    
    return new_list
            

linkedList1 = LinkedList()

linkedList1.append("Primero")
linkedList1.append("Hola")
linkedList1.append("Segundo")
linkedList1.append("Francia")

print(linkedList1)
listaModificada = eliminar_palabras_con(linkedList1, "a")
print(listaModificada)

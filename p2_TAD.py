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

        if(i < self.len or i > self.len):
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
        """Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, imprime un mensaje de error y retorna
        inmediatamente.
        """
        if(self.len == 0):
            print("Lista vacia.")
            return
        
        if(self.first.data == x):
            print(self.first.data)
            self.first = self.first.next
            self.len -= 1
            return
        else:
            n_ant = self.first
            n_act = self.first.next

            for _ in range(1, self.len):

                if(n_act.data == x):
                    print(n_act.data)
                    n_ant.next = n_act.next
                    self.len -= 1
                    return
                n_ant = n_act
                n_act = n_act.next

        print(f"{x} no se encuentra en la lista")


linkedList = LinkedList()
linkedList.insert(0, 3)
linkedList.insert(0, 5)
linkedList.insert(0, 8)

linkedList.remove(83)
# Esta no es la version final de LinkedList, falta refactorizar y testear

from operator import le
from typing import Any

""" class Tree:

    def __init__(self, cargo, left: "Tree" = None, right: "Tree" = None) -> None:

        self.cargo = cargo
        self.left = left
        self.right = right """



"""
Ejercicio 1

    Dibuje ejemplos de árboles en su hoja con las siguientes características, luego, construya sus ejemplos
    en Python.
        1. Un árbol con únicamente su raíz.
        2. Un árbol parecido a una lista de largo 3.
        3. Un árbol completo de altura 1.
        4. Un árbol vacío ¿Puede hacerlo?
"""

"""
1.
    2
"""
""" t1 = Tree(1) """

"""
2.
    2
     \
      4
       \
        5
"""

""" r2 = Tree(5)
r1 = Tree(4,None,r2)
t2 = Tree(2, None, r1) 
 """
"""
3.
    5
  /   \
 3     8 
"""

""" 
l1 = Tree(3)
r1 = Tree(8)
t3 = Tree(5,l1,r1) 
"""

"""
4.
"""

t4 = None # ? consultar profe


class Tree:
    """
    Ejercicio 2

        Implemente en la clase Tree los siguiente métodos:

    Ayuda: pensar que cada árbol tiene a su izquierda y derecha objetos árboles como sus hijos.
        • nodos: devuelve la cantidad de nodos del árbol
        • menor_mayor: devuelve el menor y el mayor elemento del árbol en una tupla.
        • buscar: busca si un elemento está o no en el árbol.
        • altura: calcula la altura del árbol, la distancia desde la raíz hasta la hoja más lejana
    """
    def __init__(self, cargo: Any, left: "Tree" = None, right: "Tree" = None) -> None:

        self.cargo: Any = cargo
        self.left: Tree = left
        self.right: Tree = right
    
    def nodos(self) -> int:
        
        total: int = 1

        if self.left is not None:
            total += self.left.nodos()

        if self.right is not None:
            total += self.right.nodos()
        
        return total

    def menor_mayor(self) -> tuple[Any, Any]:

        menor: Any = self.cargo
        mayor: Any = self.cargo
        print(self.cargo)

        if self.left is not None:
            menor_izq, mayor_izq = self.left.menor_mayor()

            if menor_izq < menor: 
                menor = menor_izq
            if mayor_izq > mayor: 
                mayor = mayor_izq

        if self.right is not None:
            menor_der, mayor_der = self.right.menor_mayor()

            if menor_der < menor:
                menor = menor_der
            if mayor_der > mayor:
                mayor = mayor_der
        
        return (menor, mayor)

    def buscar(self, x: Any) -> bool:
        
        if self.cargo == x:
            return True
        
        if self.left is not None and self.left.buscar(x):
            return True
        
        if self.right is not None and self.right.buscar(x):
            return True
        
        return False

    def altura(self) -> int:
        
        altura_left: int = -1
        altura_right: int = -1

        if self.left is not None:
            altura_left = self.left.altura()
        if self.right is not None:
            altura_right = self.right.altura()
        
        return 1 + max(altura_left, altura_right)




""" l3 = Tree(5)
r3 = Tree(92,Tree(3,Tree(3,Tree(3)),Tree(3)))
t3 = Tree(2, l3, r3) 
l2 = Tree(25)
r2 = Tree(9)
t2 = Tree(2, l2, r2) 
t1 = Tree(2, t2, t3)  """
#print(t1.menor_mayor())
#print(t1.buscar(92))
#print(t1.altura())

"""
Ejercicio 3
    a. Pensar y dibujar un ejemplo de árbol en papel, escribir los resultados de PreOrder, InOrder y
    PostOrder.
    
    b. Implementar los recorridos PreOrder, InOrder y PostOrder como funciones recursivas, verificar
    sus resultados.

    c. Implementar los recorridos PreOrder, InOrder y PostOrder como funciones iterativas, verificar
    sus resultados.

    Ayuda: Para las versiones iterativas, necesitará utilizar una Pila como estructura de datos auxiliar.
    Puede importar una implementación cualquiera de Pila que haya realizado en Prácticas anteriores.
"""

# b


r"""
Ejemplo Arbol:
                4
            /       \
            2         67
         /     \     /   \
        12      3   32   6
         \    /        /  \
         23  9       65    21
"""

""" t6 = Tree(12,None,Tree(23))
t5 = Tree(3,Tree(9))
t4 = Tree(2,t6,t5)
t3 = Tree(6,Tree(65),Tree(21))
t2 = Tree(67,Tree(32),t3)
t = Tree(4,t4,t2) """

def recorrer_pre_rec(tree: Tree) -> None:

    if tree is None:
        return

    print(tree.cargo, end=" ")

    recorrer_pre_rec(tree.left)
    
    recorrer_pre_rec(tree.right)
    
def recorrer_in_rec(tree: Tree) -> None:

    if tree is None:
        return
    
    recorrer_in_rec(tree.left)

    print(tree.cargo)

    recorrer_in_rec(tree.right)


def recorrer_post_rec(tree: Tree) -> None:

    if tree is None:
        return
    
    recorrer_post_rec(tree.left)

    recorrer_post_rec(tree.right)

    print(tree.cargo)

#recorrer_pre_rec(t)
#recorrer_in_rec(t)
#recorrer_post_rec(t)

def recorrer_pre_it(tree: Tree) -> None:
    if tree is None:
        return

    stack = [tree]

    while len(stack) > 0:

        node = stack.pop()
        print(node.cargo)

        if node.right is not None:
            stack.append(node.right)
        
        if node.left is not None:
            stack.append(node.left)
            
def recorrer_in_it(tree: Tree) -> None:
    
    if tree is None:
        return 
    
    stack = []
    current = tree

    while current is not None or len(stack) > 0:

        while current is not None:
            stack.append(current)
            current = current.left
        
        current = stack.pop()

        print(current.cargo)

        current = current.right
        

def recorrer_post_it(tree: Tree) -> None:
    if tree is None:
        return

    stack = [tree]
    salida = []

    while len(stack) > 0:

        node = stack.pop()
        salida.append(node.cargo)

        if node.left is not None:
            stack.append(node.left)

        if node.right is not None:
            stack.append(node.right)
        
    while len(salida) > 0:
        print(salida.pop())

""" t6 = Tree(12,None,Tree(23))
t5 = Tree(3,Tree(9))
t4 = Tree(2,t6,t5)
t3 = Tree(6,Tree(65),Tree(21))
t2 = Tree(67,Tree(32),t3)
t = Tree(4,t4,t2) """

#recorrer_pre_it(t)
#recorrer_in_it(t)
#recorrer_post_it(t)

def copy_tree(tree: Tree) -> Tree:
    """
    Ejercicio 4
        Escriba una función copiar que reciba un árbol y devuelva un nuevo árbol idéntico al original
    """
    if tree is None:
        return None
    
    return Tree(tree.cargo, copy_tree(tree.left), copy_tree(tree.right))

t6 = Tree(12,None,Tree(23))
t5 = Tree(3,Tree(9))
t4 = Tree(2,t6,t5)
t3 = Tree(6,Tree(65),Tree(21))
t2 = Tree(67,Tree(32),t3)
t = Tree(4,t4,t2)

""" t_copy = copy_tree(t)
recorrer_pre_rec(t)
recorrer_pre_rec(t_copy) """

def invertir(tree: Tree) -> Tree:
    """
    Ejercicio 5

        Escriba una función invertir que reciba un árbol binario e intercambie los hijos derechos por los hijos
    izquierdos en todos los nodos.
    """
    if tree is None:
        return None
    
    return Tree(tree.cargo, invertir(tree.right) , invertir(tree.left))

""" t_invertido = invertir(t)
recorrer_pre_rec(t)
print('\n')
recorrer_pre_rec(t_invertido)
print('\n') """

def sumatoria(tree: Tree) -> float:
    """
    Ejercicio 6
        Escriba una función sumatoria que reciba un árbol binario que contiene números en sus nodos y
    devuelva la suma de todos los nodos.
    """
    if tree is None:
        return 0
    
    return tree.cargo + sumatoria(tree.left) + sumatoria(tree.right)

""" sumatoria_t = sumatoria(t)
print(sumatoria_t)
 """

def sumatoria_rango(tree_A: Tree, M: int, inicio: int, final: int) -> float:
    """
    Ejercicio 7

        Escriba una función sumatoria_rango que reciba un árbol binario A cuyos nodos contienen números y
    que dado un entero M, una clave inicial inicio y una clave final final, calcula la suma de todos los
    números del árbol que se encuentren entre inicio y final, a lo sumo hasta el nivel M.
    """

    if tree_A is None or M == -1:
        return 0
    
    cargo = 0
    
    if tree_A.cargo >= inicio and tree_A.cargo <= final:
        cargo = tree_A.cargo 

    return cargo + sumatoria_rango(tree_A.left,M - 1, inicio, final) + sumatoria_rango(tree_A.right, M - 1, inicio, final)


""" sumatoria_rango = sumatoria_rango(t, 3, 2, 20)
print(sumatoria_rango) """

# Arboles Binarios de Busqueda (BST)

r"""
Ejercicio 8
    Dibuje un árbol binario de búsqueda de palabras, con al menos 5 palabras, utilizando orden de
diccionario (lexicográfico). Acomódelo como más le guste, mientras sea correcto. Luego indique en qué
lugar del árbol se insertaría la palabra python.

 
        "No tengo muchas ganas de programar hoy en"
        

              No                      No
           /      \                /      \
      muchas      tengo         muchas      tengo
      /           /              /           /
    ganas    programar         ganas    programar
    /   \                      /   \         \
   de   hoy                  de   hoy       Python
    \                         \
    en                        en
    
"""

class BSTree(Tree):
    """
    Ejercicio 9

        Utilizando la misma clase Tree de la sección anterior, implemente otra clase llamada BSTree que herede
    de esta, reimplemente los métodos menor_mayor, buscar e implemente un nuevo método llamado
    insertar que inserte un elemento.

    Ayuda: puede optar por definir métodos menor y mayor internamente por separado para hacer la
    implementación más sencilla, pero no es estrictamente necesario.
    """

    def __init__(self, cargo: Any, left: "BSTree" = None, right: "BSTree" = None) -> None:

        super().__init__(cargo)
        self.left = left
        self.right = right

    
    def menor(self) -> Any:
        
        if self.left is not None:
            return self.left.menor()
        
        return self.cargo
        
    def mayor(self) -> Any:

        if self.right is not None:
            return self.right.mayor()
        
        return self.cargo

    def menor_mayor(self) -> tuple[Any, Any]:            
        
        return (self.menor(),self.mayor())

    def buscar(self, x: Any) -> bool:
        
        if self.cargo == x:
            return True
        
        if x < self.cargo:

            if self.left is not None and self.left.buscar(x):
                return True
        
        elif x > self.cargo:
            
            if self.right is not None and self.right.buscar(x):
                return True
        
        return False

    def insert(self, x: Any) -> None:

        if self.cargo < x:
            if self.right is None:
                self.right = BSTree(x)
            else:
                self.right.insert(x)
        elif self.cargo > x :
            if self.left is None:
            
                self.left = BSTree(x)
            else:
                self.left.insert(x)
        else:
            print(f"{x} ya se encuentra en el arbol.")
            return None
        
bstree = BSTree(4)

bstree.insert(5)
bstree.insert(2)
bstree.insert(7)
bstree.insert(9)
bstree.insert(12)
bstree.insert(4)
bstree.insert(1)
bstree.insert(3)
print(bstree.menor_mayor())
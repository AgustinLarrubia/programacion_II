class Tree:

    def __init__(self, cargo, left: "Tree" = None, right: "Tree" = None) -> None:

        self.cargo = cargo
        self.left = left
        self.right = right



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



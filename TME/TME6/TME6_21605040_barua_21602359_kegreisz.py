"""
Exercice: TME6
Nom: BARUA et KEGREISZ
Date creation: 01/10/2026
"""

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild= None

#---------ex_1-------------

def insert(root: BinaryTreeNode, value : int):
    """ Une fonction récursive qui prend en paramètre un arbre 
        et une valeur et insère le noeud correspondant à 
        la nouvelle donnée.

    Args:
        root (BinaryTreeNode): un arbre binaire
        value (int): une valeur à insérer

    Returns :
        Renvoie l'arbre avec les éléments insérés.
    """

    if root is None:
        return BinaryTreeNode(value)
    elif value < root.data:
        root.leftChild = insert(root.leftChild, value)
    elif value > root.data:
        root.rightChild = insert(root.rightChild, value)
    return root


# Construction de l’arbre de l’ ́enonc ́e :
root= insert(None,13)
insert(root,10)
insert(root,10)
insert(root,17)
insert(root,8)
insert(root,12)
insert(root,9)
insert(root,23)
insert(root,20)
insert(root,15)
assert root.data == 13
assert root.leftChild.data == 10
assert root.leftChild.rightChild.data == 12

#---------ex_2-----------
#-------Question_1-------
def affiche_arbre(node : BinaryTreeNode):
    if node is None:
        return 
    print(node.data, end = " ")
    affiche_arbre(node.leftChild)
    affiche_arbre(node.rightChild)

# affiche_arbre(root)

#-------Question_2-------
def affiche_arbre(node : BinaryTreeNode):
    if node is None:
        return 
    affiche_arbre(node.leftChild)
    print(node.data, end = " ")
    affiche_arbre(node.rightChild)

# affiche_arbre(root)

#---------ex_3-----------
def cherche_element(root: BinaryTreeNode, value : int) -> bool:
    if root is None:
        return None
    elif  root.data == value:
        return True
    elif root.data < value:
        return cherche_element(root.rightChild, value)
    else:
        return cherche_element(root.leftChild, value)

#--------ex_4-------------

def minimale(node : BinaryTreeNode):
    while node.leftChild is not None:
        node = node.leftChild
    return node.data

print(minimale(root))

def maximale(node : BinaryTreeNode):
    while node.rightChild is not None:
        node = node.rightChild
    return node.data

print(maximale(root))

#---------ex_5-----------
#--------Question_1------

"""
4(2(1, 3), 8(6(5, 7), 9(-, 10)))

Il est équilibré en chaque nœud, les hauteurs des sous-arbres diffèrent
 d'au plus 1. Mais, il n'est pas parfaitement équilibré. 
 Par exemple: en 8, le sous-arbre gauche a 3 nœuds et le droit en a 2.
 Et en 9 le sous-arbre gauche est vide alors que le droit en a 1.
"""
#---------Question_2-------
def hauteur(node: BinaryTreeNode) -> int:
    if node is None:
        return 0
    return 1 + max(hauteur(node.leftChild), hauteur(node.rightChild))

#---------Question_3-------
def rotation_droite(node : BinaryTreeNode) -> BinaryTreeNode:
    gauche = node.leftChild
    node.leftChild = gauche.rightChild
    gauche.rightChild = node
    return gauche

#---------Question_4-------
def rotation_gauche(node: BinaryTreeNode) -> BinaryTreeNode:
    droite = node.rightChild
    node.rightChild = droite.leftChild
    droite.leftChild = node
    return droite

#---------Question_5-------
def equilibre(node: BinaryTreeNode, value: int) -> BinaryTreeNode:
    if node is None:
        return BinaryTreeNode(value)
    if value < node.data:
        node.leftChild = equilibre(node.leftChild, value)
    elif value > node.data:
        node.rightChild = equilibre(node.rightChild, value)
    else:
        return node
    
    gauche = node.leftChild
    droite = node.rightChild
    
    difference = hauteur(gauche) - hauteur(droite)
    
    if difference == 2:
        g = gauche.leftChild
        d = gauche.rightChild
        if hauteur(g) < hauteur(d):
            node.leftChild = rotation_gauche(gauche)
        return rotation_droite(node)
    if difference == -2:
        g = droite.leftChild
        d = droite.rightChild
        if hauteur(droite.rightChild) < hauteur(droite.leftChild):
            node.rightChild = rotation_droite(droite)
        return rotation_gauche(node)
    return node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild= None
        
def insert(node : BinaryTreeNode, value: int) -> BinaryTreeNode:
    if node is None:
        return BinaryTreeNode(value)
    elif value < node.data:
        node.leftChild = insert(node.leftChild, value)
    elif value > node.data:
        node.rightChild = insert(node.rightChild, value)
    return node
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
""" def taille(node: BinaryTreeNode) -> int:
    if node == None:
        return 0
    else: 
        return 1+taille(node.left)+taille(node.right) """

def affica_arbre(node: BinaryTreeNode) -> int:
    if node is None:
        return 
    affica_arbre(node.leftChild)
    print(node.data)
    affica_arbre(node.rightChild)
    
#affica_arbre(root)   

def cherche_elem(node: BinaryTreeNode, target) -> int:
    if node is None:
            return None
    elif node.data == target:
        return True
    elif node.data > target:
        return cherche_elem(node.leftChild, target)
    else:
        return cherche_elem(node.rightChild, target)
        
print(cherche_elem(root, 20))


def mini(node: BinaryTreeNode):
    current = node
    while current.leftChild is not None:
        current = current.leftChild
    return current.data

print(mini(root))

def maxi(node: BinaryTreeNode):
    current = node
    while current.rightChild is not None:
        current = current.rightChild
    return current.data
print(maxi(root))

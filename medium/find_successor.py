# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def getLeftMostValue(root):
    if root.left is None:
        return root
    return getLeftMostValue(root.left)
    
def getSuccessor(root:BinaryTree):
    if root.parent is None:
        return None
    if root.parent.left == root:
        return root.parent
    return getSuccessor(root.parent)

def findSuccessor(tree, node):
    if tree is None:
        return None
	
    if node.right is not None:
        return getLeftMostValue(node.right)
    return getSuccessor(node)
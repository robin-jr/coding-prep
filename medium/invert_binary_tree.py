

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def rotateNode(root):
    if root is None:
        return 
    
    root.left,root.right=root.right,root.left
    
def invertBinaryTree(tree):
    if tree is None:
        return 
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    rotateNode(tree)
    return tree
        

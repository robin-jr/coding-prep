# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def helper(array):
    tree= BST(array[0])
    rightChildIdx=None
    for i in range(1,len(array)):
        if array[i]>=tree.value:
            rightChildIdx=i
            break
            
    if rightChildIdx is not None:
        tree.right=helper(array[rightChildIdx:])

    leftChildIdx=1 if (len(array)>1 and array[1]<array[0]) else None
    if leftChildIdx is not None:
        tree.left=helper(array[leftChildIdx:rightChildIdx])
    return tree
        
def reconstructBst(preOrderTraversalValues):
    tree = helper(preOrderTraversalValues)
    return tree
    

    

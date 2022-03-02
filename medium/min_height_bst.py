def minHeightBst(array,tree=None):
    if len(array) == 0:
        return
    middleIndex=len(array)//2
    middleValue=array[middleIndex]
    if tree is None:
        tree = BST(middleValue)
    else:
        tree.insert(middleValue)
    minHeightBst(array[:middleIndex],tree)
    minHeightBst(array[middleIndex+1:],tree)
    return tree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

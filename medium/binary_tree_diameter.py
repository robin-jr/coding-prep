# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self,maxHeight=0):
        self.maxHeight = maxHeight

def height(tree,treeInfo: TreeInfo):
    if tree is None:
        return -1
    leftHeight = height(tree.left,treeInfo)
    rightHeight = height(tree.right,treeInfo)
    treeInfo.maxHeight = max(leftHeight+ rightHeight+2,treeInfo.maxHeight)
    print(leftHeight,rightHeight,treeInfo.maxHeight)
    return max(leftHeight,rightHeight)+1

def binaryTreeDiameter(tree):
    treeInfo = TreeInfo()
    height(tree,treeInfo)
    return treeInfo.maxHeight
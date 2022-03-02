class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self,balanced=True):
        self.balanced = balanced
        
def height(tree,treeInfo: TreeInfo):
    if tree is None or not treeInfo.balanced:
        return -1
    leftHeight = height(tree.left,treeInfo)
    rightHeight = height(tree.right,treeInfo)
    if abs(leftHeight - rightHeight)>1:
        treeInfo.balanced=False
    return max(leftHeight,rightHeight)+1

def heightBalancedBinaryTree(tree):
    treeInfo =TreeInfo()
    height(tree,treeInfo)
    return treeInfo.balanced

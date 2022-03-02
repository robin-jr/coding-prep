class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self,rootIdx):
        self.rootIdx = rootIdx

def helper(treeInfo: TreeInfo,leftBound,rightBound, array):
    if len(array)==0 or len(array)==treeInfo.rootIdx: return None
    currentValue = array[treeInfo.rootIdx]
    tree = None
    if leftBound<=currentValue and currentValue<rightBound:
        treeInfo.rootIdx+=1
        tree = BST(currentValue)
        tree.left= helper(treeInfo,leftBound,currentValue, array)
        tree.right= helper(treeInfo,currentValue,rightBound, array)
    return tree
    
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    tree = helper(treeInfo,float("-inf"),float("inf"), preOrderTraversalValues)
    return tree

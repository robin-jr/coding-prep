# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getDepth(node):
    depth=0
    currentNode=node
    while currentNode.ancestor is not None:
        depth+=1
        currentNode=currentNode.ancestor
    return depth

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depth1=getDepth(descendantOne)
    depth2=getDepth(descendantTwo)
    while depth1<depth2:
        descendantTwo=descendantTwo.ancestor
        depth2-=1
    while depth1>depth2:
        descendantOne=descendantOne.ancestor
        depth1-=1
    while descendantOne.name != descendantTwo.name:
        descendantOne=descendantOne.ancestor
        descendantTwo=descendantTwo.ancestor
    return descendantOne

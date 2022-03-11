from unicodedata import name


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def bfs(self,array,queue):
        if len(queue) == 0:
            return array
        currentNode=queue.pop(0)
        array.append(currentNode.name)
        for e in currentNode.children:
            queue.append(e)
        self.bfs(array,queue)
        
    def breadthFirstSearch(self, array,queue=[]):
        queue.append(self)
        self.bfs(array,queue)
        return array

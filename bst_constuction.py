class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self is None:
            return BST(value)
        if self.value <=value:
            if self.right is None:
                self.right=BST(value)
            else:
                self.right.insert(value)
        if value < self.value:
            if self.left is None:
                self.left=BST(value)
            else:
                self.left.insert(value)
        return self

    def contains(self, value):
        if self.value==value:
            return True
        if self.value<value and self.right is not None:
            return self.right.contains(value)
        if self.value>value and self.left is not None:
            return self.left.contains(value)
        return False

    def remove(self, value,parentNode=None):
        currentNode = self
        while currentNode is not None:
            if currentNode.value<value:
                parentNode=currentNode
                currentNode = currentNode.right
            elif value<currentNode.value:
                parentNode=currentNode
                currentNode = currentNode.left
            else: # Node is found
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value,currentNode)
                elif parentNode is not None:
                    if parentNode.left==currentNode:
                        parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                    elif parentNode.right==currentNode:
                        parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode is None:
                    if currentNode.right is not None:
                        currentNode.value=currentNode.right.value
                        currentNode.left=currentNode.right.left
                        currentNode.right=currentNode.right.right
                    
                    elif currentNode.left is not None:
                        currentNode.value=currentNode.left.value
                        currentNode.right=currentNode.left.right
                        currentNode.left=currentNode.left.left
                break
                
        return self
    
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
    
    def show(self):
        if self is None:
            return
        if self.left is not None:
            self.left.show()
        print(self.value)
        if self.right is not None:
            self.right.show()


x=BST(1)
x.insert(-2)
x.insert(-3)
x.insert(-4)
x.remove(1)
x.show()
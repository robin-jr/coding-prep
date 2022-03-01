# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

no_of_visited_nodes=0
last_visited_value=0

def helper(tree,k):
    global no_of_visited_nodes, last_visited_value
    print(no_of_visited_nodes,last_visited_value)
    if tree is None or k<=no_of_visited_nodes:
        return last_visited_value
    helper(tree.right,k)
    if no_of_visited_nodes<k:
        no_of_visited_nodes+=1
        last_visited_value=tree.value
        helper(tree.left,k)
    return last_visited_value

def findKthLargestValueInBst(tree, k):
    global no_of_visited_nodes, last_visited_value
    no_of_visited_nodes=0
    last_visited_value=0
    return helper(tree,k)
    

def hasCycle(node, edges, visited_nodes=set()):
    if visited_nodes.__contains__(node):
        return True
    visited_nodes.add(node)
    children = edges[node]
    for child in children:
        if hasCycle(child, edges, visited_nodes):
            return True
    visited_nodes=visited_nodes.remove(node)
    return False


def cycleInGraph(edges):
    n = len(edges)
    nodes = [i for i in range(n)]
    for node in nodes:
        if hasCycle(node, edges, set()):
            return True
    return False


edges = [
    [1, 2],
    [2],
    []
]

x = cycleInGraph(edges)
print(x)

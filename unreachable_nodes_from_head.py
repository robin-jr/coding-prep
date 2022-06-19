n,m= map(int,input().split())

d={}

for i in range(m):
    x,y = map(int,input().split())
    d[x] = d.get(x,[]) + [y]
head = int(input())


def fun(queue, visited=set()):
    if not queue: return len(visited)
    currentNode = queue.pop()
    visited.add(currentNode)
    neighbors = d.get(currentNode,[])
    for neighbor in neighbors:
        if neighbor not in visited:
            queue.append(neighbor)
    return fun(queue, visited)
            
x = fun([head])

print(n-x)
    
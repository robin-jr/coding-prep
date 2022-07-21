from functools import cache


def getOdds(n):
    a = []
    for i in range(1,n+1):
        if i%2 != 0: a.append(i)
    return a

def getEvens(n):
    a = []
    for i in range(1,n+1):
        if i%2 == 0: a.append(i)
    return a

@cache
def move(target, power, distance=0,steps=0, direction=1, mm = float("inf")):
    print(target, distance, steps, direction)
    if target == distance : 
        return steps
    if distance - target >= power: 
        return float("inf")
    if distance < 0 : 
        return float("inf")
    if steps > 100 : 
        return float("inf")
    
    r = [float("inf")]
    
    if direction == 1:
        for e in getOdds(power):
            x = move(target, power, distance+e, steps+1, 0, min(r))
            r.append(x)
    elif direction == 0:
        for e in getEvens(power):
            x = move(target, power, distance-e, steps+1, 1, min(r))
            r.append(x)
    # print(r)
    return min(r)

a = [7,9,11]
b = [3,15,5]
c = 2
mins = []

j=1
xx = []
for i in range(len(a)):
    xx.append(move(a[i],b[i]))
    if len(xx)==c: 
        mins.append(min(xx))
        xx = []

# x = move(11,5)
print(mins)
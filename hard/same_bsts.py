def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne)!=len(arrayTwo): return False
    n = len(arrayOne)
    if n==0: return True
    
    if arrayOne[0]!=arrayTwo[0]: return False
    fe = arrayOne[0]
    
    left1 = []
    left2 = []
    right1 = []
    right2 = []
    for i in range(1,n):
        p = arrayOne[i]
        q = arrayTwo[i]
        if p<fe: left1.append(p)
        if q<fe: left2.append(q)
        if p>=fe: right1.append(p)
        if q>=fe: right2.append(q)
    return sameBsts(left1,left2) and sameBsts(right1,right2)


# a1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
# a2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]
a1 = [10, 15, 8, 12, 94, 81, 5, 2, 10]
a2 = [10, 8, 5, 15, 2, 10, 12, 94, 81]

x = sameBsts(a1,a2)
print(x)
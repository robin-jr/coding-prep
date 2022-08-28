from ast import arg


def samebsts1(arrayone, arraytwo):
    if len(arrayone)!=len(arraytwo): return False
    n = len(arrayone)
    if n==0: return True
    
    if arrayone[0]!=arraytwo[0]: return False
    fe = arrayone[0]
    
    left1 = []
    left2 = []
    right1 = []
    right2 = []
    for i in range(1,n):
        p = arrayone[i]
        q = arraytwo[i]
        if p<fe: left1.append(p)
        if q<fe: left2.append(q)
        if p>=fe: right1.append(p)
        if q>=fe: right2.append(q)
    return samebsts1(left1,left2) and samebsts1(right1,right2)

def samebsts(arrayone, arraytwo, i1=0, i2=0, minv=float("-inf"), maxv=float("inf")):
    if i1==-1 or i2==-1: return i1==i2
    if arrayone[i1]!=arraytwo[i2]: return False
    if len(arrayone)!=len(arraytwo): return False
    n = len(arrayone)
    print(arrayone[i1], arraytwo[i2], minv, maxv)
    
    l1 = -1
    for i in range(i1 +1 , n):
        if arrayone[i]<arrayone[i1] and arrayone[i]>=minv: 
            l1 = i; break
    l2 = -1  
    for i in range(i2+1, n):
        if arraytwo[i]<arraytwo[i2] and arraytwo[i]>=minv:
            l2 = i; break
    r1 = -1
    for i in range(i1+1,n):
        if arrayone[i]>=arrayone[i1] and arrayone[i]<maxv:
            r1 = i; break
    r2 = -1
    for i in range(i2+1, n):
        if arraytwo[i]>=arraytwo[i2] and arraytwo[i]<maxv:
            r2 = i; break
    
    return samebsts(arrayone, arraytwo, l1, l2 , minv, arrayone[i1]) and samebsts(arrayone, arraytwo, r1, r2, arrayone[i1], maxv)

a1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
a2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]
# a1 = [10, 15, 8, 12, 94, 81, 5, 2, 10]
# a2 = [10, 8, 5, 15, 2, 10, 12, 94, 81]

x = samebsts(a1,a2)
print(x)
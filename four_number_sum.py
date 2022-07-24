class E():
    def __init__(self, i, j, sum) -> None:
        self.i = i
        self.j = j
        self.sum = sum

    def __str__(self) -> str:
        return f"{self.i} {self.j} {self.sum}"
        
def fourNumberSum(array, targetSum):
    st = []
    n = len(array)
    for i in range(n-1):
        for j in range(i+1,n):
            st.append(E(i,j,array[i]+array[j]))
    
    n = len(st)
    result = set()
    for i in range(n-1):
        for j in range(i+st[i].j+1,n):
            t = [array[st[i].i],array[st[i].j],array[st[j].i],array[st[j].j]]
            t.sort()
            if st[i].sum+st[j].sum == targetSum and len(set(t))==4:
                result.add(tuple(t))
    t = []
    for e in result:
        t.append(list(e))
    
    return t

array = [7, 6, 4, -1, 1, 2]
targetSum = 16
x = fourNumberSum(array,targetSum)
print(x)
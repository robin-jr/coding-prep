def traverseLevel(array,iMin,iMax,jMin,jMax):
    result = []
    for j in range(jMin,jMax+1):
        result.append(array[iMin][j])
    for i in range(iMin+1,iMax+1):
        result.append(array[i][jMax])
    for j in range(jMax-1,jMin-1,-1):
        if iMin==iMax:
            break
        result.append(array[iMax][j])
    for i in range(iMax-1,iMin,-1):
        if jMin==jMax:
            break
        result.append(array[i][jMin])
    return result
def spiralTraverse(array):
    if len(array)==0: return []
    iMin=0
    iMax=len(array)-1
    jMin=0
    jMax=len(array[0])-1
    result=[]
    while iMin<=iMax and jMin<=jMax:
        result.extend(traverseLevel(array,iMin,iMax,jMin,jMax))
        iMin+=1
        jMin+=1
        iMax-=1
        jMax-=1
    return result

array=[
  [1, 2, 3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10, 9, 8, 7]
]
array=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# array=[[1,2],[3,4],[5,6]]
# 1 2 3 
# 4 5 6
# 7 8 9
# 10 11 12
x=spiralTraverse(array)
print(x)
# n=int(input())
# matrix=[]
# for _ in range(n):
#     matrix.append([ 1 if e=='R' else 0 for e in input().strip()])

def getRightIndex(array,element):
    n=len(array)
    for i in range(n-1,-1,-1):
        if array[i]==element:
            return i
    return 0

def calculateExtremeIndices(matrix):
    indices=[]
    n=len(matrix)
    for row in matrix:
        indices.append(getRightIndex(row,1))
    print(indices)
    return indices

def isPossible(matrix):
    indices= calculateExtremeIndices(matrix)
    indices.sort()
    n=len(indices)
    for i in range(n):
        if indices[i]>i:
            return False
    return True
        
matrix=[
    [0,0,0,0], # 0 # 0
    [1,0,1,0], # 2 # 0
    [1,1,1,0], # 2 # 2
    [1,0,0,0], # 0 # 2
]
matrix=[
    [0,0,1,1,0], # 3
    [0,1,1,1,0], # 3
    [1,0,0,0,0], # 0
    [1,0,0,0,0], # 0
    [1,0,1,0,0], # 2
]
# matrix=[
#     [0,0],
#     [1,0]
# ]
x= isPossible(matrix)
print(x)
x=calculateExtremeIndices(matrix)
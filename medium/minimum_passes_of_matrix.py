import copy
def convert_neighbors(i,j,matrix):
    new_positive_indexes=[]
    if j< len(matrix[0]) -1 and matrix[i][j+1]<0:
        matrix[i][j+1]*=-1
        new_positive_indexes.append([i,j+1])
    if j>0 and matrix[i][j-1]<0:
        matrix[i][j-1]*=-1
        new_positive_indexes.append([i,j-1])
    if i>0 and matrix[i-1][j]<0:
        matrix[i-1][j]*=-1
        new_positive_indexes.append([i-1,j])
    if i<len(matrix)-1 and matrix[i+1][j]<0:
        matrix[i+1][j]*=-1
        new_positive_indexes.append([i+1,j])
    return new_positive_indexes

def getNoOfPositives(matrix):
    count=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] <0:
                count+=1
    return count

def minimumPassesOfMatrix(matrix):
    positive_indexes=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] >0:
                positive_indexes.append([i,j])
    if len(positive_indexes)<1:
        return -1
    no_of_passes=0
    while len(positive_indexes):
        new_positive_indexes=[]
        new_matrix= copy.deepcopy(matrix)
        for e in positive_indexes:
            new_positive_indexes+=convert_neighbors(e[0],e[1],new_matrix)
        positive_indexes=new_positive_indexes
        if len(positive_indexes):
            no_of_passes+=1
        matrix=new_matrix
    if getNoOfPositives(matrix)>0:
        return -1
    return no_of_passes    

matrix=[
  [0, -1, -3, 2, 0],
  [1, -2, -5, -1, -3],
  [3, 0, 0, -4, -1]
]
matrix=[
    [0,-2,-1],
    [-5,2,0],
    [-6,-2,0]
]
matrix= [
    [1, 0, 0, -2, -3],
    [-4, -5, -6, -2, -1],
    [0, 0, 0, 0, -1],
    [-1, 0, 3, 0, 3]
  ]
x=minimumPassesOfMatrix(matrix) 
print(x)
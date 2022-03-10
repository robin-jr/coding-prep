visited=[]

def traverse(matrix, i, j):
    if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j]!=1 or visited[i][j]:
        return 
    visited[i][j]=1
    traverse(matrix, i+1, j)
    traverse(matrix, i-1, j)
    traverse(matrix, i, j-1)
    traverse(matrix, i, j+1)
    matrix[i][j]=2
    return 

def removeIslands(matrix):
    no_of_rows = len(matrix)
    no_of_cols = len(matrix[0])
    global visited
    visited = [[0 for _ in range(no_of_cols)] for _ in range(no_of_rows)]
    for i in range(no_of_rows):
        for j in range(no_of_cols):
            if i==0 or j==0 or i==no_of_rows-1 or j==no_of_cols-1:
                traverse(matrix, i,j)
    for i in range(no_of_rows):
        for j in range(no_of_cols):
            if matrix[i][j]==1:
                matrix[i][j] =0
            elif matrix[i][j]==2:
                matrix[i][j]=1
    return matrix

matrix = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]
]
matrix = removeIslands(matrix)
for e in matrix:
    print(e)

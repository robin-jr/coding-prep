visited = []
def traverse(matrix, i, j):
    if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]) or visited[i][j] or matrix[i][j]==0:
        return 0
    visited[i][j]=1
    sum= 1
    sum += traverse(matrix, i+1, j)
    sum += traverse(matrix, i-1, j)
    sum += traverse(matrix, i, j-1)
    sum += traverse(matrix, i, j+1)
    return sum 
    
def riverSizes(matrix):
    no_of_rows = len(matrix)
    no_of_cols = len(matrix[0])
    global visited
    visited = [[0 for _ in range(no_of_cols)] for _ in range(no_of_rows)]
    result = []
    for i in range(no_of_rows):
        for j in range(no_of_cols):
            if visited[i][j] == 0 and matrix[i][j] == 1:
                result.append(traverse(matrix, i, j))
            visited[i][j] = 1

    return result

matrix=[
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]
matrix=[[1,1,1],[1,0,0]]
x= riverSizes(matrix)
print(x)
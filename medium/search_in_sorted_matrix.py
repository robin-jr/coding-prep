def helper(matrix, target, i, j):
    if i>=len(matrix) or j<0: return [-1,-1]
    if matrix[i][j]==target: return [i,j]
    if matrix[i][j]>target: return helper(matrix, target, i, j-1)
    if matrix[i][j]<target: return helper(matrix, target, i+1, j)
    
def searchInSortedMatrix(matrix, target):
    clen = len(matrix[0])
    return helper(matrix, target, 0, clen-1)

# iterative solution
def searchInSortedMatrix1(matrix, target):
    i , j = 0, len(matrix[0])-1
    while i< len(matrix) and j>=0:
        if matrix[i][j]==target: return [i,j]
        if matrix[i][j]>target: j-=1
        else: i+=1
    return [-1,-1]

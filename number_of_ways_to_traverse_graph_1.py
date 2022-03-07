def numberOfWaysToTraverseGraph(width, height,i=0,j=0):
    result=[[0 for _ in range(width)] for _ in range(height)]
    result[0][0]=1
    for i in range(height):
        for j in range(width):
            if i==0 and j==0:
                continue
            result[i][j]=result[i][j-1]+result[i-1][j]
    return result[height-1][width-1]

    
x= numberOfWaysToTraverseGraph(2,3)
print(x)

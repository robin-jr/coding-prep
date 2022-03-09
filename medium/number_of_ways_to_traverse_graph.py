def numberOfWaysToTraverseGraph(width, height,i=0,j=0):
    sum=0
    if i==height-1 and j==width-1:
        sum+=1
    if i<height-1:
        sum+= numberOfWaysToTraverseGraph(width, height,i+1,j)
    if j<width-1:
        sum+= numberOfWaysToTraverseGraph(width, height,i,j+1)
    return sum

x= numberOfWaysToTraverseGraph(2,3)
print(x)
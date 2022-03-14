def taskAssignment(k, tasks):
    result=[]
    n=2*k
    sorted_indices=sorted(range(n),key=lambda x:tasks[x])
    for i in range(k):
        result.append([sorted_indices[i],sorted_indices[n-i-1]])
    return result
    

tasks=[1, 3, 5, 3, 1, 4]
k=3
x=taskAssignment(k,tasks)
print(x)
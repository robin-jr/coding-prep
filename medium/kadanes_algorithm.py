def kadanesAlgorithm(array):
    prev=array[0]
    m=prev
    for i in range(1,len(array)):
        prev=max(array[i]+prev,array[i])
        m=max(prev,m)
    return m

array=[3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
x=kadanesAlgorithm(array)
print(x)
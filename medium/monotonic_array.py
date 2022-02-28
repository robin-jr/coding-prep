def isMonotonic(array):
    n=len(array)
    if n<2:
        return True
    diff=0
    i=0
    while i< n-1:
        if array[i+1]>array[i] and diff==0:
            diff=1
        if array[i+1]<array[i] and diff==0:
            diff=-1
        if array[i+1]>array[i] and diff==-1:
            return False
        if array[i+1]<array[i] and diff==1:
            return False
        i+=1
    return True

array =[-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
x=isMonotonic(array)
print(x)
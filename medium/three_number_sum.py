from typing import List

def threeNumberSum(array , targetSum):
    array.sort()
    n :int = len(array)
    result = list([])
    if n<3:
        return []
    i=0
    while i<n-2:
        k=n-1
        j=i+1
        while j<k:
            sum = array[i]+ array[j]+array[k]
            if   sum==targetSum:
                result.append([array[i],array[j],array[k]])
            if sum<targetSum:
                j+=1
            else:
                k-=1
        i+=1
    return result
        
                 
        
    

a=[12, 3, 1, 2, -6, 5, -8, 6]
a=[1,2,3]
x=threeNumberSum(a,6)
print(x)
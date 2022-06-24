def merge(arrays):
    l = arrays[0]
    r = arrays[1]
    ans = []
    i,j=0,0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            ans.append(l[i])
            i+=1
        else:
            ans.append(r[j])
            j+=1
    while i< len(l): 
        ans.append(l[i])
        i+=1
    while j< len(r):
        ans.append(r[j])
        j+=1
    return ans
    
def mergeSortedArrays(arrays):
    if len(arrays) == 1: return arrays[0]
    
    if len(arrays) == 2: return merge(arrays)

    l = merge(arrays[:2])
    r = [l]+arrays[2:]
    
    return mergeSortedArrays(r)

arrays = [
  [1, 5, 9, 21],
  [-1, 0],
  [-124, 81, 121],
  [3, 6, 12, 20, 150]
]
x = mergeSortedArrays(arrays)
            
print(x)
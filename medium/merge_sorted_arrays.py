import heapq


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

def mergeSortedArrays2(arrays):
    h = []
    
    for i in range(len(arrays)):
        h.append((arrays[i][0],i, 0))
    heapq.heapify(h)
    
    s = []
    while h:
        e, ki, i = heapq.heappop(h)
        s.append(e) 
        if i == len(arrays[ki])-1: continue
        heapq.heappush(h, (arrays[ki][i+1], ki, i+1))
        
    return s

arrays = [
  [1, 5, 9, 21],
  [-1, 0],
  [-124, 81, 121],
  [3, 6, 12, 20, 150]
]
x = mergeSortedArrays2(arrays)
            
print(x)
def countTriplets(arr, target):
    n = len(arr)
    count=0
    for i in range(n-1):
        potential_pairs = []
        for j in range(i+1,n):
            for e in potential_pairs:
                if arr[j]<e: count+=1
            potential_pairs.append(target-arr[i]-arr[j])
    return count

def countTriplets1(arr,target):
    arr.sort()
    n = len(arr)
    count = 0 
    for i in range(n):
        j = i+1
        k = n-1
        while j < k:
            if arr[i]+arr[j]+arr[k]>=target:
                k-=1
            else:
                count+= (k-j)
                j+=1
    return count
        
                
arr = [-2,0,1,3]
target = 2
x = countTriplets(arr,target)
print(x)
x = countTriplets1(arr,target)
print(x)

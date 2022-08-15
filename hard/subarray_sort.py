def subarraySort(array):
    n = len(array)
    mn = float("inf")
    mx = float("-inf")
    for i in range(1,n):
        if array[i]<array[i-1]:
            mn = min(mn,array[i])
            mx = max(mx,array[i-1])
    
    if mn==float("inf"): return [-1,-1]
    
    a = 0; b=n-1
    while array[a]<= mn: a+=1
    while array[b]>=mx: b-=1

    return [a,b]


array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
x = subarraySort(array)
print(x)

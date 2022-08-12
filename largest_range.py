def getRange(d,e):
    l = e-1
    r = e+1
    d[e]=True
    while True:
        if d.__contains__(l):
            d[l]=True
            l-=1
        else: break
    while True:
        if d.__contains__(r):
            d[r]=True
            r+=1
        else: break
    return [l+1,r-1]
        
def largestRange(array):
    d = {}
    ranges = []
    for e in array:
        d[e] = False
    for e in array:
        if d[e]==False:
            x = getRange(d,e)
            ranges.append([x,abs(x[0]-x[1])])
    return max(ranges, key= lambda x: x[1])[0]

array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
# array.sort()
x = largestRange(array)
print(x)

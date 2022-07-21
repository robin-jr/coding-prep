def calculateSlope(point1,point2):
    try:
        return (point2[1]-point1[1]) / (point2[0]-point1[0])
    except:
        return None

def lineThroughPoints(points):
    n=len(points)
    maxCount=1
    if n==1:
        return maxCount
    for i in range(n):
        dict={}
        for j in range(n):
            if i==j:
                continue
            currentSlope=calculateSlope(points[i],points[j])
            dict[currentSlope]=dict.get(currentSlope,1)+1 # no. of points this line passes through
        c= max(dict.values())
        maxCount = max(c,maxCount)
    return maxCount


points= [
    [1, 1],
    [2, 2],
    [3, 3],
    [0, 4],
    [-2, 6],
    [4, 0],
    [2, 1]
  ]

x = lineThroughPoints(points)
print(x)
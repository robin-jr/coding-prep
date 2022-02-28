from xmlrpc.client import MAXINT


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    i=0
    j=0
    minDiff=MAXINT
    minPair=[]
    while i<len(arrayOne) and j<len(arrayTwo):
        print(arrayOne[i],arrayTwo[j])
        diff=abs(arrayOne[i]-arrayTwo[j])
        if diff==0:
            return [arrayOne[i], arrayTwo[j]]
        if diff<minDiff:
            minDiff = diff
            minPair=[arrayOne[i],arrayTwo[j]]
        if arrayOne[i]<arrayTwo[j]:
            i+=1
        else:
            j+=1
    return minPair
        
arrayOne=[-1, 5, 10, 20, 28, 3]
arrayTwo=[26, 134, 135, 15, 17]
x=smallestDifference(arrayOne, arrayTwo)
print(x)
def longestPeak(array):
    n=len(array)
    maxLength=0
    i=1
    while i<n-1:
       isPeak=array[i]>array[i-1] and array[i]>array[i+1]
       if not isPeak:
           i+=1    
           continue
       leftIndex=i-2
       while leftIndex>=0 and array[leftIndex]<array[leftIndex+1]:
           leftIndex-=1
       rightIndex=i+2
       while rightIndex<n and array[rightIndex]<array[rightIndex-1]:
           rightIndex+=1
       currentLength=rightIndex-leftIndex-1
       maxLength=max(currentLength,maxLength)
       i=rightIndex
    return maxLength

array=[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
array=[1, 2, 3,1,2,3,4,5,4]
# array=[5, 4, 3, 2, 1, 2, 1]
# array= [1, 1, 3, 2, 1]
# array =[1, 2, 3, 2, 1, 1]
x=longestPeak(array)

print(x)
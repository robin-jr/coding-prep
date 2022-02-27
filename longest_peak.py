def longestPeak(array):
    n=len(array)
    length=0
    direction=0
    maxLength=0
    for i in range(1,n):
        r= array[i]
        l = array[i-1]
        if r==l: #reset direction
            if length>=maxLength and length!=0 and direction==-1:
                maxLength=length+1
            direction=0
            length=0
        elif r>l and direction!=1: #reset direction
            if length>maxLength and length!=0:
                maxLength=length+1 #including the current position 
            direction=1
            length=2
        elif r<l and direction!=-1: #reset direction
            if length>maxLength and length!=0:
                maxLength=length+1
            if direction!=1:
                continue
            direction=-1
        elif r>l and direction==1: #increase length
            length+=1
        elif r<l and direction ==-1: #increase length
            length+=1
        if length+1>maxLength and direction==-1:
            maxLength=length+1 #last element
    return maxLength
array=[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# array=[1, 2, 3,1,2,3,4,5,4]
# array=[5, 4, 3, 2, 1, 2, 1]
# array= [1, 1, 3, 2, 1]
array =[1, 2, 3, 2, 1, 1]
x=longestPeak(array)

print(x)
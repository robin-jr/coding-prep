def hasSingleCycle(array):
    counter=0
    i=0
    while counter < len(array):
        if counter>0 and i==0:
            return False
        counter+=1
        i+=array[i]
        i%=len(array)
    return i==0

array =[2, 3, 1, -4, -16, 2]
x = hasSingleCycle(array)
print(x)
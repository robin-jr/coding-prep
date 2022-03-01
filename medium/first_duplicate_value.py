def firstDuplicateValue(array):
    for i in range(len(array)):
        e = array[i]
        if array[abs(e)-1]<0:
            return abs(e)
        else:
            array[abs(e)-1]*=-1
    return -1

array=[2, 1, 5,3, 3,2, 4]
        
x=firstDuplicateValue(array)
print(x)


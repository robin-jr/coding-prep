def threeNumberSort(array, order):
    f =0 
    s= 0
    t= len(array)-1
    i=0

    while i < len(array) and s<=t:
        if array[i]==order[0]:
            array[i],array[f]=array[f],array[i]
            f+=1; s+=1
        elif array[i]==order[1]:
            # array[i],array[s]=array[s],array[i] //no need actually[optional]
            s+=1
        elif array[i]==order[2]:
            array[i],array[t]=array[t],array[i]
            t-=1; i-=1
        i+=1
    return array


array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]

x = threeNumberSort(array,order)
print(x)
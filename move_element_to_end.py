def moveElementToEnd(array, toMove):
    i=0
    j=len(array)-1
    while i<j:
        if array[j]==toMove:
            j -=1
            continue
        if array[i]==toMove:
            array[i],array[j] = array[j],array[i] #swap
        i+=1
    return array
a=[2, 1, 2, 2, 2, 3, 4, 2]
x=moveElementToEnd(a,2)

print(x)
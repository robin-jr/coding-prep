def firstDuplicateValue(array):
    counts={}
    for e in array:
        c = counts.get(e,0)
        if c==0:
            counts[e]=1
        else:
            return e
    return -1

array=[2, 1, 5,  3, 3,2, 4]
x=firstDuplicateValue(array)
print(x)


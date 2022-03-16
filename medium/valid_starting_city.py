def validStartingCity(distances, fuels, mpg):
    start=0
    miles_remaining=0
    n=len(distances)
    while start<n-1:
        for i in range(start,n):
            miles_remaining+= (fuels[i]*mpg)
            if miles_remaining<distances[i]:
                miles_remaining=0
                start=i+1
                break
            miles_remaining-=distances[i]
        if i==n-1:
            break
    return start
        

distances=[5, 25, 15, 10, 15]
fuel=[1, 2, 1, 0, 3]
x=validStartingCity(distances,fuel,10)
print(x)
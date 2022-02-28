def arrayOfProducts(array):
    n=len(array)
    leftProducts=[1 for _ in range(n)]
    rightProducts=[1 for _ in range(n)]
    products=[1 for _ in range(n)]
    
    for i in range(1,n):
        leftProducts[i] =leftProducts[i-1]*array[i-1]
        products[i] = leftProducts[i]
    
    for i in range(n-2,-1,-1):
        rightProducts[i] =rightProducts[i+1]*array[i+1]
        products[i]*=rightProducts[i]
    
    return products
    

array=[5, 1, 4, 2]
x=arrayOfProducts(array)
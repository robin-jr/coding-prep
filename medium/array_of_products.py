def arrayOfProducts(array):
    n=len(array)
    products=[1 for _ in range(n)]
    
    leftRunningProduct=1
    for i in range(n):
        products[i] = leftRunningProduct
        leftRunningProduct*=array[i]
        
    rightRunningProduct=1
    for i in range(n-1,-1,-1):
        products[i]*=rightRunningProduct
        rightRunningProduct*=array[i]
    
    return products
    

array=[5, 1, 4, 2]
x=arrayOfProducts(array)
print(x)
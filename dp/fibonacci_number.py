def fib(n: int) -> int:
    if n==0: return 0
    if n==1: return 1
    a ,b = 0,1
    c = 0
    for _ in range(2,n+1):
        c=a+b
        a,b= b,c
    return c
    # arr = [0,1]
    # for i in range(2,n+1):
    #     arr.append(arr[i-1]+arr[i-2])
    # return arr[n]

for i in range(9):
    x = fib(i)
    print(x)
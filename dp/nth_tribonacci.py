def fib(n: int) -> int:
    if n==0: return 0
    if n==1: return 1
    if n==2: return 1
    a ,b, c = 0,1,1
    d = 0
    for _ in range(3,n+1):
        d=a+b+c
        a,b,c = b,c,d
    return d

for i in range(10):
    x = fib(i)
    print(x)
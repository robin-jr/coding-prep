T = int(input())
for case in range(T):
    n= int(input())
    a=list(map(int,input().split()))
    a.sort()
    count=0
    i=0
    while i<n:
        if a[i]>=i+1:
            count+=1
        else:
            a.pop(i)
            n-=1
            continue
        i+=1
    print("Case #{}: {}".format(case+1,count))
    
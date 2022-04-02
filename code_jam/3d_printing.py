T = int(input())
for case in range(T):
    p=[[0] for i in range(3)]
    for i in range(3):
        p[i]=list(map(int,input().split()))
    c = min(p[0][0],p[1][0],p[2][0])
    m = min(p[0][1],p[1][1],p[2][1])
    y = min(p[0][2],p[1][2],p[2][2])
    k = min(p[0][3],p[1][3],p[2][3])
    
    print("Case #{}: ".format(case+1),end="")
    if c+m+y+k<10e5:
        print("IMPOSSIBLE")
        continue
    sum = c+m+y+k
    diff = int(sum - 10e5)
    while diff>0:
        if k>=diff: 
            k-=diff
            diff=0
        elif y >=diff:
            y-=diff
            diff=0
        elif m >=diff:
            m-=diff
            diff=0
        elif c >= diff:
            c-=diff
            diff=0
        elif diff>k:
            diff-=k
            k=0
        elif diff>y:
            diff-=y
            y=0
        elif diff>m:
            diff-=m
            m=0
        elif diff>c:
            diff-=c
            c=0
    print(c,m,y,k)
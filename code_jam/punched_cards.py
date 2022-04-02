def drawRow(i,j):
    for col in range(j):
        if i==0 and col==0:
            print("..+",end="")
        elif col==0:
            print("+-+",end="")
        else:
            print("-+",end="")
    print("")
    
def drawRow2(i,j):
    for col in range(j):
        if i==0 and col==0:
            print("..|",end="")
        elif col==0:
            print("|.|",end="")
        else:
            print(".|",end="")
    print("")

T = int(input())
for case in range(T):
    r,c = map(int, input().split())
    print("Case #{}:".format(case+1))
    for i in range(r):
        drawRow(i,c)
        drawRow2(i,c)
    drawRow(r,c)
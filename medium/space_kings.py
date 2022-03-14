import copy
p=20
q=60
n=3

# alien_lives=[80,80,120]
# golds=[100,200,300]
arr=[
    [80,100],
    [80,200],
    [120,300]
]
# p=50
# q=400
# n=2
# arr=[
#     [60,100],
#     [190,200]
# ]

p=200
q=10
n=5
arr=[
    [20,100],
    [30,20],
    [20,101],
    [200,500],
    [10,1000]
]

max_gold=0

def hit(arr,pointsSoFar,isAsha):
    global max_gold
    # print(arr,pointsSoFar)
    if len(arr)==0:
        max_gold=max(max_gold,pointsSoFar)
        return
    
    # Asha skips, so Amir hits [or] just Amir hits
    a= copy.deepcopy(arr)
    a[0][0]-=q
    if a[0][0]<1:
        a.pop(0)
    hit(a,pointsSoFar,True)
    
    if isAsha:
        for i in range(len(arr)):
            a=copy.deepcopy(arr)
            a[i][0]-=p
            tempPoints=pointsSoFar
            if a[i][0]<1:
                tempPoints+=a[i][1]
                a.pop(i)
            hit(a,tempPoints,False)

hit(arr,0,True)
print(max_gold)
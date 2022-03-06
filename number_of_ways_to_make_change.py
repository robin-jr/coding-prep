
def numberOfWaysToMakeChange(n, denoms):
    ways=[0 for i in range(n+1)]
    ways[0]=1
    for denom in denoms:
        for i in range(1,n+1):
            if denom<=i:
                ways[i]+=ways[i-denom]
    return ways[-1]


n=6
denoms=[1,5]
x=numberOfWaysToMakeChange(n,denoms)
print(x)

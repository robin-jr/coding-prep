def levenshteinDistance(str1, str2):
    arr=[[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i==0 and j==0:
                arr[i][j]=0
            elif i==0:
                arr[i][j]=arr[i][j-1]+1
            elif j==0:
                arr[i][j]=arr[i-1][j]+1
            elif str1[i-1]==str2[j-1]:
                arr[i][j]=arr[i-1][j-1]
            else:
                arr[i][j]=min(arr[i][j-1],arr[i-1][j],arr[i-1][j-1])+1
    return arr[-1][-1]
    
str2="yabd"
str1="abc"

x = levenshteinDistance(str1, str2)
print(x)

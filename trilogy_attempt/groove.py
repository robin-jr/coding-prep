class Solution:
    def getArray(self,n,b):
        arr = [[0 for j in range(n)] for i in range(n)]
        mid = n//2
        for i in range(n):
            for j in range(n):
                if i==j and i == mid:
                    arr[i][j] = -1
                if abs(mid-i)<=b:
                    if abs(mid-j) <= b:
                        arr[i][j] = -1
        return arr
    
    def solve(self, A, B):
        n,b = A,B
        arr = self.getArray(n,b)
        for i in range(n):
            for j in range(n):
                if i==0 and j==0:
                    arr[i][j] = 1
                    continue
                if arr[i][j] != -1:
                    ways = 0
                    if arr[i-1][j] != -1: ways +=arr[i-1][j]
                    if arr[i][j-1] != -1: ways += arr[i][j-1]
                    arr[i][j] = ways
        for e in arr:
            for e in e: 
                print (e,end = "      ")
            print("\n")
        return arr[-1][-1]

s  = Solution()
x = s.solve(7,1)
print(x)
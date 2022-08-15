class Solution:
    def convert(self, s: str, numRows: int) -> str:
        k = 0 
        t = ["" for _ in range(numRows)]
        up = True
        for e in s:
            if k==numRows: 
                up=False
                k-=2
            if k <=0:
                up = True
                k = 0
            t[k]+=e
            if up: k+=1 
            else: k-=1
        return "".join(t)     
            
            
    
s = "PAYPALISHIRING"
numRows = 3
ss = Solution()
x = ss.convert(s,numRows)
print(x)
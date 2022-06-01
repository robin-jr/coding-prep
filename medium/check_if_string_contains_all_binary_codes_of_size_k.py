class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        combinations =set()
        n = len(s)
        for i in range(n-k):
            combinations.add(s[i:i+k])
        return len(combinations) == 2**k

    def hasAllCodes2(self, s:str, k:int) -> bool:
        need = 1<<k
        h = [False]*need
        n = len(s)
        all_one = need-1
        hs = 0
        for i in range(0,n):
            hs = ((hs<<1) & all_one) | int(s[i])
            if i>=k-1 and not h[hs]:
                h[hs] = True
                need-=1
                if need==0: return True
        return False

s = "00110110"
k = 2
s = "00110"
k=2
sol = Solution()
x = sol.hasAllCodes2(s,k)
print(x)

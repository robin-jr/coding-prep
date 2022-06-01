class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor==0: return -1
        negative = False
        if divisor<0 : divisor = -divisor; negative = True
        if dividend<0 : dividend = -dividend; negative = not negative
        r =0
        while True:
            dividend -= divisor
            if dividend>=0: r+=1
            else: break
        return r if not negative else -r

s = Solution()
x = s.divide(-1,1)
print(x)
from typing import *


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        required_sum = n*(n+1)//2
        sum = 0 
        for e in nums: sum+=e
        return required_sum - sum

nums =  [9,6,4,2,3,5,7,0,1]
s = Solution()
x =s.missingNumber(nums)
print(x)
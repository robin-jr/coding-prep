
from typing import *

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
    
nums = [1,2,3,4]
s = Solution()
x = s.runningSum(nums)
print(x)
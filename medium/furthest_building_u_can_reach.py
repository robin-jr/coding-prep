from functools import cache
from typing import *

class Solution:
    @cache
    def helper(self, heights: Tuple[int], bricks: int, ladders: int, i: int=0) -> int:
        if i>= len(heights)-1: 
            return i

        if heights[i] >= heights[i+1]: return self.helper(heights, bricks, ladders, i+1)

        heightDiff = heights[i+1] - heights[i]

        if ladders >0 and heightDiff > bricks : return self.helper(heights, bricks, ladders-1, i+1) # no bricks available
        
        if heightDiff <= bricks and ladders < 1 : return self.helper(heights, bricks-heightDiff, ladders, i+1) # no ladders available
        
        if heightDiff> bricks and ladders < 1 : 
            return i

        if bricks >= heightDiff and ladders >0 :
            return max(self.helper(heights, bricks-heightDiff, ladders, i+1), self.helper(heights, bricks, ladders-1,i+1)) # we have both
        
        
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int, i: int=0) -> int:
        # heights = tuple(heights)
        # return self.helper(heights, bricks, ladders, i)
        from heapq import heappush, heappop

        minheap = []

        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heappush(minheap,diff)
            if len(minheap) > ladders:
                bricks -= heappop(minheap)
            if bricks<0:
                return i
        return len(heights)-1 

        
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1

s = Solution()
x = s.furthestBuilding(heights,bricks, ladders)
print(x)
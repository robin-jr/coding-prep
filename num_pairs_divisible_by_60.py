from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n=len(time)
        count = 0
        for i in range(n):
            time[i]=time[i]%60
        pairs={}
        for e in time:
            needed_pair = (60-e)%60
            if pairs.__contains__(e):
                count+=pairs[e]
            pairs[needed_pair] = pairs.get(needed_pair,0)+1
        return count
            
        

s = Solution()
time = [30,20,150,100,40]
x = s.numPairsDivisibleBy60(time)
print(x)
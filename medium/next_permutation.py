import time
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def getPermutations(arr,s,p):
            if not s:arr.append(p)
            else: 
                for i in range(len(s)):
                    getPermutations(arr,s[:i]+s[i+1:],p+s[i])
            return arr
        
        s=""
        for e in nums: s+=str(e)
        x = getPermutations([],s,"")
        x=list(set(x))
        x.sort()
        n=len(x)
        for i, e in enumerate(x):
            if int(e)==int(s):
                t = x[i+1] if i<n-1 else x[0]
                break
        for i,e in enumerate(t):
            nums[i]=int(e)

nums=[6,7,5,3,5,6,2,9,1,2]
start = time.time()
Solution().nextPermutation(nums)
print(nums)
end = time.time()
print(end - start)
from typing import  *

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        a = 0
        total_width_needed = 0
        for e in s:
            curr_width = widths[ord(e)-97]
            total_width_needed += curr_width
            if total_width_needed > 100:
                total_width_needed = curr_width
                a += 1
        a += 1 if total_width_needed != 0 else 0
        return [a, total_width_needed]


ss = Solution()
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
# widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# s = "bbbcccdddaaa" # 10 10 10 10 10 10 10 10 10 4 4 4
x = ss.numberOfLines(widths, s)
print(x)
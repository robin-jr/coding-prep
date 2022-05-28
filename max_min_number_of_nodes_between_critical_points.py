# Definition for singly-linked list.
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        indices = []
        prev = None
        sign = 0
        i=0
        while head:
            i+=1
            if prev:
                if prev > head.val:
                    if sign==1: indices.append(i-1)
                    sign = -1
                elif prev< head.val:
                    if sign==-1: indices.append(i-1)
                    sign = 1
                elif prev == head.val:
                    sign = 0
            head, prev = head.next, head.val

        n = len(indices)
        if n<2: return [-1,-1]
        maxD = indices[-1]-indices[0]
        minD = maxD
        i ,j = 0, 1
        while j<n:
            diff = indices[j]-indices[i]
            if diff<minD: minD = diff
            i+=1; j+=1
        return [minD,maxD]


l = ListNode(5)
l.next = ListNode(3)
l.next.next=ListNode(1)
l.next.next.next=ListNode(2)
l.next.next.next.next=ListNode(5)
l.next.next.next.next.next=ListNode(1)
l.next.next.next.next.next.next=ListNode(2)
s = Solution()
x = s.nodesBetweenCriticalPoints(l)
print(x)
        
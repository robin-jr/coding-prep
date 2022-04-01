class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        right_indices={}
        for e,current_element in enumerate(s):
            right_indices[current_element]=e 
        visited=set()
        stack=[]
        for i,e in enumerate(s):
            if e not in visited:
                while stack and e < stack[-1] and right_indices[stack[-1]]>i:
                    visited.remove(stack.pop())
                visited.add(e)
                stack.append(e)
        return ''.join(stack)
        
s = "cbacdcbc"
solution = Solution()
x=solution.removeDuplicateLetters(s)
print("solution -> ",x)
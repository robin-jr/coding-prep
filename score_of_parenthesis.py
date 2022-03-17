class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for e in s:
            if e == '(':
                stack.append(e)
            else:
                last = stack.pop()
                if last=='(': stack.append(1)
                else: 
                    stack.pop()
                    stack.append(last*2)
            if len(stack)>1 and stack[-1]!='(' and stack[-2]!='(':
                stack.append(stack.pop()+stack.pop())
        return stack[0]

s="((()))()"
s="(()(()))"
# [6]
sol = Solution()
x=sol.scoreOfParentheses(s)
print(x)
def balancedBrackets(string):
    stack=[]
    for e in string:
        if e in ['(','[','{']:
            stack.append(e)
        if e not in [')','}',']']:
            continue
        elif len(stack)>0:
            if stack[-1]=='{' and e=='}':
                stack.pop()
            elif stack[-1]=='(' and e==')':
                stack.pop()
            elif stack[-1]=='[' and e==']':
                stack.pop()
            else: #overlapping brackets
                return False
        else: #stack is empty
            return False
    return not len(stack)

string="([])(){}(())()()"
x=balancedBrackets(string)
print(x)

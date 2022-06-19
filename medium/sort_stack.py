def sortStack(stack):
    if len(stack)>0:
        top = stack.pop()
        sortStack(stack)
        order(stack,top)
    return stack

def order(stack,top):
    if len(stack)==0 or stack[-1]<=top:
        stack.append(top)
    else:
        t= stack.pop()
        order(stack,top)
        stack.append(t)
    
stack = [-5, 2, -2, 4, 3, 1]
x = sortStack(stack)
print(x)
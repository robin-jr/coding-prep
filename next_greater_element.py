def nextGreaterElement(array):
    n = len(array)
    result = [-1] * n
    stack = []
    for i in range(2*n):
        while stack and array[stack[-1]]<array[i%n]:
            result[stack.pop()]=array[i%n]
        stack.append(i%n)
    return result

array = [2, 5, -3, -4, 6, 7, 2]
x = nextGreaterElement(array)
print(x)

        
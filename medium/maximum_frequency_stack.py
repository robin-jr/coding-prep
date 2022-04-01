class FreqStack:
    def __init__(self):
        self.frequencies={}
        self.stack=[]

    def push(self, val: int) -> None:
        self.frequencies[val]=self.frequencies.get(val, 0) + 1
        self.stack.insert(0, val)

    def pop(self) -> int:
        max_frequency = max(self.frequencies.values())
        for i, e in enumerate(self.stack):
            if self.frequencies.get(e)==max_frequency:
                self.frequencies[e]-=1
                return self.stack.pop(i)


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
freqStack = FreqStack()
freqStack.push(5)  # The stack is [5]
freqStack.push(7)  # The stack is [5,7]
freqStack.push(5)  # The stack is [5,7,5]
freqStack.push(7)  # The stack is [5,7,5,7]
freqStack.push(4)  # The stack is [5,7,5,7,4]
freqStack.push(5)  # The stack is [5,7,5,7,4,5]
# return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
x = freqStack.pop()
print(x)
# return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
x = freqStack.pop()
print(x)
# return 5, as 5 is the most frequent. The stack becomes [5,7,4].
x = freqStack.pop()
print(x)
# return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
x = freqStack.pop()
print(x)

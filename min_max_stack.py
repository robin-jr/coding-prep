# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self) -> None:
        self.array = []
        self.mins = []
        self.maxs = []
    def peek(self):
        return self.array[-1]

    def pop(self):
        self.maxs.pop()
        self.mins.pop()
        return self.array.pop()

    def push(self, number):
        self.array.append(number)        
        if not self.mins:
            self.mins.append(number)
            self.maxs.append(number)
        else:
            self.mins.append(min(self.getMin(),number))
            self.maxs.append(max(self.getMax(),number))

    def getMin(self):
        return self.mins[-1]

    def getMax(self):
        return self.maxs[-1]
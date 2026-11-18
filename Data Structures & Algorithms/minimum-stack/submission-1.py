class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if val is not None:
            self.stack.append(val)

    def pop(self) -> None:
        if self is not None:
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack is not None:
            return self.stack[-1]
        

    def getMin(self) -> int:
        i = 0
        minE = self.stack[0]
        lenStack = len(self.stack)
        while i < lenStack:
            if self.stack[i] < minE:
                minE = self.stack[i]
            i += 1
        return minE
        

class MinStack:

    def __init__(self):
        self.currmin = float('inf')
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.currmin = val
        else:
            self.stack.append(val - self.currmin)
            if self.stack[-1] < 0:
                self.currmin = val
        

    def pop(self) -> None:
        x = self.stack.pop()
        if x < 0:
            self.currmin -= x
        

    def top(self) -> int:
        if self.stack[-1] > 0:
            return self.stack[-1] + self.currmin
        else:
            return self.currmin

    def getMin(self) -> int:
        return self.currmin

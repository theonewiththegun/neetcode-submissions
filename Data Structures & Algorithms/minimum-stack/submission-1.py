# [] min: None
# [10] min: 10
# [10, 8] min: 8
# [10, 8, 20] min: 8
# [10, 8, 20, 1] min: 1
# [10, 8, 20] min: 8
# [10, 8] min: 8
# [10] min: 10
# when the stack is pushed against, the min is the min of the prev min and the pushed val
# when the stack is popped, the min is the min that was calculated for the previous stack size
# so basically we could store the history of all the mins as yet another stack
# and push/pop it in sync with the main stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(
                min(
                    self.min_stack[-1],
                    val,
                )
            )
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        

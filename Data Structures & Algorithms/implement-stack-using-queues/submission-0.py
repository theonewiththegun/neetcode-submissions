# 1 2 3 4
# we need to make one of queues to pop from front the most recent value
# how

from collections import deque

class MyStack:

    def __init__(self):
        self.q0 = deque()
        self.q1 = deque()
        
    def push(self, x: int) -> None:
        q_from = self.q1 if not self.q0 else self.q0
        q_to = self.q0 if not self.q0 else self.q1
        q_to.append(x)
        while q_from:
            q_to.append(q_from.popleft())
        

    def pop(self) -> int:
        q = self.q1 if not self.q0 else self.q0
        return q.popleft()
        

    def top(self) -> int:
        q = self.q1 if not self.q0 else self.q0
        return q[0]
        

    def empty(self) -> bool:
        return not self.q0 and not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
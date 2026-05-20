class ListNode:
    def __init__(self, val, prv=None, nxt=None):
        self.val = val
        self.prv = prv
        self.nxt = nxt


class Deque:
    
    def __init__(self):
        # those two always point to a dummy
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.tail.prv, self.head.nxt = self.head, self.tail
        self.n = 0


    def isEmpty(self) -> bool:
        return self.n == 0
        

    def append(self, value: int) -> None:
        # prev -insert here-> tail-dummy
        new = ListNode(value, prv=self.tail.prv)
        self.tail.prv.nxt = new
        self.tail.prv = new
        self.n += 1
        

    def appendleft(self, value: int) -> None:
        # head-dummy -insert here-> next
        new = ListNode(value, prv=self.head, nxt=self.head.nxt)
        self.head.nxt.prv = new
        self.head.nxt = new
        self.n += 1
        

    def pop(self) -> int:
        # prev -> last (pop me) -> tail-dummy
        if self.n == 0:
            return -1
        new_last = self.tail.prv.prv
        out = new_last.nxt.val
        new_last.nxt = self.tail
        self.tail.prv = new_last
        self.n -= 1
        return out
        

    def popleft(self) -> int:
        # head-dummy -> first (pop me) -> next
        if self.n == 0:
            return -1
        new_first = self.head.nxt.nxt
        out = new_first.prv.val
        new_first.prv = self.head
        self.head.nxt = new_first
        self.n -= 1
        return out
        

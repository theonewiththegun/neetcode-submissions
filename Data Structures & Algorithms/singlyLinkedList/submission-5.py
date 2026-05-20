class ListNode:
    def __init__(self, val, nxt = None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    
    def __init__(self):
        self.head: ListNode = None
        self.tail: ListNode = None

    
    def get(self, index: int) -> int:
        ptr = self.head
        i = 0
        while ptr is not None:
            if i == index:
                return ptr.val
            ptr = ptr.nxt
            i += 1
            
        return -1
        

    def insertHead(self, val: int) -> None:
        if self.head is not None:
            self.head = ListNode(val, nxt=self.head)
        else:
            self.head = ListNode(val)
            self.tail = self.head
        # print(self.getValues())
        

    def insertTail(self, val: int) -> None:
        if self.tail is not None:
            self.tail.nxt = ListNode(val)
            self.tail = self.tail.nxt
        else:
            self.head = ListNode(val)
            self.tail = self.head
        # print(self.getValues())
        
    def remove(self, index: int) -> bool:
        # print(self.getValues())
        if not self.head:
            # print('nothing to remove')
            return False

        ptr = self.head
        prev = None

        for i in range(index):
            if ptr.nxt is None:
                # print('invalid index to remove')
                return False
            prev = ptr
            ptr = ptr.nxt

        if prev is None:
            # print('removing head')
            self.head = ptr.nxt
            if not self.head:
                # print('head was the only element, cleaning up the tail')
                self.tail = None
        else:
            # print('basic remove case')
            prev.nxt = ptr.nxt
            if not prev.nxt:
                self.tail = prev

        return True

    def getValues(self) -> List[int]:
        ptr = self.head
        out = []
        while ptr is not None:
            out.append(ptr.val)
            ptr = ptr.nxt
        return out
        
        

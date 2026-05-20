# cases
# 1 - empty list
# 2 - one-element-list
# 3 - three-elements-list

class ListNode:
    def __init__(self, val, nxt = None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1) # always points to the dummy
        self.tail = self.head

    
    def get(self, index: int) -> int:
        # 1
        # ptr = None; no loop; return -1
        # 2
        # ptr = dummy; 1 iter: i = 1, ptr = 1st elmt; return 1st elmt
        # 3
        # ptr = dummy; 3 iters res: i = 2, ptr = 3rd elmt; return 3rd
        ptr = self.head.nxt
        i = 0
        while ptr:
            if i == index:
                return ptr.val
            i += 1
            ptr = ptr.nxt
        return -1
        

    def insertHead(self, val: int) -> None:
        # 1
        # new -> dummy+1 (none)
        # dummy -> new -> none
        # tail -> new
        # 2
        # dummy -> new -> prev1st
        # 3
        # dummy -> new -> prev1st
        new_node = ListNode(val, self.head.nxt)
        self.head.nxt = new_node
        if not new_node.nxt:
            self.tail = new_node


    def insertTail(self, val: int) -> None:
        # 1
        # dummy -> new
        # tail -> new
        # 2
        # 1st -> new
        # tail -> new
        # 3
        # 3rd -> new
        # tail -> new
        new_node = ListNode(val)
        self.tail.nxt = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        # 1; index = 0
        # ptr = dummy; no loop; return False
        # 1; index = 1
        # ptr = dummy; 1 iter: i = 1, ptr = None; exit loop; return False
        # 2; index = 0
        # ptr = dummy; no loop; ptr and ptr.nxt exist; dummy.nxt = None
        ptr = self.head
        i = 0
        while ptr and i < index:
            i += 1
            ptr = ptr.nxt

        if ptr and ptr.nxt:
            ptr.nxt = ptr.nxt.nxt
            if not ptr.nxt:
                self.tail = ptr
            return True

        return False
        

    def getValues(self) -> List[int]:
        ptr = self.head.nxt
        out = []
        while ptr:
            out.append(ptr.val)
            ptr = ptr.nxt
        return out
        

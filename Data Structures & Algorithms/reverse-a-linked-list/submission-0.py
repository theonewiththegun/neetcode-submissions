# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2 -> 3
# ptr = 1; ptr.nxt.nxt = ptr; ptr = ptr.nxt.nxt

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr_n = head
        next_n = head.next
        curr_n.next = None
        while next_n:
            cache = next_n.next
            next_n.next = curr_n
            curr_n = next_n
            next_n = cache
        
        return curr_n

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# l1, l2
# dummy head
# while l1ptr and l2ptr
# the least goes to head
# the remaining go to head

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        tail = head
        l, r = list1, list2
        while l and r:
            if l.val <= r.val:
                tail.next = l
                tail = l
                l = l.next
            else:
                tail.next = r
                tail = r
                r = r.next

        while l:
            tail.next = l
            tail = l
            l = l.next
        
        while r:
            tail.next = r
            tail = r
            r = r.next

        return head.next

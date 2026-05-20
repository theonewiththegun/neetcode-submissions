# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# we need to take the min element of all the given lists
# so it's O(m) for each iter where m is the number of lists
# and it's O(k) iters in total, where k is the max list len
# so the total time complexity would be O(m*k) = O(n) where n is the number of
# elements in each list, so kinda linear time, could work

# problems
# - singly linked list, if need a ref to the prev element, we should be careful
# - how do we keep the current ptr for each of the given lists? hashmap

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        dummy_head = ListNode(0)

        hm = {}
        for i, head in enumerate(lists):
            hm[i] = head
        
        ptr = dummy_head
        while hm:
            candidate = None
            candidate_idx = None
            for i, node in hm.items():
                if not candidate or node.val < candidate.val:
                    candidate = node
                    candidate_idx = i
            ptr.next = candidate
            ptr = ptr.next
            hm[candidate_idx] = candidate.next
            if not hm[candidate_idx]:
                del hm[candidate_idx]

        return dummy_head.next





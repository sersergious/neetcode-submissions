# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we can check if the next node.next hax a 
        #node that's < than the curr val, assuming sorted
        
        if head is None:
            return False

        if head and head.next is None:
            return False
        
        if head and head.next == head:
            return True
        

        prev = head
        curr = head.next

        while curr:
            if curr.val < prev.val and curr.next is not None:
                return True      
            
            temp = curr.next
            prev = curr
            curr = temp

        return False
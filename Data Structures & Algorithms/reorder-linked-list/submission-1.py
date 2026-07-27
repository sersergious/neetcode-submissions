# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # this is a repeat. I kinda remember the Solution 

        #Edge case: check if head is none or is a len == 1
        

        #1. Compute the midpoint

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        
        slow.next = None 

        #2. Reverse the l2

        prev = None 

        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2 
            l2 = temp
        
        l2 = prev
        #3. Update pointers
            # prev as the start of the reversed list
        l1 = head  
        
        while l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next

        # reverse the list
        prev = slow.next = None
        
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp

        l1, l2 = head, prev 
        
        while l2:
            l1Next = l1.next
            l2Next = l2.next

            l1.next = l2
            l2.next = l1Next 

            l1 = l1Next
            l2 = l2Next

        


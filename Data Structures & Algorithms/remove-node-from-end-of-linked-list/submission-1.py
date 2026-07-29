# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse the list 
        # then count off # number of node + update the ptrs
            
        headReverse = self.reverseList(head)
        count = 0
        node = prev = ListNode()
        node.next = headReverse
        
        while count < n:
            count += 1
            prev = node 
            node = node.next
        
        prev.next = node.next

        if n == 1:  
            return self.reverseList(prev.next) 
        else:
            return self.reverseList(headReverse)
        

         

        

    def reverseList(self, head):
        curr = head
        prev = None 

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        carry = 0

        while l1 and l2:
            total = carry + l1.val + l2.val

            if total >= 10:
                node.next = ListNode(total % 10)
                carry = total // 10
            else:
                node.next = ListNode(total)
                carry = 0
            
            l1 = l1.next
            l2 = l2.next
            node = node.next
        
        while l1:
            total = carry + l1.val

            if total >= 10:
                node.next = ListNode(total % 10)
                carry = total // 10
            else:
                node.next = ListNode(total)
                carry = 0
            
            l1 = l1.next
            node = node.next
        
        while l2:
            total = carry  + l2.val

            if total >= 10:
                node.next = ListNode(total % 10)
                carry = total // 10
            else:
                node.next = ListNode(total)
                carry = 0
            
            l2 = l2.next
            node = node.next

        if carry != 0:
            node.next = ListNode(carry)

        return dummy.next

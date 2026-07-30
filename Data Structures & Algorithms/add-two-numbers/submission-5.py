# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = dummy = ListNode()

        while l1 and l2:
            valSum = l1.val + l2.val + carry
            
            if valSum >= 10:
                carry = valSum // 10
                actual = valSum % 10
                res.next = ListNode(actual)
            else:
                res.next = ListNode(valSum)
                carry = 0
            
            l1 = l1.next
            l2 = l2.next
            res = res.next

        while l1:
            valSum = carry + l1.val
            if valSum >= 10:
                carry = valSum // 10
                actual = valSum % 10
                res.next = ListNode(actual)
            else:
                res.next = ListNode(valSum)
                carry = 0
            res = res.next
            l1 = l1.next

        while l2:
            valSum = carry + l2.val
            if valSum >= 10:
                carry = valSum // 10
                actual = valSum % 10
                res.next = ListNode(actual)
            else:
                res.next = ListNode(valSum)
                carry = 0
            res = res.next
            l2 = l2.next
        
        if carry > 0:
            res.next = ListNode(carry)

        return dummy.next
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Time:
        # Reflection: i was buildin the new list with nexts and then updating randoms.

        hM = {None: None}
        cur = head
        # Two pass 
        # To create copies in the dict
        while cur:
            copy = Node(cur.val)
            hM[cur] = copy
            cur = cur.next
        
        cur = head
        # To map the pointers
        while cur:
            copy = hM[cur]
            copy.next = hM[cur.next]
            copy.random = hM[cur.random]
            cur = cur.next

        return hM[head]
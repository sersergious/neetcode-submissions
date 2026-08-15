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
        # Time
        # Reflection

        copy = {None: None}
        cur = head

        while cur:
            copy[cur] = Node(cur.val)
            cur = cur.next
        
        node = copy[head]
        cur = head
        
        while cur:
            node.next = copy[cur.next]
            node.random = copy[cur.random]
            cur = cur.next
            node = node.next

        return copy[head]
        
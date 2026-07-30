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
        # Time: 50 minutes
        # Reflection: in the end had to look at the solution because i got
        # confused with the random pointers. More specifically i was treating 
        # them as just values, when instead they are memory chuncks. So, my 
        # dummy list building pattern was failing (which I tried initially). 
        # I was pointing to the copies of the nodes that weren't in memory yet
        # which explained the nulls I was getting for the random pointers.
        # Instead, use hashmap to store actual copies of the nodes. 

        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
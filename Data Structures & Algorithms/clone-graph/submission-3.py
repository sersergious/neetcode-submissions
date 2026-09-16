"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Time: 17
# Reflection: Second attempt - I had to go back to the previous soluion because there was a bug I could not fix. Turned out to be a wrong base case, where i was return the original node, instead of its copy.

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hM = {}

        def dfs(node):
            
            if node in hM:
                return hM[node]

            copy = Node(node.val)
            hM[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        
        return dfs(node) if node else None

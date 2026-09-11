"""
import copy
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapped = {}

        def dfs(node):
            if node in mapped:
                return mapped[node]

            clone = Node(node.val)
            mapped[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
                
        return dfs(node) if node else None
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: 16
# Reflection: I got the algo initially wrong - I thought we append the node and then keep iterating until queue is None. Wrong technically since we  traverse a portion of the tree but we cannot build the list on the non-existent index of len(queue)-1 -- that was my mistake. Reached for solution. Now i need to redo this problem.

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root])
        res = []

        while queue:
            qLen = len(queue)
            lvl = []
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    lvl.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
            if lvl:
                res.append(lvl)
        
        return res
            

        
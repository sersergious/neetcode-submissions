# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        return self._goodNodes(root, root.val)
    
    def _goodNodes(self, root, maxSoFar):
        if not root:
            return 0
        
        good = 1 if root.val >= maxSoFar else 0
        maxSoFar = max(maxSoFar, root.val)

        return good + self._goodNodes(root.left, maxSoFar) + self._goodNodes(root.right, maxSoFar)


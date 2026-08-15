# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isValid(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isValid(self, root1, root2):

        if not root1 and not root2:
            return True
        
        if root1 and root2 and root1.val == root2.val:
            return self.isValid(root1.left, root2.left) and self.isValid(root1.right, root2.right)
        
        return False

        
        

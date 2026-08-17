# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root:
            return False
        
        if root.val > p.val and root.val > q.val and root.left:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if root.val < p.val and root.val < q.val and root.right:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root

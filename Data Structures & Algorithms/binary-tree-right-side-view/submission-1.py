# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time:
# Reflection:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []

        while q:
            qLen = len(q)
            nodes = []

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if nodes:
                res.append(nodes[-1])
        
        return res



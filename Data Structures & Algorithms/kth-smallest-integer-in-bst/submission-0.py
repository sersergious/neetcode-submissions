# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        nodes = []

        while q:
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()

                if node:
                    nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
        nodes.sort()
        return nodes[k-1]
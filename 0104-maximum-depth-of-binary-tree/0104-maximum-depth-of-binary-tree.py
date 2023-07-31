# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0

        q = deque([(root, 1)])

        while q:
            cur, level = q.popleft()
            if cur.left:
                q.append((cur.left, level + 1))
            if cur.right:
                q.append((cur.right, level + 1))

        return level
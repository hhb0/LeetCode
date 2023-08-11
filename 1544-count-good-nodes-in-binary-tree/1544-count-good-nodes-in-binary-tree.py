# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque

        if not root:
            return 0

        q = deque([(root, root.val)])
        n = 1

        while q:
            cur, cur_max = q.popleft()

            if cur.left:
                if cur.left.val >= cur_max:
                    n += 1
                q.append([cur.left, max(cur_max, cur.left.val)])

            if cur.right:
                if cur.right.val >= cur_max:
                    n += 1
                q.append([cur.right, max(cur_max, cur.right.val)])

        return n               

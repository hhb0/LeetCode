# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        from collections import deque

        if not root:
            return False

        q = deque([(root, root.val)])

        while q:
            cur_node, cur_sum = q.popleft()

            if not cur_node.left and not cur_node.right:
                if cur_sum == targetSum:
                    return True
            if cur_node.left:
                q.append((cur_node.left, cur_sum+cur_node.left.val))
            if cur_node.right:
                q.append((cur_node.right, cur_sum+cur_node.right.val))

        return False
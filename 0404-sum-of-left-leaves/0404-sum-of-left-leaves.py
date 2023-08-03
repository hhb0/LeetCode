# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        from collections import deque, defaultdict
        if not root:
            return 0
        answer = 0
        q = deque([(root, False)])
        while q:
            cur_node, is_left = q.popleft()
            
            if not cur_node.left and not cur_node.right and is_left == True:
                answer += cur_node.val
            if cur_node.left:
                q.append((cur_node.left, True))
            if cur_node.right:
                q.append((cur_node.right, False))
        return answer
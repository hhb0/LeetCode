# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque, defaultdict

        if not root:
            return []

        q=deque([root])
        ans =[]
        while q:
            n = len(q)
            cur_sum =0

            for i in range(n):
                cur = q.popleft()
                cur_sum += cur.val
                if cur.left: 
                    q.append(cur.left)
                if cur.right: 
                    q.append(cur.right)
            ans.append(cur_sum/n)

        return ans
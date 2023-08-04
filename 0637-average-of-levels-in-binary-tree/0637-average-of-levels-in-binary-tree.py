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

        d = defaultdict(int)
        c = defaultdict(int)
        q = deque([(root, 0)])
        ans = []
        while q:
            cur, level = q.popleft()
            d[level] += cur.val
            c[level] += 1

            if cur.left:
                q.append((cur.left, level+1))
            if cur.right:
                q.append((cur.right, level+1))
   
        for i in range(len(d)):
            ans.append(list(d.values())[i] / list(c.values())[i])
        return ans
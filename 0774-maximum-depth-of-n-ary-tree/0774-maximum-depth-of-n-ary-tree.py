"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        from collections import deque

        if not root:
            return 0

        q = deque([(root, 1)])

        while q:
            cur, level = q.popleft()
            if cur.children:
                for child in cur.children:
                    q.append((child, level+1))

        return level

        
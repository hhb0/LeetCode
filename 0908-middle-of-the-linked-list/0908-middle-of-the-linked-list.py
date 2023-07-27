# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        cur = head
        while (head.next):
            head = head.next
            cnt += 1
            if cnt % 2 == 0:
                cur = cur.next
        if cnt % 2 ==1:
            cur = cur.next
        return cur
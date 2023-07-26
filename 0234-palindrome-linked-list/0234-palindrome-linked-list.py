# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = []
        temp = head
        while temp!= None:
            cur.append(temp.val)
            temp = temp.next
        cur_re = cur.copy()
        cur_re.reverse()
        return True  if cur_re == cur else False
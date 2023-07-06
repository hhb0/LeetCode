# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        cur = head
        while l1 or l2:
            if l1 and l2:
                cur_val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                cur_val = l1.val
                l1 = l1.next
            elif l2:
                cur_val = l2.val
                l2 = l2.next
            # 더해서 계산한 값을 cur.next에 ListNode로 만들어서 추가
            cur_val += carry
            cur.next = ListNode(cur_val % 10)
            cur = cur.next
            # 10이 넘어갈 경우 carry를 1로 설정, 그게 아니면 0으로 설정
            if cur_val >= 10:
                carry = 1
            else:
                carry = 0
        if carry:
            cur.next = ListNode(carry)
        return head.next

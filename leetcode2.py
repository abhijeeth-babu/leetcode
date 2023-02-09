# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        temp = new_head
        carry_over = 0
        while l1 or l2:
            result = carry_over
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next
            carry_over = result // 10
            temp.next = ListNode(result % 10)
            temp = temp.next
        if carry_over:
            temp.next = ListNode(carry_over)
        return new_head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right, left_prev = head, head, None
        for i in range(n):
            right = right.next
        while right:
            right = right.next
            left = left.next
            left_prev = left_prev.next if left_prev else head
        if left_prev:
            left_prev.next = left.next
        else:
            return head.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp1 = head
        temp2 = self.split_list(head)
        new_head = ListNode()
        while temp1 or temp2:
            if temp1:
                new_head.next = temp1
                temp1 = temp1.next
                new_head = new_head.next
            if temp2:
                new_head.next = temp2
                temp2 = temp2.next
                new_head = new_head.next
    
    def split_list(self, head):
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

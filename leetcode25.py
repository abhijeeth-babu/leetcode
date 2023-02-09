# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length, temp = 0, head
        while temp:
            length += 1
            temp = temp.next
        div = length // k
        dummy = ListNode(0, head)
        curr, prev = head, dummy
        for i in range(div):
            count = 0
            curr_last = curr
            prev_last = prev
            while curr and count < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count += 1
            curr_last.next = curr
            prev_last.next = prev
            prev = curr_last
        
        return dummy.next

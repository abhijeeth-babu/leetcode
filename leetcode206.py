class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        return self.helper(head, None)
    
    def helper(self, curr, prev):
            if curr is None:
                return prev
            next_curr = curr.next
            curr.next = prev
            return helper(next_curr, curr)

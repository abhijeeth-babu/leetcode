"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution1:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_dict = {None:None}
        node = head
        while node:
            copy_dict[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            copy = copy_dict[node]
            copy.next = copy_dict[node.next]
            copy.random = copy_dict[node.random]
            node = node.next
        return copy_dict[head]
      
      
class Solution2:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        temp = head
        while temp:
            copy = Node(temp.val)
            nxt = temp.next
            temp.next = copy
            temp.next.next = nxt
            temp = temp.next.next
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        temp = head
        copy = temp.next
        ctemp = copy
        while ctemp.next:
            temp.next = temp.next.next
            temp = temp.next
            ctemp.next = ctemp.next.next
            ctemp = ctemp.next
        return copy

"""
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        if head is None:
            return None

        curr = head
        for i in range(1, x):
            if curr is None:
                return head
            curr = curr.next

        if curr is None:
            return head

        up = curr.next
        down = curr.prev

        # Only one node in list
        if down is None and up is None:
            return None

        # Delete head
        elif down is None:
            head = up
            head.prev = None
            curr.next = None
            return head

        # Delete tail
        elif up is None:
            down.next = None
            curr.prev = None
            return head

        # Delete middle node
        else:
            down.next = up
            up.prev = down
            curr.next = None
            curr.prev = None
            return head
            
        
            
        
        
        
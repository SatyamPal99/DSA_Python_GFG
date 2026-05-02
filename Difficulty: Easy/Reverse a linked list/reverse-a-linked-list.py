"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        up=head
        down=None
        curr=head
        while up!=None:
            up=up.next
            curr.next=down
            down=curr
            curr=up
        head=down
        return head
        
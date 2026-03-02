'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteHead(self, head):
        temp=head
        head=head.next
        temp.next=None
        return head
        
    
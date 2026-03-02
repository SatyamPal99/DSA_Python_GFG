'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
import sys
class Solution:
    def deleteHead(self, head):
        if head==None:
            return None
        temp=head
        head=head.next
        temp.next=None
        return head
        
    
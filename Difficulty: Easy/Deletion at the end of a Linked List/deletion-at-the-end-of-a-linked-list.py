'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def removeLastNode(self, head):
        if head==None:
            return head
        elif head.next==None:
            return None
        temp=head
        prev=temp
        while temp.next != None:
            prev=temp
            temp=temp.next
        prev.next=None
        return head
            
        
        
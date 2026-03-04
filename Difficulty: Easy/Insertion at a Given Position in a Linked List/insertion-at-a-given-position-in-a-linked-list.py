'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):
        temp=head
        prev=None
        new=Node(val)
        if head==None:
            if pos==1:
                new=Node(val)
                return new
            else:
                return None
        if pos==1:
            new=Node(val)
            new.next=head
            return new
        for i in range(0,pos-2):
            temp=temp.next
        
        new.next=temp.next
        temp.next=new
        return head
      
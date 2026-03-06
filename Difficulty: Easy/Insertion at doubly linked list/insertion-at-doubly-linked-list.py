'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        if head==None:
            head=Node(x)
            return head
        curr=head
        for i in range(p):
            if curr==None:
                new=Node(x)
                new.prev=down
                down.next=new
                new.next=None
            curr=curr.next
        down=curr.prev
        up=curr.next
        if curr.next==None:
            new=Node(x)
            new.prev=curr
            curr.next=new
            new.next=None
            return head
        elif curr.prev==None:
            new=Node(x)
            new.prev=curr
            curr.next=new
            new.next=up
            up.prev=new
            return head
        else:
            new=Node(x)
            curr.next=new
            new.prev=curr
            new.next=up
            up.prev=new
            return head
            
            
            
            
            
                
        
'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        temp1=head1
        temp2=head2
        head=Node(-1)
        temp=head
        while(temp1!=None and temp2!=None):
            if temp1.data<temp2.data:
                temp.next=temp1
                temp1=temp1.next
                temp=temp.next
            elif temp1.data>temp2.data:
                temp.next=temp2
                temp2=temp2.next
                temp=temp.next 
            else:
                temp.next=temp1
                temp1=temp1.next
                temp=temp.next
                temp.next=temp2
                temp2=temp2.next
                temp=temp.next
            
        if temp1==None:
            temp.next=temp2
            
        elif temp2==None:
            temp.next=temp1
        return head.next
        
        
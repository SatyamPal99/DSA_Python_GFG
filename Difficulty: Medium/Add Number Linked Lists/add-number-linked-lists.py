'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):
        lis1=[]
        lis2=[]
        while head1 or head2:
            if head1:
                lis1.append(head1.data)
                head1=head1.next
            if head2:
                lis2.append(head2.data)
                head2=head2.next
        carry=0
        dummy=Node(-1)
        curr=dummy
        while lis1 or lis2:
            sum=carry
            if lis1:
                sum=sum+lis1.pop()
            if lis2:
                sum=sum+lis2.pop()
            value=sum%10
            carry=sum//10
            new=Node(value)
            curr.next=new
            curr=curr.next
        if(carry):
            new=Node(carry)
            curr.next=new
            curr=curr.next
        #return dummy.next
        curr=dummy.next
        dummy.next=None
        up=curr.next
        back=None
        while curr!=None:
            curr.next=back
            back=curr
            curr=up
            if curr==None:
                break
            up=up.next
        while back and back.data==0:
            back=back.next
        
        return back
            
            
            
            
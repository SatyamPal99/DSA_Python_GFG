'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        """head1=self.reverse(head)
        carry=1
        curr=head1
        while curr:
            val=curr.data+carry
            if val<10:
                curr.data=val
                carry=0
                break
            else:
                carry=1
                curr.data=0
            curr=curr.next
        
        if carry==1:
            new=Node(1)
            head1=self.reverse(head1)
            new.next=head1
            return new
        head1=self.reverse(head1)
        return head1
                
        
        
        
    def reverse(self,head):
        temp=head
        pre=None
        curr=head
        while temp:
            curr=curr.next
            temp.next=pre
            pre=temp
            temp=curr
        return pre"""
        
    # Optimized Approach using Recursion
        carry=1
        ans=self.fun(head)
        if ans==1:
            new=Node(1)
            new.next=head
            return new
        return head
        
    def fun(self,head):
        if head==None:
            return 1
        
        
        carry=self.fun(head.next)
        sum=carry+head.data
        if sum<10:
            head.data=sum
            return 0
        else:
            head.data=0
            return 1
        return head
            
    
    
    
    
    
            
            
'''
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    """def mergeKLists(self, arr):
        n=len(arr)
        head=arr[0]
        for i in range(1,n):
            head=self.fun(head,arr[i])
        return head
    
    
    def fun(self,head1,head2):
        dummy=Node(-1)
        temp=dummy
        if head1==None:
            return head2
        if head2==None:
            return head1
        while head1!=None and head2!=None:
            
            if (head1.data<head2.data):
                temp.next=head1
                head1=head1.next
                temp=temp.next
            elif head1.data>head2.data:
                temp.next=head2
                head2=head2.next
                temp=temp.next
            else:
                temp.next=head1
                head1=head1.next
                temp=temp.next
                temp.next=head2
                head2=head2.next
                temp=temp.next
        if head1==None:
            temp.next=head2
        else:
            temp.next=head1
        return dummy.next"""
        
        
    def mergeKLists(self, arr):
        # code here
        result_arr=[]
        for i in range(len(arr)):
            cur=arr[i]
            while cur is not None:
                result_arr.append(cur.data)
                cur=cur.next
        result_arr.sort()
        dummy=Node(-1)
        curr=dummy
        
        for value in result_arr:
            curr.next=Node(value)
            curr=curr.next
        
        return dummy.next
            
            
        
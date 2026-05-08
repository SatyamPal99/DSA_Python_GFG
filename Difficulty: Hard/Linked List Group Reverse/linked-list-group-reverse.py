"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        temp=head
        prev=None
        while temp!=None:
            kth=self.findKth(temp,k)
            if kth==None:
                last=self.reverse(nextNode)
                prev.next=last
                break
            nextNode=kth.next
            kth.next=None
            self.reverse(temp)
            if(head==temp):
                head=kth
            else:
                prev.next=kth
            prev=temp
            temp=nextNode
        return head
        
    def reverse(self,temp):
        curr=temp
        prev=None
        while curr!=None:
            curr=curr.next
            temp.next=prev
            prev=temp
            temp=curr
        return prev
    def findKth(self,temp,k):
        k=k-1
        while(temp!=None and k>0):
            k-=1
            temp=temp.next
        return temp
        
        
        
        
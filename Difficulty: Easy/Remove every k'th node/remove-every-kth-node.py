#Your task is to complete this function
#Your function should return the new head pointer
'''
class node:
    def __init__(self,x):
        self.data = x
        self.next = None
'''

class Solution:
    def deleteK(self, head, k):
        temp=head
        count=0
        prev=None
        while temp!=None:
            count+=1
            if count==k:
                prev.next=prev.next.next
                count=0
            prev=temp
            temp=temp.next
        return head
                
                
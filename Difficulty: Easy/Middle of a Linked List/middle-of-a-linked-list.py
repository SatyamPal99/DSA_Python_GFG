'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        mid=(count//2)+1
        curr=head
        while mid-1:
            curr=curr.next
            mid-=1
        return curr.data
            

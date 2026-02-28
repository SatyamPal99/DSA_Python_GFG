'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        temp=head
        count=0
        while temp.next != None:
            temp=temp.next
            count+=1
        return count+1
        
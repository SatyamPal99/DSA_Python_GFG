'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        temp=head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        return arr[count//2]
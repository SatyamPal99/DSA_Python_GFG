'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def printList(self, head):
        arr=[]
        temp=head
        while temp is not None:
            arr.append(temp.data)
            temp=temp.next
        return arr
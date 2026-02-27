'''
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def arrayToList(self, arr):
        head=Node(arr[0])
        mover=head
        for i in range(1, len(arr)):
            temp=Node(arr[i])
            mover.next=temp
            mover=temp
        return head
        
        
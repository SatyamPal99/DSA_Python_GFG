'''
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def arrayToList(self, arr):
        n=len(arr)
        head=Node(arr[0])
        temp=head
        for i in range(1,n):
            new=Node(arr[i])
            temp.next=new
            temp=new
        return head
            
        
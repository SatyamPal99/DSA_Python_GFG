#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        head=Node(arr[0])
        temp=head
        for i in range(1, len(arr)):
            new=Node(arr[i])
            temp.next=new
            new.prev=temp
            temp=temp.next
        return head
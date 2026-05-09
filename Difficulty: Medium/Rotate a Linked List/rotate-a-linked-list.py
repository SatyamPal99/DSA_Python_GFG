'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def rotate(self, head, k):
        if head==None or head.next==None:
            return head
        n=1
        tail=head
        while tail.next!=None:
            tail=tail.next
            n+=1
        tail.next=head
        k=k%n
        if k==0:
            tail.next=None
            return head
        tail=head
        for _ in range(1,k):
            tail=tail.next
        newhead=tail.next
        tail.next=None
        return newhead
            
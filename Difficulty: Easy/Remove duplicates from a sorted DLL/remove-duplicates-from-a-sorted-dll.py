'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    def removeDuplicates(self, head):
        temp1=temp2=head
        temp2=temp2.next
        pre=head
        while(temp2!=None):
            if temp1.data==temp2.data:
                pre=temp2
                temp2=temp2.next
            else:
                temp1.next=pre.next
                temp1=temp1.next
                pre=temp1
                temp2=temp2.next
        temp1.next=pre.next
        return head
            
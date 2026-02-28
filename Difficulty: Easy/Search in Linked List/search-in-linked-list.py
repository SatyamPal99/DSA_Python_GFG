'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        temp=head
        if temp.next==None and temp.data==key:
            return True
        elif temp.next==None and temp.data!=key:
            return False
        while temp.next != None:
            if temp.data==key:
                return True
            else:
                temp=temp.next
        if temp.next==None and temp.data==key:
            return True
        else:
            return False
            
        
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        up=head
        down=head
        while(up!=None and up.next!=None):
            down=down.next
            up=up.next.next
            if (up==down):
                return True
        return False
        
        

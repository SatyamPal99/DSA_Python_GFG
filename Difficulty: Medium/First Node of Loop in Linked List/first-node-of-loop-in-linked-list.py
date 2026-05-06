"""
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
"""

class Solution:
    def cycleStart(self, head):
        temp=head
        d={}
        while temp!=None:
            if temp in d:
                return temp.data
            d[temp]=d.get(temp,0)+1
            temp=temp.next
        return -1
            
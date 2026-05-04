'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        d={}
        temp=head
        count=0
        while temp!=None:
            if temp in d:
                return count-d[temp]
            else:
                d[temp]=count
                count+=1
                temp=temp.next
        return 0
            
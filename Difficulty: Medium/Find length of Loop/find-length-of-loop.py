'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        """d={}
        temp=head
        count=0
        while temp!=None:
            if temp in d:
                return count-d[temp]
            else:
                d[temp]=count
                count+=1
                temp=temp.next
        return 0"""
        
        #optimized approach 
        
        slow=fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return self.find_num(slow, fast)
        return 0
        
    def find_num(self,slow,fast):
        count=1
        fast=fast.next
        while fast!=slow:
            count+=1
            fast=fast.next
        return count
        
        
        
        
        
        
            
from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        """temp1=head
        arr=[]
        while(temp1!=None):
            temp2=temp1.next
            while temp2!=None and temp1.data+temp2.data<=target:
                if (temp1.data+temp2.data)==target:
                    arr.append([temp1.data,temp2.data])
                temp2=temp2.next
            temp1=temp1.next
        return arr"""
        
        left=head
        right=head
        arr=[]
        while right.next!=None:
            right=right.next
        while left.data<right.data:
            if left.data+right.data>target:
                right=right.prev
            elif left.data+right.data<target:
                left=left.next
            else:
                arr.append([left.data, right.data])
                left=left.next
                right=right.prev
        return arr
            
                    
                    
                    
                    
                    
                    
                    
                    

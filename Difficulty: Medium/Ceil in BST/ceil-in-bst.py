'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''

class Solution:
    def findCeil(self,root, x):
        ans=-1
        while root:
            if root.data>x:
                ans=root.data
                root=root.left
            elif root.data<x:
                root=root.right
            else:
                ans=root.data
                return ans
        return ans
                
        
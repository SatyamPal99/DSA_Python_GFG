'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isBalanced(self, root):
        """ans=self.fun(root)
        if ans==-1:
            return False
        else:
            return True"""
            
        if not root:
           return 1
       
        left_height = self.isBalanced(root.left)
        right_height = self.isBalanced(root.right)
        if left_height == 0 or right_height == 0 or abs(left_height - right_height) > 1:
            return False
        return 1 + max(left_height, right_height)
        
        
    def fun(self,root):
        if root==None:
            return 0
        l=self.fun(root.left)
        r=self.fun(root.right)
        if l==-1 or r==-1:
            return -1
        if abs(l-r)>1:
            return -1
        return 1+max(l,r)
        
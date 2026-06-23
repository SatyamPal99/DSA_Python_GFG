'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isSymmetric(self, root):
        return self.fun(root.left,root.right)
        
    def fun(self,leftt,rightt):
        if leftt==None or rightt==None:
            return leftt==rightt
        if leftt.data!=rightt.data:
            return False
        
        t1=self.fun(leftt.left,rightt.right)
        t2=self.fun(leftt.right,rightt.left)
        return t1 and t2
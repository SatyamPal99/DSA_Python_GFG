''' Structure of a Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
import math
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def largestBst(self, root):
        self.maxSize=0
        self.helper(root)
        return self.maxSize
        
    def helper(self,root):
        if root==None:
            return [math.inf,-math.inf,0]
        left=self.helper(root.left)
        right=self.helper(root.right)
        if left[1]<root.data<right[0]:
            size=left[2]+right[2]+1
            self.maxSize=max(self.maxSize,size)
            return [min(left[0],root.data),max(right[1],root.data),size]
        return [-math.inf,math.inf,0]
        
        
        
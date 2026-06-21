"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def Paths(self, root):
        ans=[]
        temp=[]
        self.fun(root,ans,temp)
        
        return ans
        
        
    def fun(self,root,ans,temp):
        if root==None:
            return  
        
        temp.append(root.data)
        
        if root.left==None and root.right==None:
            ans.append(temp[:])
            temp.pop()
            return
        
        self.fun(root.left,ans,temp)
        self.fun(root.right,ans,temp)
        temp.pop()
        return
        
        
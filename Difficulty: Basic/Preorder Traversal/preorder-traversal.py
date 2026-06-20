'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preOrder(self, root):
        ans=[]
        self.fun(root,ans)
        return ans
    def fun(self,root,ans):
        if root==None:
            return 
        ans.append(root.data)
        self.fun(root.left,ans)
        self.fun(root.right,ans)
        return ans
    
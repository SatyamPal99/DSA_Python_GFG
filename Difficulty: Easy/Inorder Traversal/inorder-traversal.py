'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self, root):
        ans=[]
        self.fun(root,ans)
        return ans
    def fun(self,root,ans):
        if root==None:
            return ans
        self.fun(root.left,ans)
        ans.append(root.data)
        self.fun(root.right,ans)
        return ans
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        ans=[]
        self.fun(root,ans)
        return ans
    def fun(self,root,ans):
        if root==None:
            return
        
        self.fun(root.left,ans)
        self.fun(root.right,ans)
        ans.append(root.data)
        return ans
        
        
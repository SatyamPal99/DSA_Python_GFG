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
        """ans=[]
        self.fun(root,ans)
        return ans"""
        
        curr=root
        ans=[]
        while curr:
            if curr.left==None:
                ans.append(curr.data)
                curr=curr.right
            else:
                predecessor=self.find_pred(curr)
                if predecessor.right==None:
                    ans.append(curr.data)
                    predecessor.right=curr
                    curr=curr.left
                else:
                    predecessor.right=None
                    curr=curr.right
        return ans
                    
                
                
    def find_pred(self,root):
        pred=root.left
        while pred.right and pred.right!=root:
            pred=pred.right
        return pred
        
        
        
    def fun(self,root,ans):
        if root==None:
            return 
        ans.append(root.data)
        self.fun(root.left,ans)
        self.fun(root.right,ans)
        return ans
    
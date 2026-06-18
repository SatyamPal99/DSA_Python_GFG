'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        res=[]
        if root==None:
            return res
        if root.left==None and root.right==None:
            res.append(root.data)
            return res
        res.append(root.data)
        self.left(root,res)
        self.leaf(root,res)
        self.rightToNonleaf(root.right,res)
        return res
        
    def left(self,root,res):
        root=root.left
        while root:
            if root.left!=None or root.right!=None:
                res.append(root.data)
            if root.left:
                root=root.left
            else:
                root=root.right
    def leaf(self,root,res):
        if root.left==None and root.right==None:
            res.append(root.data)
            return res
        
        if root.left:
            self.leaf(root.left,res)
        if root.right:
            self.leaf(root.right,res)
        
    def rightToNonleaf(self,root,res):
        
        temp=[]
        while root:
            if root.left!=None or root.right!=None:
                temp.append(root.data)
            if root.right:
                root=root.right
            else:
                root=root.left
        for i in range(len(temp)-1,-1,-1):
            res.append(temp[i])
        
        
        
        
        
        
        
                
                
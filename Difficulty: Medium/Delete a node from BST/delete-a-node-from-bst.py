# Structure of a Tree Node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def delNode(self, root, x):
        if root==None:
            return None
        if root.data==x:
            return self.helper(root,x)
        curr=root
        while curr:
            if curr.data>x:
                if curr.left!=None and curr.left.data==x:
                    curr.left=self.helper(curr.left,x)
                    
                else:
                    curr=curr.left
            else:
                if curr.right!=None and curr.right.data==x:
                    curr.right=self.helper(curr.right,x)
                else:
                    curr=curr.right
        return root
    
    def helper(self,curr,x):
        if curr.left==None:
            return curr.right
        if curr.right==None:
            return curr.left
        right_child=curr.right
        predecessor=self.find(curr)
        predecessor.right=right_child
        return curr.left
                
                    
                    
                    
    def find(self,curr):
        pred=curr.left
        while pred.right:
            pred=pred.right
        return pred
                    
        
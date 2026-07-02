'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def insert(self, root, key):
        # Recursive way
        """if root==None:
            return Node(key)
        if key<root.data:
            root.left=self.insert(root.left,key)
        if key>root.data:
            root.right=self.insert(root.right,key)
        return root"""
        
        # Iterative way
        
        if root==None:
            return Node(key,None,None)
        curr=root
        while curr:
            if curr.data>key:
                if curr.left==None:
                    new=Node(key)
                    curr.left=new
                    return root
                curr=curr.left
            elif curr.data<key:
                if curr.right==None:
                    new=Node(key)
                    curr.right=new
                    return root
                curr=curr.right
                
        
        
        
        
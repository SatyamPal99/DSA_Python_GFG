'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def search(self, root, key):
        if root==None:
            return 
        if key<root.data:
            return self.search(root.left,key)
        elif key>root.data:
            return self.search(root.right,key)
        else:
            return True
            
        
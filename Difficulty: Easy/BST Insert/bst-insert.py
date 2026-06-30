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
        if root==None:
            return Node(key)
        if key<root.data:
            root.left=self.insert(root.left,key)
        if key>root.data:
            root.right=self.insert(root.right,key)
        return root
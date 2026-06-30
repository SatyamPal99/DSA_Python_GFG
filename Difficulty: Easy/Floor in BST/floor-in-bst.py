'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        ans=-1
        while root:
            if root.data==k:
                return root.data
            if root.data<k:
                ans=root.data
            if root.data<k:
                root=root.right
            else:
                root=root.left
        return ans
        
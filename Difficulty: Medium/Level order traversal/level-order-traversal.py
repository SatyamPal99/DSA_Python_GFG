# A binary tree Node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root):
        q=deque()
        q.append(root)
        ans=[]
        while q:
            temp=q.popleft()
            ans.append(temp.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return ans
            
        
        
        
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import defaultdict,deque
class Solution:
    def topView(self, root):
        mapp={}
        q=deque()
        q.append((root,0))
        while q:
            temp=q.popleft()
            node=temp[0]
            x=temp[1]
            if x not in mapp:
                mapp[x]=node.data
            if node.left:
                q.append((node.left,x-1))
            if node.right:
                q.append((node.right,x+1))
        ans=[]
        for x in sorted(mapp):
            ans.append(mapp[x])
        return ans
        
        
        
        
        
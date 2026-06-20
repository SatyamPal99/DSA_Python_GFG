''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

class Solution:
    def leftView(self, root):
        if root==None:
            return []
        q=deque()
        q.append((0,root))
        mapp={}
        while q:
            temp=q.popleft()
            level=temp[0]
            value=temp[1]
            if level not in mapp:
                mapp[level]=value.data
            if value.left:
                q.append((level+1,value.left))
            if value.right:
                q.append((level+1,value.right))
        ans=[]
        for i in sorted(mapp):
            ans.append(mapp[i])
        return ans
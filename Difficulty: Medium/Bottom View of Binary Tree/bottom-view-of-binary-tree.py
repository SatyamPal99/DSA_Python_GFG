'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        q=deque()
        mapp={}
        q.append((0,root))
        while q:
            temp=q.popleft()
            verticle=temp[0]
            value=temp[1]
            mapp[verticle]=value.data
            if value.left:
                q.append((verticle-1,value.left))
            if value.right:
                q.append((verticle+1,value.right))
        ans=[]
        for i in sorted(mapp):
            ans.append(mapp[i])
        return ans
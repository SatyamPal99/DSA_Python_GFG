'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def zigZagTraversal(self, root):
        ans=[]
        q=deque()
        q.append(root)
        flag=True
        while q:
            size=len(q)
            res=[0]*size
            for i in range(size):
                temp=q.popleft()
                idx=i if flag else size-i-1
                res[idx]=temp.data
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            flag = not flag
            ans.extend(res)
        return ans
        
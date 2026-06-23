'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        q=deque()
        q.append(root)
        while q:
            temp=q.popleft()
            sum=0
            if temp.left==None and temp.right==None:
                continue
            if temp.left:
                sum=sum+temp.left.data
            if temp.right:
                sum=sum+temp.right.data
            if sum!=temp.data:
                return False
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return True
                    
                    
                    
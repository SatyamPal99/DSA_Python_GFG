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
        """q=deque()
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
        return True"""
        
        #using Recursion(od DFS)
        
        value,ans=self.fun(root)
        return ans
        
    def fun(self,root):
        if root==None:
            return 0,1
        if root.left==None and root.right==None:
            return root.data,1
        
        left,isL=self.fun(root.left)
        right,isR=self.fun(root.right)
        if left+right==root.data:
            if isL and isR:
                return root.data,1
        return root.data,0
        
        
        
                    
                    
                    
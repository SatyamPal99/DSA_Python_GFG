'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def minTime(self, root, target):
        if root==None:
            return 0
        mapp={}
        self.parent(root,mapp)
        q=deque()
        tar=self.find_tar(root,target)
        visited=set()
        visited.add(tar)
        q.append(tar)
        ans=0
        while q:
            for i in range(len(q)):
                temp=q.popleft()
                if temp.left and temp.left not in visited:
                    q.append(temp.left)
                    visited.add(temp.left)
                if temp.right and temp.right not in visited:
                    q.append(temp.right)
                    visited.add(temp.right)
                if temp in mapp and mapp[temp] not in visited:
                    q.append(mapp[temp])
                    visited.add(mapp[temp])
            ans+=1
        return ans-1
        
    def find_tar(self,root,tar):
        if root==None:
            return 
        if root.data==tar:
            return root
        a1=self.find_tar(root.left,tar)
        a2=self.find_tar(root.right,tar)
        if a1!=None:
            return a1
        else:
            return a2
        
    def parent(self,root,mapp):
        q=deque()
        q.append(root)
        while q:
            temp=q.popleft()
            if temp.left:
                mapp[temp.left]=temp
                q.append(temp.left)
            if temp.right:
                mapp[temp.right]=temp
                q.append(temp.right)
        
            
                
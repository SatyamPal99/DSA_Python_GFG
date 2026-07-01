'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def serialize(self, root):
        if root==None:
            return []
        ans=[]
        q=deque()
        q.append(root)
        while q:
            temp=q.popleft()
            if temp==None:
                ans.append(-999)
            else:
                ans.append(temp.data)
                q.append(temp.left)
                q.append(temp.right)
        return ans
        
                
                

    def deSerialize(self, arr):
        
        if len(arr)==0:
            return
        root=Node(arr[0])
        q=deque()
        q.append(root)
        i=1
        while q:
            curr=q.popleft()
            if arr[i]!=-999:
                curr.left=Node(arr[i])
                q.append(curr.left)
            i+=1
            if arr[i]!=-999:
                curr.right=Node(arr[i])
                q.append(curr.right)
            i+=1
        return root
        
            
            
        
        
        
        
        
    
'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrderSuccessor(self, root, k):
        curr=root
        ans=[]
        while curr:
            if curr.left==None:
                ans.append(curr.data)
                curr=curr.right
            else:
                pred=self.find_pred(curr)
                if pred.right==None:
                    pred.right=curr
                    curr=curr.left
                else:
                    ans.append(curr.data)
                    pred.right=None
                    curr=curr.right
        #print(ans)
        res=-1
        for i in ans:
            if i>k.data:
                return i
        return res
                
                
            
                    
                
                
    def find_pred(self,curr):
        pred=curr.left
        while pred.right and pred.right!=curr:
            pred=pred.right
        return pred
                
        
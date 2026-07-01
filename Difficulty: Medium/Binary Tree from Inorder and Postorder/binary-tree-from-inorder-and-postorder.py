""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
"""

class Solution:
    def buildTree(self, inorder, postorder):
        mapp={}
        for i in range(len(inorder)):
            if inorder[i] not in mapp:
                mapp[inorder[i]]=i
        ans=self.fun(postorder,0,len(postorder)-1,inorder,0,len(inorder)-1,mapp)
        return ans
        
        
    def fun(self,postorder,post_start,post_end,inorder,in_start,in_end,mapp):
        if post_start>post_end or in_start>in_end:
            return None
        root=Node(postorder[post_end])
        in_root=mapp[root.data]
        left_nums=in_root-in_start
        root.left=self.fun(postorder,post_start,post_start+left_nums-1,inorder,in_start,in_root-1,mapp)
        root.right=self.fun(postorder,post_start+left_nums,post_end-1,inorder,in_root+1,in_end,mapp)
        return root
        
        
'''  Structure of a Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def buildTree(self, inorder, preorder):
        mapp={}
        for i in range(len(inorder)):
            mapp[inorder[i]]=i
        return self.fun(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,mapp)
        
        
    def fun(self,pre,pre_start,pre_end,inorder,in_start,in_end,mapp):
        if pre_start>pre_end or in_start>in_end:
            return None
        node=Node(preorder[pre_start])
        in_root=mapp[node.data]
        left_num=in_root-in_start
        node.left=self.fun(pre,pre_start+1,left_num+pre_start,inorder,in_start,in_root-1,mapp)
        node.right=self.fun(pre,left_num+pre_start+1,pre_end,inorder,in_root+1,in_end,mapp)
        return node
class Solution:

    def countNodes(self, root):
        # Bruteforce --> any traversal (inorder,preorder,postorder)
        if root==None:
            return 0
        ans1=self.countNodes(root.left)
        ans2=self.countNodes(root.right)
        return 1+ans1+ans2
            
        
#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    # Return a list containing the post order traversal of the given tree
    def postOrder(self,node):
        # Using two stack
        """st1=[node]
        st2=[]
        while st1:
            temp=st1.pop()
            st2.append(temp.data)
            if temp.left!=None:
                st1.append(temp.left)
            if temp.right!=None:
                st1.append(temp.right)
        return st2[::-1]"""
        
        # using reverse of postoreder [left right root] --> [root,left,right] 
        
        st=[root]
        ans=[]
        while st:
            temp=st.pop()
            ans.append(temp.data)
            if temp.left!=None:
                st.append(temp.left)
            if temp.right!=None:
                st.append(temp.right)
            
        return ans[::-1]
            
        
        
        
        
        
        
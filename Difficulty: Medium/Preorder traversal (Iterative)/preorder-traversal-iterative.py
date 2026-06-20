'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preOrder(self, root):
        st=[]
        st.append(root)
        ans=[]
        while st:
            temp=st.pop()
            ans.append(temp.data)
            if temp.right:
                st.append(temp.right)
            if temp.left:
                st.append(temp.left)
        return ans
            
            
        
# Definition for Node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def inOrder(self, root):
        """st=[]
        ans=[]
        temp=root
        while True:
            if temp!=None:
                st.append(temp)
                temp=temp.left
            else:
                if len(st)==0:
                    break
                temp=st.pop()
                ans.append(temp.data)
                temp=temp.right
        return ans"""
        
        # Method2 using visited array...
        
        st=[root]
        visited=[0]
        ans=[]
        while st:
            temp=st.pop()
            flag=visited.pop()
            if not flag:
                if temp.right!=None:
                    st.append(temp.right)
                    visited.append(0)
                st.append(temp)
                visited.append(1)
                if temp.left!=None:
                    st.append(temp.left)
                    visited.append(0)
            else:
                ans.append(temp.data)
        return ans
            
            
            
        
        
        
        
        
        
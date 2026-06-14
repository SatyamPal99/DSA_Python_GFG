# Definition for Node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def inOrder(self, root):
        st=[]
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
        return ans
        
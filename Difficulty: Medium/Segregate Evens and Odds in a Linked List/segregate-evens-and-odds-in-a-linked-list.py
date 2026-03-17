# User function Template for Python3

# Following is the structure of node 
# class node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, head):
        st=[]
        curr=head
        while curr:
            if (curr.data)%2==0:
                st.append(curr.data)
            curr=curr.next
        curr=head
        while curr:
            if (curr.data)%2==1:
                st.append(curr.data)
            curr=curr.next
        curr=head
        while curr:
            curr.data=st.pop(0)
            curr=curr.next
        return head
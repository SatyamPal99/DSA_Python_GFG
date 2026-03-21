'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        st=[]
        curr=head
        while curr:
            st.append(curr.data)
            curr=curr.next
        curr=head
        while curr:
            if curr.data==st.pop():
                curr=curr.next
            else:
                return False
        return True
        
        
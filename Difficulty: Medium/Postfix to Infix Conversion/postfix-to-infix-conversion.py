#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        st=[]
        for i in postfix:
            if i.isalpha():
                st.append(i)
            else:
                t1=st.pop()
                t2=st.pop()
                ans="("+t2+i+t1+")"
                st.append(ans)
        return st.pop()
                
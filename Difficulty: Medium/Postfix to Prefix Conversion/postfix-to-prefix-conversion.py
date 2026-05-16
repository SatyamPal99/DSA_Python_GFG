class Solution:
    def postToPre(self, s):
        st=[]
        for i in s:
            if i.isalpha():
                st.append(i)
            else:
                t1=st.pop()
                t2=st.pop()
                st.append(i+t2+t1)
        return st.pop()
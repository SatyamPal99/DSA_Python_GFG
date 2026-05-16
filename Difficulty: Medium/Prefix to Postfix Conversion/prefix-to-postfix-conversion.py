class Solution:
    def preToPost(self, s):
        st=[]
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                st.append(s[i])
            else:
                t1=st.pop()
                t2=st.pop()
                st.append(t1+t2+s[i])
        return st.pop()
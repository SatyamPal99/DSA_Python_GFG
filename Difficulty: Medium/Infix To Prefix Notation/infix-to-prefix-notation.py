class Solution:
    def infixToPrefix(self, s):
        a=""
        for i in range(len(s)-1,-1,-1):
            if s[i]==")":
                a=a+"("
            elif s[i]=="(":
                a=a+")"
            else:
                a=a+s[i]
        ans=""
        st=[]
        for i in a:
            if i.isalnum():
                ans=ans+i
            elif i=="(":
                st.append(i)
            elif i==")":
                while st and st[-1]!="(":
                    ans=ans+st.pop()
                if st:
                    st.pop()
            else:
                while st and st[-1]!="(" and (self.prec(i)<self.prec(st[-1]) or (self.prec(i)==self.prec(st[-1]) and self.isRightAssociative(i))) :   
                    ans=ans+st.pop()
                st.append(i)
        while st:
            ans=ans+st.pop()
        return "".join(ans[::-1])
    
    def prec(self,temp):
        if temp=="^":
            return 3
        elif temp in "+-":
            return 1
        elif temp in "*/":
            return 2
        else:
            return -1
    def isRightAssociative(self,curr):
        return curr=="^"
                
                
        
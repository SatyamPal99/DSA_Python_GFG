class Solution:
    def infixtoPostfix(self, s):
        i=0
        st=[]
        ans=""
        while i<len(s):
            if ((s[i]>='A' and s[i]<='Z') or 
            (s[i]>='a' and s[i]<='z') or
            (s[i]>='0' and s[i]<='9')):
                ans=ans+s[i]
            elif s[i]=="(":
                st.append(s[i])
            elif s[i]==")":
                while(st and st[-1]!='('):
                    ans=ans+st.pop()
                st.pop()
            else:
                while st and st[-1] != '(' and \
                (self.prec(st[-1]) > self.prec(s[i]) or (self.prec(st[-1]) == self.prec(s[i]) \
                                    and not self.isRightAssociative(s[i]))):
                    ans=ans+st.pop()
                st.append(s[i])
            i+=1
        while st:
            ans=ans+st.pop()
        return ans
        
    def prec(self,temp):
        if temp=='^':
            return 3
        elif temp=='*' or temp=="/":
            return 2
        elif temp=="+" or temp=="-":
            return 1
            
        else:
            return -1
    def top(self,st):
        return st[-1]
    def isRightAssociative(self,c):
        return c == '^'
        
                    
                    
        
        
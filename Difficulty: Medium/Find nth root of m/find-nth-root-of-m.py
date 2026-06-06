class Solution:
    def nthRoot(self, n, m):
        if m==0:
           return 0
        for i in range(1,m+1):
            if self.fun(n,i)==m:
                return i
        return -1
           
    def fun(self,n,x):
        ans=1
        while(n>0):
            if n%2==1:
                ans=ans*x
                n=n-1
            else:
                x=x*x
                n=n//2
        return ans
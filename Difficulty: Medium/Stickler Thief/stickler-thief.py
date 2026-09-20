class Solution:  
    def findMaxSum(self, arr):
        n=len(arr)
        dp=[-1]*(n+1)
        return self.fun(arr,n-1,dp)
        #print(dp)
        
    def fun(self,arr,n,dp):
        if n==0:
            return arr[n]
        if n<0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        pick=arr[n]+self.fun(arr,n-2,dp)
        not_pick=0+self.fun(arr,n-1,dp)
        
        dp[n]=max(pick,not_pick)
        return dp[n]
        
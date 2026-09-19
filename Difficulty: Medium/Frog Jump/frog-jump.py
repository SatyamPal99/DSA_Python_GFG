import math
class Solution:
    def minCost(self, height: list[int]) -> int:
        n=len(height)
        dp=[-1]*(n+1)
        return self.fun(n-1,height,dp)
        
    def fun(self,n,arr,dp):
        if n==0:
            return 0
        elif n<0:
            return math.inf
            
        if dp[n]!=-1:
            return dp[n]
        left=self.fun(n-1,arr,dp)+abs(arr[n]-arr[n-1])
        right=self.fun(n-2,arr,dp)+abs(arr[n]-arr[n-2])
        
        dp[n]=min(left,right)
        
        return dp[n]
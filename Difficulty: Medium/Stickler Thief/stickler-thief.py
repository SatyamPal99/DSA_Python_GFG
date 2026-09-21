import math
class Solution:  
    def findMaxSum(self, arr):
        """n=len(arr)
        dp=[-1]*(n+1)
        return self.fun(arr,n-1,dp)"""
        
        
        #print(dp)
        
        #Tabular DP
        n=len(arr)
        if n==1:
            return arr[0]
        if n==2:
            return max(arr[0],arr[1])
        if n==3:
            return max(arr[0],arr[1],max(arr[1],arr[0]+arr[2]))
        
        dp=[-1]*(n+1)
        dp[0]=arr[0]
        dp[1]=arr[1]
        dp[2]=max(dp[1],dp[0]+arr[2])
        ans=-(math.inf)
            
        for i in range(3,n):
            dp[i]=max(dp[i-2]+arr[i],dp[i-3]+arr[i])
            ans=max(ans,dp[i])
        return ans
        
        
    """def fun(self,arr,n,dp):
        if n==0:
            return arr[n]
        if n<0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        pick=arr[n]+self.fun(arr,n-2,dp)
        not_pick=0+self.fun(arr,n-1,dp)
        
        dp[n]=max(pick,not_pick)
        return dp[n]"""
        
class Solution:
    def maximumPoints(self, mat):
        n=len(mat)
        dp=[[-1]*4 for _ in range(n)]
        return self.fun(n-1,3,mat,dp)
        
    def fun(self,n,last,mat,dp):
        if n==0:
            maxi=0
            for i in range(0,3):
                if i!=last:
                    maxi=max(maxi,mat[0][i])
            return maxi
            
        if dp[n][last]!=-1:
            return dp[n][last]
            
        maxi=0
        for i in range(0,3):
            if i!=last:
                score=self.fun(n-1,i,mat,dp)+mat[n][i]
                maxi=max(maxi,score)
        dp[n][last]=maxi
        return dp[n][last]
                    
        
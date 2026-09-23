class Solution:
    def maximumPoints(self, mat):
        n=len(mat)
        """dp=[[-1]*4 for _ in range(n)]
        return self.fun(n-1,3,mat,dp)"""
        
        # Tabulation (bottom-up)
        
        dp=[[-1]*4 for _ in range(n)]
        dp[0][0]=max(mat[0][1],mat[0][2])
        dp[0][1]=max(mat[0][0],mat[0][2])
        dp[0][2]=max(mat[0][0],mat[0][1])
        dp[0][3]=max(mat[0][1],max(mat[0][1],mat[0][2]))
        
        for day in range(1,n):
            for last in range(4):
                dp[day][last]=0
                for task in range(3):
                    if task!=last:
                        score=mat[day][task]+dp[day-1][task]
                        dp[day][last]=max(dp[day][last],score)
        return dp[n-1][3]
                
        
        
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
                    
        
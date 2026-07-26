class Solution:
    def cntOnes(self, grid):
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        for i in range(0,m):
            if grid[0][i]==1:
                self.dfs(grid,vis,0,i)
            if grid[n-1][i]==1:
                self.dfs(grid,vis,n-1,i)
        for i in range(0,n):
            if grid[i][0]==1:
                self.dfs(grid,vis,i,0)
            if grid[i][m-1]==1:
                self.dfs(grid,vis,i,m-1)
        ans=0
        for i in range(0,n):
            for j in range(0,m):
                if vis[i][j]==0 and grid[i][j]==1:
                    ans+=1
        return ans
                
                
                
    def dfs(self,grid,vis,row,col):
        vis[row][col]=1
        drow=[0,0,-1,1]
        dcol=[1,-1,0,0]
        for i in range(4):
            nrow=row+drow[i]
            ncol=col+dcol[i]
            if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]==1 and vis[nrow][ncol]==0:
                self.dfs(grid,vis,nrow,ncol)
                
                
                
                
                
        
            
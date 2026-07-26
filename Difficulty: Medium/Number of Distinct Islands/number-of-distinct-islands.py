from typing import List
class Solution:
    def countDistinctIslands(self, grid):
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        s=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='L' and vis[i][j]==0:
                    temp=[]
                    self.dfs(grid,vis,i,j,i,j,temp)
                    s.add(tuple(temp))
        return len(s)
                    
    def dfs(self,grid,vis,row,col,row0,col0,temp):
        vis[row][col]=1
        temp.append((row-row0,col-col0))
        drow=[0,0,-1,1]
        dcol=[-1,1,0,0]
        for i in range(4):
            nrow=row+drow[i]
            ncol=col+dcol[i]
            if (0<=nrow<len(grid) and 0<=ncol<len(grid[0]) and grid[nrow][ncol]=='L' and vis[nrow][ncol]==0):
                self.dfs(grid,vis,nrow,ncol,row0,col0,temp)
                    
            
            
            
        
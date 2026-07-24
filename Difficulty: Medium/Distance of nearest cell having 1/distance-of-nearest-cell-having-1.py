class Solution:
	def nearest(self, grid):
	    n=len(grid)
	    m=len(grid[0])
	    vis=[[0]*len(grid[0]) for _ in range(len(grid))]
	    ans=[[0]*len(grid[0]) for _ in range(len(grid))]
	    q=deque()
	    for i in range(len(grid)):
	        for j in range(len(grid[0])):
	            if grid[i][j]==1:
	                q.append([i,j,0])
	                vis[i][j]=1
	 
	    while(q):
	        temp=q.popleft()
	        row=temp[0]
	        col=temp[1]
	        cost=temp[2]
	        ans[row][col]=cost
	        delrow=[0,0,-1,1]
	        delcol=[1,-1,0,0]
	        for k in range(4):
	            nrow=row+delrow[k]
	            ncol=col+delcol[k]
	            if 0<=nrow<n and 0<=ncol<m and vis[nrow][ncol]==0:
	                q.append([nrow,ncol,cost+1])
	                vis[nrow][ncol]=1
	                
	    return ans
	                
		
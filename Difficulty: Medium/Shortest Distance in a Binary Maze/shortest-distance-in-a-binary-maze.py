from collections import deque
import math
class Solution:
    def shortestPath(self, mat: list[list[int]], src: list[int], dest: list[int]) -> int:
        # Source or destination is blocked
        if mat[src[0]][src[1]] == 0 or mat[dest[0]][dest[1]] == 0:
            return -1

        # Already at destination
        if src == dest:
            return 0
        
        
        n=len(mat)
        m=len(mat[0])
        q=deque()
        dist=[[math.inf]*m for _ in range(n)]
        q.append((0,src[0],src[1]))
        dist[src[0]][src[1]]=0
        
        dr=[-1,1,0,0]
        dc=[0,0,-1,1]
        while q:
            dis,row,col=q.popleft()
            for i in range(4):
                r=row+dr[i]
                c=col+dc[i]
                
                
                if 0<=r<n and 0<=c<m and mat[r][c]==1 and dis+1<dist[r][c]:
                    if r==dest[0] and c==dest[1]:
                        return dis+1
                    
                    dist[r][c]=dis+1
                    q.append((dis+1,r,c))
                    
        return -1
                    
                
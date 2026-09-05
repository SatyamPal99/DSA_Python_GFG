class Disjoint_set:
    def __init__(self,n):
        self.par=list(range(n+1))
        self.rank=[0]*(n+1)
        self.size=[1]*(n+1)
    def find_set(self,node):
        if node==self.par[node]:
            return node
        self.par[node]=self.find_set(self.par[node])
        return self.par[node]

    def union_by_size(self,u,v):
        root_u=self.find_set(u)
        root_v=self.find_set(v)
        if root_u==root_v:
            return False
        if self.size[root_v]<self.size[root_u]:
            self.par[root_v]=root_u
            self.size[root_u]=self.size[root_u]+self.size[root_v]
        else:
            self.par[root_u]=root_v
            self.size[root_v]=self.size[root_v]+self.size[root_u]
        return True

    def union_by_rank(self,u,v):
        root_u=self.find_set(u)
        root_v=self.find_set(v)
        if root_u==root_v:
            return
        if self.rank[root_u]<self.rank[root_v]:
            self.par[u]=self.par[v]
        elif self.rank[root_u]>self.rank[root_v]:
            self.par[v]=self.par[u]
        else:
            self.par[v]=self.par[u]
            self.rank[root_u]+=1


class Solution:
    def countIslands(self, grid):
        n=len(grid)
        m=len(grid[0])
        ds=Disjoint_set(n*m)
        
        cnt=0
        dr=[-1,-1,-1,0,0,1,1,1]
        dc=[0,-1,1,-1,1,0,-1,1]
        for row in range(n):
            for col in range(m):
                if grid[row][col]!="L":
                    continue
                
                cnt+=1
                node=row*m+col
                for k in range(8):
                    r=row+dr[k]
                    c=col+dc[k]
                    if 0<=r<n and 0<=c<m:
                        if grid[r][c]=='L':
                            nei=r*m+c
                            if ds.union_by_size(node,nei):
                                cnt-=1  
        return cnt
                            
                    
                
            
            
            
        
        
        
        
        
        
        
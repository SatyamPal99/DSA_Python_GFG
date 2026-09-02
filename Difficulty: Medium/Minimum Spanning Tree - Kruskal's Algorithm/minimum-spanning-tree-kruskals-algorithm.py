from typing import List

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
            return
        if self.size[root_v]<self.size[root_u]:
            self.par[root_v]=root_u
            self.size[root_u]=self.size[root_u]+self.size[root_v]
        else:
            self.par[root_u]=root_v
            self.size[root_v]=self.size[root_v]+self.size[root_u]
            
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
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        edge=[]
        for u,v,w in edges:
            edge.append((w,u,v))
        
        ds=Disjoint_set(V)
        edge.sort()
        cost=0
        mst=[]
        for w,u,v in edge:
            if (ds.find_set(u))!=(ds.find_set(v)):
                cost+=w
                ds.union_by_size(u,v)
        return cost
            
        
        
        
        
        
        
        
        
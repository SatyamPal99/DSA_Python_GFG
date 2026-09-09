class Disjoint_set:
    def __init__(self,n):
        self.size=[1]*n
        self.par=list(range(n))
    def find_par(self,node):
        if node==self.par[node]:
            return node
        self.par[node]=self.find_par(self.par[node])
        return self.par[node]

    def union_by_size(self,u,v):
        root_u=self.find_par(u)
        root_v=self.find_par(v)
        if root_u==root_v:
            return
        elif self.size[root_u]>self.size[root_v]:
            self.par[root_v]=root_u
            self.size[root_u]+=self.size[root_v]
        else:
            self.par[root_u]=root_v
            self.size[root_v]+=self.size[root_u]


class Solution:
    def minConnect(self, V, edges):
        ds=Disjoint_set(V)
        extraEdges=0
        for u,v in edges:
            if ds.find_par(u)==ds.find_par(v):
                extraEdges+=1
            else:
                ds.union_by_size(u,v)
        
        components=0
        for i in range(V):
            if ds.find_par(i)==i:
                components+=1
        if extraEdges>=components-1:
            return components-1
        return -1
        
        
        
        
        
        

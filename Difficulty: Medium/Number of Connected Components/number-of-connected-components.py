class disjoint_set:
    def __init__(self,n):
        self.par=list(range(n))
        self.size=[1]*(n)
        
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
            self.size[root_u]+=self.size[root_v]
            self.par[root_v]=root_u
        else:
            self.size[root_v]+=self.size[root_u]
            self.par[root_u]=root_v

class Solution:
    def countConnected(self, V, edges):
        ds=disjoint_set(V)
        for u,v in edges:
            ds.union_by_size(u,v)
                
        count=0
       
        for i in range(V):
            if ds.find_par(i)==i:
                count+=1
                
        
        return count
        
        
        
        
        
        
        
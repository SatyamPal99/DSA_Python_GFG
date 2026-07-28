class Solution:
    def isCyclic(self, V, edges):
        vis=[0]*V
        pathvis=[0]*V
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            
        for i in range(V):
            if vis[i]==0:
                if self.dfs(adj,i,vis,pathvis)==True:
                    return True
        return False
                
                
    def dfs(self,adj,node,vis,pathvis):
        vis[node]=1
        pathvis[node]=1
        for i in adj[node]:
            if vis[i]==0:
                if self.dfs(adj,i,vis,pathvis)==True:
                    return True
            elif pathvis[i]==1:
                return True
        pathvis[node]=0
        return False
        
        
        

class Solution:
    def isBipartite(self, V, edges):
        vis=[-1]*V
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for i in range(V):
            if vis[i]==-1:
                if self.dfs(V,adj,i,0,vis)==False:
                    return False
        return True
                
    def dfs(self,V,adj,node,col,vis):
        vis[node]=col
        for i in adj[node]:
            if vis[i]==-1:
                if self.dfs(V,adj,i,not col,vis)==False:
                    return False
            elif vis[i]==col:
                return False
        return True
        
class Solution:
    def safeNodes(self, V, edges):
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        pathvis=[0]*V
        vis=[0]*V
        safe=[0]*V
        ans=[]
        for i in range(V):
            if vis[i]==0:
                self.dfs(adj,pathvis,vis,i,safe)

        for i in range(V):
            if safe[i]==1:
                ans.append(i)
        return ans
                    
                
                
    def dfs(self,adj,pathvis,vis,node,safe):
        vis[node]=1
        pathvis[node]=1
        safe[node]=0
        for i in adj[node]:
            if vis[i]==0:
                if self.dfs(adj,pathvis,vis,i,safe)==True:
                    safe[node]=0
                    return True
            elif pathvis[i]==1:
                safe[node]=0
                return True
        safe[node]=1
        pathvis[node]=0
        return False
        
        

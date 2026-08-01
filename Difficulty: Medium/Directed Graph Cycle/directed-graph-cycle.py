class Solution:
    def isCyclic(self, V, edges):
        # using dfs
        """vis=[0]*V
        pathvis=[0]*V
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            
        for i in range(V):
            if vis[i]==0:
                if self.dfs(adj,i,vis,pathvis)==True:
                    return True
        return False"""
        
        vis=[0]*V
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        inDeg=[0]*V
        q=deque()
        for i in range(V):
            for j in adj[i]:
                inDeg[j]+=1
        for j in range(V):
            if inDeg[j]==0:
                q.append(j)
        count=0
        while q:
            node=q.popleft()
            count+=1
            for i in adj[node]:
                inDeg[i]-=1
                if inDeg[i]==0:
                    q.append(i)
        if count<V:
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
    
    
    
                
                
    
    
    
        
        
        
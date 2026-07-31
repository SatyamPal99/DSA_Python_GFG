from collections import deque
class Solution:
    def topoSort(self, V, edges):
        # Usinf BFS(Kahn's Algorithm)
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        INdegree=[0]*V
        for i in range(V):
            for j in adj[i]:
                INdegree[j]+=1
        q=deque()
        for i in range(V):
            if INdegree[i]==0:
                q.append(i)
        ans=[]
        while q:
            node=q.popleft()
            ans.append(node)
            for i in adj[node]:
                INdegree[i]-=1
                if INdegree[i]==0:
                    q.append(i)
        return ans
        
        
        
        
        
        
        """vis=[0]*V
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        st=[]   
        for i in range(V):
            if vis[i]==0:
                self.dfs(vis,adj,i,st)
        ans=[]
        for i in range(len(st)):
            temp=st.pop()
            ans.append(temp)
        return ans
    
    def dfs(self,vis,adj,node,st):
        vis[node]=1
        for i in adj[node]:
            if vis[i]==0:
                self.dfs(vis,adj,i,st)
        st.append(node)"""
                
        
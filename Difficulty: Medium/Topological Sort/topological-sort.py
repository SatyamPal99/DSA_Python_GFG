class Solution:
    def topoSort(self, V, edges):
        vis=[0]*V
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
        st.append(node)
                
        
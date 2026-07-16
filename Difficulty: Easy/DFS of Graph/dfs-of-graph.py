class Solution:
    def dfs(self, adj):
        vis=[0]*len(adj)
        vis[0]=1
        ans=[]
        self.helper(adj,vis,ans,0)
        return ans
    def helper(self,adj,vis,ans,idx):
        ans.append(idx)
        for i in adj[idx]:
            if vis[i]!=1:
                vis[i]=1
                self.helper(adj,vis,ans,i)
        
        
        
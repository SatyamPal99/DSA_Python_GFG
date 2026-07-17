
from collections import deque

class Solution:
	def isCycle(self, V, edges):
	    adj=[[] for _ in range(V)]
	    for u,v in edges:
	        adj[u].append(v)
	        adj[v].append(u)
	    vis=[0]*V
	    for i in range(V):
	        if vis[i]==0:
	            ans=self.fun(i,adj,vis)
	            if ans:
	                return True
	    return False
	    
	    
    def fun(self,src,adj,vis):
        vis[src]=1
        q=deque()
        q.append([src,-1])
        while q:
            temp=q.popleft()
            node=temp[0]
            parent=temp[1]
            for i in adj[node]:
                if vis[i]==0:
                    vis[i]=1
                    q.append([i,node])
                elif (parent!=i):
                    return True
        return False
            
            
            
            
            
            
            
		
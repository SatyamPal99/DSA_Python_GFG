from collections import deque
import math
class Solution:
    def shortestPath(self, V, edges, src, dest):
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        relax=[math.inf]*V
        relax[src]=0
        q=deque()
        q.append((src,0))
        while q:
            node,d=q.popleft()
            for i in adj[node]:
                dis=d+1
                if relax[i]>dis:
                    relax[i]=dis
                    q.append((i,dis))
        for i in range(V):
            if relax[i]==math.inf:
                relax[i]=-1
        return relax[dest]
        
                
        
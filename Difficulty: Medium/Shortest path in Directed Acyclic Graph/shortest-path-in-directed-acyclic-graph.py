from collections import deque
import math
class Solution:
    def shortestPath(self, V: int, edges: list[list[int]]) -> list[int]:
        adj=[[] for _ in range(V)]
        for u,v,d in edges:
            adj[u].append((v,d))
        indeg=[0]*V
        for i in range(V):
            for v,d in adj[i]:
                indeg[v]+=1
        ans=[]
        q=deque()
        for i in range(V):
            if indeg[i]==0:
                q.append(i)
        relax=[math.inf]*V
        # source is 0
        relax[0]=0
        while q:
            node=q.popleft()
            ans.append(node)
            for v,d in adj[node]:
                indeg[v]-=1
                if indeg[v]==0:
                    q.append(v)
        for node in ans:
            if relax[node]!=math.inf:
                for v,d in adj[node]:
                    if relax[node]+d<relax[v]:
                        relax[v]=relax[node]+d
        for i in range(V):
            if relax[i]==math.inf:
                relax[i]=-1
        
        return relax
                
                
            
            
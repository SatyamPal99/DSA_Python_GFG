import heapq
import math
class Solution:
    def shortestPath(self, V, edges, src, dest):
        adj=[[] for _ in range(V+1)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
            
        pq=[]
        parent=[i for i in range(V+1)]
        dist=[math.inf]*(V+1)
        dist[dest]=0
        heapq.heappush(pq,(0,dest))
        
        while pq:
            
            d,node=heapq.heappop(pq)
            if d>dist[node]:
                continue
            
            for nei,w in adj[node]:
                dis=d+w
                if dis<dist[nei]:
                    dist[nei]=dis
                    heapq.heappush(pq,(dis,nei))
                    
        if dist[src]==math.inf:
            return [-1]
            
        ans=[src]
        node=src
        while node!=dest:
            best=math.inf
            for nei,w in adj[node]:
                if dist[node]==w+dist[nei]:
                    best=min(best,nei)
            node=best
            ans.append(node)
        
        return ans
            
        
        
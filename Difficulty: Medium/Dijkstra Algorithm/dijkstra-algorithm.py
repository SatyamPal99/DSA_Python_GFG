import heapq
import math
class Solution:
    def dijkstra(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        adj=[[] for _ in range(V)]
        for u,v,w in edges:
            adj[u].append((w,v))
            adj[v].append((w,u))
        dist=[math.inf]*V
        pq=[(0,src)]
        dist[src]=0
        while pq:
            w,node=heapq.heappop(pq)
            if w>dist[node]:
                continue
            for d,nei in adj[node]:
                dis=w+d
                if dis<dist[nei]:
                    dist[nei]=dis
                    heapq.heappush(pq,(dis,nei))
        return dist
                
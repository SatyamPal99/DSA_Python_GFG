class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        dist=[10**8]*V
        dist[src]=0
        for i in range(V):
            for u,v,wt in edges:
                if dist[u]==10**8:
                    continue
                elif dist[u]+wt<dist[v]:
                    if i==V-1:
                        return [-1]
                    dist[v]=dist[u]+wt
        
        return dist
            
        
import heapq
class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        pq=[]
        vis=[0]*V
        adj=[[] for _ in range(V)]
        for u,v,wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))
        sum=0
        heapq.heappush(pq,(0,0,-1))
        mst=[]
        while pq:
            cost,node,par=heapq.heappop(pq)
            if vis[node]==1:
                continue
            elif vis[node]==0 and par==-1:
                vis[node]=1
            elif vis[node]==0 and par!=-1:
                vis[node]=1
                sum=sum+cost
                mst.append((node,par))
                
            for nei,wt in adj[node]:
                if vis[nei]==0:
                    heapq.heappush(pq,(wt,nei,node))
        return sum
        
        
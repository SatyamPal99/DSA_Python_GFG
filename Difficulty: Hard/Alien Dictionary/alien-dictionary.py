class Solution:
    def findOrder(self, words: list[str]) -> str:
        chars = set()
        for word in words:
            for ch in word:
                chars.add(ch)
                
        chars=sorted(chars)
        
        mp={}
        rev={}
        for idx,ch in enumerate(chars):
            mp[ch]=idx
            rev[idx]=ch
            
        V=len(chars)
        
        adj=[[] for _ in range(V)]
        for i in range(len(words)-1):
            s1=words[i]
            s2=words[i+1]
            length=min(len(s1),len(s2))
            
            """if len(s1)>len(s2) and s1[:length]==s2[:length]:
                return ""  """
                
            for j in range(length):
                if s1[j]!=s2[j]:
                    adj[mp[s1[j]]].append(mp[s2[j]])
                    break
        ans=self.topo(adj,V)
        if len(ans)!=V:
            return ""
        topo=""
        for node in ans:
            topo+=rev[node]
        return topo
        
            
        
        
    def topo(self,adj,V):
        indeg=[0]*V
        for i in range(V):
            for j in adj[i]:
                indeg[j]+=1
        q=deque()
        for i in range(V):
            if indeg[i]==0:
                q.append(i)
        ans=[]
        while q:
            node=q.popleft()
            ans.append(node)
            for i in adj[node]:
                indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)
        return ans
            
            
            
                    
        
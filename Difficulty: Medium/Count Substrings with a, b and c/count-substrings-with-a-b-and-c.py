class Solution:
    def countSubstring(self, s):
        """cout=0
        for i in range(len(s)):
            mapp={0:-1,1:-1,2:-1}
            for j in range(i,len(s)):
                mapp[ord(s[j])-ord('a')]=1
                if mapp.get(0,-1)!=-1 and mapp.get(1,-1)!=-1 and mapp.get(2,-1)!=-1:
                    cout+=1
        return cout"""
        
        # better...
        r=0
        cout=0
        mapp={0:-1,1:-1,2:-1}
        while r<len(s):
            mapp[ord(s[r])-ord('a')]=r
            if mapp.get(0,-1)!=-1 and mapp.get(1,-1)!=-1 and mapp.get(2,-1)!=-1:
                cout=cout+(1+min(mapp.get(0,0),mapp.get(1,0),mapp.get(2,0)))
            r+=1
        return cout
            
            
                    
                
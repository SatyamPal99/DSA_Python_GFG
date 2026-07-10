class Solution:
    def longestKSubstr(self, s, k):
        r=0
        l=0
        maxlen=-1
        mapp={}
        while r<len(s):
            mapp[s[r]]=mapp.get(s[r],0)+1
            if len(mapp)>k:
                mapp[s[l]]-=1
                if mapp[s[l]]==0:
                    del mapp[s[l]]
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        if len(mapp)>=k:
            return maxlen
        else:
            return -1
                
            
class Solution:
    def longestSubarray(self, arr, k):
        # bruteforce...
        """maxlen=0
        for i in range(len(arr)):
            summ=0
            for j in range(i,len(arr)):
                summ=summ+arr[j]
                if summ==k:
                    maxlen=max(maxlen,j-i+1)
        return maxlen"""
        
        # Optimized...
        
        maxlen=0
        summ=0
        mapp={}
        for i in range(len(arr)):
            summ=summ+arr[i]
            if summ==k:
                maxlen=i+1
            elif summ-k in mapp:
                maxlen=max(maxlen,i-mapp[summ-k])
            if summ not in mapp:
                mapp[summ]=i
        return maxlen
                    
                
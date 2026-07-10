class Solution:
    def cntSubarrays(self, arr, k):
        maxlen=0
        summ=0
        mapp={}
        for i in arr:
            summ=summ+i
            if summ==k:
                maxlen+=1
            if summ-k in mapp:
                maxlen=maxlen+mapp[summ-k]
            mapp[summ]=mapp.get(summ,0)+1
        return maxlen
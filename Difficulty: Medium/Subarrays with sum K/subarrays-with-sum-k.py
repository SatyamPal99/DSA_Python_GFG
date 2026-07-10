class Solution:
    def cntSubarrays(self, arr, k):
        count=0
        summ=0
        mapp={}
        for i in range(len(arr)):
            summ=summ+arr[i]
            if summ==k:
                count+=1
            if summ-k in mapp:
                count=count+mapp[summ-k]
            mapp[summ]=mapp.get(summ,0)+1
        return count
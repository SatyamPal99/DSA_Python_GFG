class Solution:
    def minTime (self, arr, k):
        low=max(arr)
        high=sum(arr)
        """for i in range(low,high+1):
            res=self.fun(arr,i)
            if res<=k:
                return i"""
        
        # Optimized...
        while(low<=high):
            mid=(low+high)//2
            if self.fun(arr,mid)<=k:
                high=mid-1
            else:
                low=mid+1
        return low
            
        
        
    def fun(self,arr,area):
        painter=1
        allocated=0
        for i in range(len(arr)):
            if allocated+arr[i]<=area:
                allocated+=arr[i]
            else:
                painter+=1
                allocated=arr[i]
        return painter
        
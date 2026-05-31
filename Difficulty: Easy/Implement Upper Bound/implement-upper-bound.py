class Solution:
    def upperBound(self, arr, tar):
        n=len(arr)
        i=0
        j=n-1
        ans=n
        while(i<=j):
            mid=(i+j)//2
            if arr[mid]>tar:
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        n=len(arr)
        i=0
        j=n-1
        ans=n
        while(i<=j):
            mid=(i+j)//2
            if arr[mid]>=x:
                ans=mid
                j=mid-1
            elif arr[mid]<x:
                i=mid+1
        if ans==n:
            return -1
        return ans
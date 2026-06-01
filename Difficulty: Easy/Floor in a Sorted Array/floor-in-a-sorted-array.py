class Solution:
    def findFloor(self, arr, x):
        i=0
        j=len(arr)-1
        ans=len(arr)
        while(i<=j):
            mid=(i+j)//2
            if arr[mid]>x:
                j=mid-1
            elif arr[mid]<=x:
                ans=mid
                i=mid+1
        if ans==len(arr):
            return -1
        return ans
        
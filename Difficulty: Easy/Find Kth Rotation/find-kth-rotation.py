class Solution:
    def findKRotation(self, arr):
        low=0
        high=len(arr)-1
        mini=999999999
        idx=-1
        while(low<=high):
            mid=(low+high)//2
            if arr[low]<=arr[high]:
                if mini>arr[low]:
                    idx=low
                    mini=arr[low]
                break
            if arr[mid]>=arr[low]:
                if mini>arr[low]:
                    idx=low
                    mini=arr[low]
                low=mid+1
            else:
                if mini>arr[mid]:
                    idx=mid
                    mini=arr[mid]
                high=mid-1
        return idx
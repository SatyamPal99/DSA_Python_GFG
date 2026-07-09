class Solution:
    def findUnique(self, arr):
        # Optimized
        ans=0
        for i in range(len(arr)):
            ans=ans^arr[i]
        return ans
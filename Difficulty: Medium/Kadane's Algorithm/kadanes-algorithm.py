class Solution:
    def maxSubarraySum(self, arr):
        summ=0
        max_sum=-(sys.maxsize)
        for i in range(len(arr)):
            summ=summ+arr[i]
            max_sum=max(max_sum,summ)
            if summ<0:
                summ=0
        return max_sum
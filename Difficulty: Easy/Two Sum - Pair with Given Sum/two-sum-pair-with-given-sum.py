class Solution:
	def twoSum(self, arr, target):
	    arr.sort()
	    low=0
	    high=len(arr)-1
	    summ=0
	    while(low<high):
	        summ=arr[low]+arr[high]
	        if summ>target:
	            high-=1
	        elif summ<target:
	            low=low+1
	        else:
	            return True
	    return False
		
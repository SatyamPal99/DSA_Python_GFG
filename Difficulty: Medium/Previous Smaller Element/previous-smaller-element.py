class Solution:
	def prevSmaller(self, arr):
	    """ans=[-1]*len(arr)
		for i in range(len(arr)):
		    for j in range(i-1,-1,-1):
		        if arr[j]<arr[i]:
		            ans[i]=arr[j]
		            break
	    return ans"""
	    
	    ans=[-1]*len(arr)
	    st=[]
	    for i in range(len(arr)):
	        while st and st[-1]>=arr[i]:
	            st.pop()
	        
	        if not st:
	            ans[i]=-1
	        else:
	            ans[i]=st[-1]
	        st.append(arr[i])
	    return ans
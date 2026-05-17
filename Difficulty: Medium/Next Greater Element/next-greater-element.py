class Solution:
    def nextLargerElement(self, arr):
        """ans=[-1]*len(arr)
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    ans[i]=arr[j]
                    break
        return ans"""
        
        # Optimized Approach...
        
        
        st=[]
        for i in range(len(arr)-1,-1,-1):
            if not st:
                st.append(arr[i])
                arr[i]=-1
            else:
                if st[-1]>arr[i]:
                    temp=arr[i]
                    arr[i]=st[-1]
                    st.append(temp)
                else:
                    while(st):
                        if st[-1]>arr[i]:
                            temp=arr[i]
                            arr[i]=st[-1]
                            st.append(temp)
                            break
                        else:
                            st.pop()
                    if not st:
                        st.append(arr[i])
                        arr[i]=-1
        return arr
            
        
class Solution:
    def missingNum(self, arr):
        #brute force
        """for i in range(1,len(arr)+2):
            flag=0
            for j in range(0,len(arr)):
                if arr[j]==i:
                    flag=1
                    break
            if flag==0:
                return i"""
                
        # Better
        mapp={}
        for i in arr:
            if i not in mapp:
                mapp[i]=1
            
        for i in range(1,len(arr)+2):
            if i not in mapp:
                return i
        
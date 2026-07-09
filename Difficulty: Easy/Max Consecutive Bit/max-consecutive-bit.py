class Solution:
    def maxConsecBits(self, arr):
        count1=0
        count0=0
        maxx1=0
        maxx0=0
        prev=None
        for i in range(len(arr)):
            if arr[i]==0:
                if prev==1:
                    count0=0
                count0+=1
                if count0>maxx0:
                    maxx0=count0
                    
            else:
                if prev==0:
                    count1=0
                count1+=1
                if count1>maxx1:
                    maxx1=count1
            prev=arr[i]
        return max(maxx0,maxx1)
class Solution:
    def sort012(self, arr):
        zeros=0
        one=0
        two=0
        for i in range(0,len(arr)):
            if arr[i]==0:
                zeros+=1
            elif arr[i]==1:
                one+=1
            else:
                two+=1
        for i in range(0,zeros):
            arr[i]=0
        for j in range(zeros,zeros+one):
            arr[j]=1
        for k in range(one+zeros,one+zeros+two):
            arr[k]=2
        return arr
        
                
            
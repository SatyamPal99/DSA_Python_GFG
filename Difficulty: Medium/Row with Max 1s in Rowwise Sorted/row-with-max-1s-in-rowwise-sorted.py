class Solution:
    def rowWithMax1s(self, mat):
        maxi=-1
        ans=-1
        idx=-1
        for i in range(len(mat)):
            count=-1
            low=0
            high=len(mat[0])-1
            while(low<=high):
                mid=(low+high)//2
                if mat[i][mid]==1:
                    idx=mid
                    count=len(mat[0])-idx
                    high=mid-1
                elif mat[i][mid]<1:
                    low=mid+1
            if count>maxi:
                ans=i
                maxi=count
        return ans
        
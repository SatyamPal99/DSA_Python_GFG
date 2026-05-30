class Solution:
    def celebrity(self, mat):
        knowMe=[0]*len(mat)
        iKnow=[0]*len(mat)
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j:
                    continue
                if mat[i][j]==1:
                    knowMe[j]+=1
                    iKnow[i]=1
        for i in range(len(mat)):
            if knowMe[i]==len(mat)-1 and iKnow[i]==0:
                return i
        return -1
        
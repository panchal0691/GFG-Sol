class Solution:
    def findMaxSum(self,n,m,mat):
        if n < 3 or m < 3:
            return -1
        
        ans = -1
        
        for i in range(n - 2):
            for j in range(m - 2):
                # A is present at i, j
                summation = (
                    mat[i][j] + mat[i][j + 1] + mat[i][j + 2] +
                    mat[i + 1][j + 1] +
                    mat[i + 2][j] + mat[i + 2][j + 1] + mat[i + 2][j + 2]
                )
                ans = max(ans, summation)
        
        return ans

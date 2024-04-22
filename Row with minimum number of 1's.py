class Solution:
    def minRow(self,n,m,a):
        ans = -1
        mini = float('inf')
        for i in range(n):
            curr = 0
            for j in range(m):
                if a[i][j] == 1:
                    curr += 1
            if curr < mini:
                mini = curr
                ans = i + 1
        return ans
        #code here

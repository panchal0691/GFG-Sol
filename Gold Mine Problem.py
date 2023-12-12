class Solution:
    def maxGold(self, n, m, M):
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            dp[i][m - 1] = M[i][m - 1]
        
        for j in range(m - 2, -1, -1):
            for i in range(n):
                dp[i][j] = dp[i][j + 1]
                
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j + 1])
                if i < n - 1:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j + 1])
                    
                dp[i][j] += M[i][j]
        
        ans = 0
        
        for i in range(n):
            ans = max(ans, dp[i][0])
        
        return ans

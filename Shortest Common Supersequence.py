class Solution:
    def shortestCommonSupersequence(self, a, b, n, m):
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if a[i] == b[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                    continue

                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return n + m - dp[0][0]

# Example usage:
# solution = Solution()
# result = solution.shortestCommonSupersequence("AGGTAB", "GXTXAYB", 6, 7)
# print(result)

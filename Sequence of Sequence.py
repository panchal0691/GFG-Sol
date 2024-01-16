Sequence of Sequence
class Solution:
    def numberSequence(self, m, n):
        dp = [[0] * (m + 1) for _ in range(n)]

        for i in range(1, m + 1):
            dp[n - 1][i] = 1

        for i in range(n - 2, -1, -1):
            for j in range(1, m + 1):
                for k in range(2 * j, m + 1):
                    dp[i][j] += dp[i + 1][k]

        return sum(dp[0])

class Solution:
    def maxSumWithK(self, a, n, k):
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            dp[i] = a[i] + dp[i + 1]
            dp[i] = max(dp[i], 0)
        
        ans = float('-inf')
        cur_sum = 0
        for i in range(k):
            cur_sum += a[i]
        
        for i in range(k, n):
            summ = cur_sum + dp[i]
            ans = max(ans, summ)
            
            cur_sum += a[i]
            cur_sum -= a[i - k]
        
        return max(ans, cur_sum)

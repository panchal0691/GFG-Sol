class Solution:
    def longestSubseq(self, n, a):
        # Create a list to store the longest subsequence length ending at each index
        dp = [0] * n
        
        # Variable to store the maximum subsequence length found
        ans = 0
        
        # Iterate over the array in reverse
        for i in range(n-1, -1, -1):
            maxi = 0
            # Check all elements ahead of the current element
            for j in range(i+1, n):
                # Check if the absolute difference is 1
                if abs(a[i] - a[j]) == 1:
                    maxi = max(maxi, dp[j])
            # Update the dp array for the current element
            dp[i] = 1 + maxi
            # Update the answer with the maximum length found
            ans = max(ans, dp[i])
        
        return ans

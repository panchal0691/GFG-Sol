class Solution:
    def longSubarrWthSumDivByK(self, arr, n, k):
        sum_val = 0
        suffix = {0: n}
        ans = 0
        
        for i in range(n - 1, -1, -1):
            sum_val = (sum_val + (arr[i] % k) + k) % k
            
            if sum_val not in suffix:
                suffix[sum_val] = i
            else:
                ans = max(ans, suffix[sum_val] - i)
        
        return ans

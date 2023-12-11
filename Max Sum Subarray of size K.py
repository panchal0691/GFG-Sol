class Solution:
    def maximumSumSubarray(self, K, Arr, N):
        sum_val = 0
        best = 0
        
        for i in range(K):
            sum_val += Arr[i]
        
        best = sum_val
        
        for i in range(K, N):
            sum_val -= Arr[i - K]
            sum_val += Arr[i]
            
            best = max(best, sum_val)
        
        return best

class Solution:
    def findMaxSum(self, arr, n):
        next_0 = next_1 = 0
        
        for i in range(n - 1, -1, -1):
            cur_0 = max(arr[i] + next_1, next_0)
            cur_1 = next_0
            
            next_0 = cur_0
            next_1 = cur_1
        
        return next_0

class Solution:
    def pairAndSum(self, n, arr):
        ans = 0
        
        for i in range(32):
            count = 0
            for j in range(n):
                if arr[j] & (1 << i):
                    count += 1
            ans += (1 << i) * (count * (count - 1) // 2)
        
        return ans
        #code here

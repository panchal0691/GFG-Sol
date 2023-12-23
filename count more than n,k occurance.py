from collections import defaultdict

class Solution:
    def countOccurence(self, arr, n, k):
        f = defaultdict(int)
        
        for i in range(n):
            f[arr[i]] += 1
        
        ans = 0
        
        for val in f.values():
            if val > (n // k):
                ans += 1
        
        return ans

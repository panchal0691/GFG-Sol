class Solution:
    def minimumStep(self, n):
        ans = 0
        
        while n >= 3:
            ans += n % 3 + 1
            n //= 3
        
        return ans + (n - 1)

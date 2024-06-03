class Solution:
    MOD = int(1e9 + 7)
    
    def power(self, a, b):
        ans = 1
        while b > 0:
            if b & 1:
                ans *= a
                ans %= self.MOD
            a *= a
            a %= self.MOD
            b >>= 1
        return ans
    
    def numberOfConsecutiveOnes(self, n):
        a = [0] * n
        b = [0] * n
        
        a[0] = 1
        b[0] = 1
        
        for i in range(1, n):
            a[i] = (a[i - 1] + b[i - 1]) % self.MOD
            b[i] = a[i - 1]
        
        return (self.power(2, n) + self.MOD - (a[n - 1] + b[n - 1]) % self.MOD) % self.MOD

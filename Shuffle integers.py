class Solution:
    def shuffleArray(self, arr, n):
        mod = 1001
        for i in range(n // 2):
            a[i * 2] += (a[i] % mod) * mod
            a[i * 2 + 1] += (a[i + n // 2] % mod) * mod
        
        for i in range(n):
            a[i] //= mod

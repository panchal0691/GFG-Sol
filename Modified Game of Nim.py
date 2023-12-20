class Solution:
    def findWinner(self, n, A):
        val = 0
        
        for i in range(n):
            val ^= A[i]
        
        return 2 if n % 2 != 0 and val > 0 else 1

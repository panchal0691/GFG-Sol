class Solution:
    def gameOfXor(self, N, A):
        ans = 0
        
        for i in range(N):
            if ((i + 1) & 1) and ((N - i) & 1):
                ans ^= A[i]
        
        return ans

class Solution:
    def columnWithMaxZeros(self,arr,N):
        best = 0
        ans = -1
        
        for j in range(N):
            cur = 0
            
            for i in range(N):
                cur += arr[i][j] == 0
                
            if cur > best:
                best = cur
                ans = j
        
        return ans

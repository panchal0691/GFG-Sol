class Solution:
    def posOfRightMostDiffBit(self, m, n):
        for i in range(32):
            x = (m >> i) & 1
            y = (n >> i) & 1
            
            if x != y:
                return i + 1
        
        return -1

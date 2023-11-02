class Solution:
    def minDist(self, a, n, x, y):
        last = -1
        pos = -1
        ans = float('inf')
        
        for i in range(n):
            if a[i] == x:
                if last == y:
                    ans = min(ans, i - pos)
                
                last = x
                pos = i
            elif a[i] == y:
                if last == x:
                    ans = min(ans, i - pos)
                    
                last = y
                pos = i
        
        return -1 if ans == float('inf') else ans

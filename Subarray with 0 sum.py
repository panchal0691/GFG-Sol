
class Solution:
    def subArrayExists(self, arr, n):
        found = {0: 1}
        _sum = 0
        
        for i in range(n):
            _sum += arr[i]
            
            if _sum in found:
                return True
                
            found[_sum] = 1
        
        return False

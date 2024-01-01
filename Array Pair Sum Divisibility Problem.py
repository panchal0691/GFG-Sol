
class Solution:
	def canPair(self, nuns, k):
	    f = {}
        
        for num in nums:
            cur = num % k
            need = (k - cur) % k
            
            if need in f and f[need] > 0:
                f[need] -= 1
                if f[need] == 0:
                    del f[need]
            else:
                if cur in f:
                    f[cur] += 1
                else:
                    f[cur] = 1
        
        return len(f) == 0

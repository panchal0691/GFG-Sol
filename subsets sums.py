class Solution:
	def subsetSums(self, arr, N):
	    
	    ans = []
	    def fun(ind: int,sum:int):
	        if ind ==N:
	            ans.append(sum)
	            return
	        
	        fun(ind +1, sum + arr[ind])
	        fun(ind +1, sum)
	    fun(0,0)
	   
	    return ans

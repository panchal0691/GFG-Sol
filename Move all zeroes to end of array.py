class Solution:
	def pushZerosToEnd(self,arr, n):
	    index = 0
        
        for i in range(n):
            if arr[i] != 0:
                arr[index] = arr[i]
                index += 1
        
        while index < n:
            arr[index] = 0
            index += 1

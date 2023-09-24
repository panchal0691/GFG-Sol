class Solution:
    def duplicates(self, arr, n):
        base = n
        duplicates = []

        for i in range(n):
            num = arr[i] % base
            arr[num] = base + arr[num]

        for i in range(n):
            if arr[i] // base > 1:
                duplicates.append(i)

        return duplicates if len(duplicates) != 0 else [-1]
    	# code here
    	    

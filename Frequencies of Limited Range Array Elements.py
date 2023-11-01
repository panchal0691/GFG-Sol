class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        mask = (1 << 16) - 1
        for i in arr:
            val = i & mask
            if val <= N:
                arr[val - 1] += (1 << 16)
        
        for i in range(len(arr)):
            arr[i] >>= 16

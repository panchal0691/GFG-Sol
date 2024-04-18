class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        ans = []
        for i in range(n + 2):
            ind = abs(arr[i])
            if arr[ind] > 0:
                arr[ind] = -arr[ind]
            else:
                ans.append(ind)
        return ans

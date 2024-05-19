class Solution:
    def findClosest(self, n, k, arr):
        lo, hi = 0, n - 1
        ans = arr[0]
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if abs(k - arr[mid]) == abs(k - ans):
                ans = max(ans, arr[mid])
            elif abs(k - arr[mid]) < abs(k - ans):
                ans = arr[mid]
                
            if arr[mid] == k:
                return arr[mid]
            elif arr[mid] < k:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return ans

class Solution:
    def findPeakElement(self, nums):
        lo, hi = 0, len(nums) - 1
        ans = float('-inf')
        
        while lo <= hi:
            mid = (lo + hi) // 2
            ans = max(ans, nums[mid])
            
            if mid == 0:
                lo = mid + 1
            elif mid == len(nums) - 1:
                hi = mid - 1
            elif nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans

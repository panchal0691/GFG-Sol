from collections import defaultdict

class Solution:
    def winner(self, arr, n):
        votes = defaultdict(int)
        
        for candidate in arr:
            votes[candidate] += 1
        
        best = 0
        ans = ['', '']
        
        for candidate, count in votes.items():
            if count > best:
                best = count
                ans[0] = candidate
                ans[1] = str(best)
            elif count == best and candidate < ans[0]:
                ans[0] = candidate
        
        return ans

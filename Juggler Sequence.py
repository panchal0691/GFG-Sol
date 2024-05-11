from math import sqrt

class Solution:
    def jugglerSequence(self, n):
        ans = [n]
        prev = n
        while prev != 1:
            if prev % 2 == 1:
                ans.append(int(sqrt(pow(prev, 3))))
            else:
                ans.append(int(sqrt(prev)))
            prev = ans[-1]
        return ans

# Example usage:
# sol = Solution()
# print(sol.jugglerSequence(5))

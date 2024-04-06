class Solution:

    #Function to count number of ways to reach the nth stair
    #when order does not matter.
    def countWays(self, n):

        mod = 1000000007
        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 1

        for i in range(2, n + 1):
            res[i] = res[i - 2] + 1

        return res[n]

        # code here

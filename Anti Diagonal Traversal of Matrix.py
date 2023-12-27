class Solution:
    def antiDiagonalPattern(self, matrix):
        n = len(matrix)
        ans = []
        
        # first part
        for j in range(n):
            x, y = 0, j
            while y > -1 and x < n:
                ans.append(matrix[x][y])
                x += 1
                y -= 1
        
        # second part
        for i in range(1, n):
            x, y = i, n - 1
            while y > -1 and x < n:
                ans.append(matrix[x][y])
                x += 1
                y -= 1
        
        return ans

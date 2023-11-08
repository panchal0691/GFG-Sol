class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix):
        i = 0
        j = 0

        n = len(matrix)
        ans = [0] * (n * n)

        for c in range(n * n):
            ans[c] = matrix[i][j]

            if i % 2 == 1:
                j -= 1
            else:
                j += 1

            if j == n or j == -1:
                if j == n:
                    j = n - 1
                else:
                    j = 0

                i += 1

        return ans


class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        upper = 0
        lower = 0

        for i in range(n):
            for j in range(i + 1):
                lower += matrix[i][j]
            for j in range(i, n):
                upper += matrix[i][j]

        return [upper, lower]
        # code here 

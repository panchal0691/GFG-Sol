import heapq
import sys

class Solution:
    def MinimumEffort(self, n, m, heights):
        pq = [(0, (0, 0))]
        dist = [[sys.maxsize] * m for _ in range(n)]
        dist[0][0] = 0
        
        while pq:
            step, (row, col) = heapq.heappop(pq)
            
            if row == n - 1 and col == m - 1:
                return step
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nrow, ncol = row + dr, col + dc
                
                if 0 <= nrow < n and 0 <= ncol < m:
                    val = max(step, abs(heights[nrow][ncol] - heights[row][col]))
                    
                    if val < dist[nrow][ncol]:
                        dist[nrow][ncol] = val
                        heapq.heappush(pq, (val, (nrow, ncol)))
        
        return dist[n - 1][m - 1]

# Example usage:
# sol = Solution()
# n = 3
# m = 3
# heights = [[1,2,2],[3,8,2],[5,3,5]]
# print(sol.MinimumEffort(n, m, heights))

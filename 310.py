from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        result = []
        indegree = [0] * n
        adj = {}

        for u, v in edges:
            indegree[u] += 1
            indegree[v] += 1
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)

        que = deque()
        for i in range(n):
            if indegree[i] == 1:
                que.append(i)

        while n > 2:
            size = len(que)
            n -= size

            for _ in range(size):
                u = que.popleft()
                for v in adj.get(u, []):
                    indegree[v] -= 1
                    if indegree[v] == 1:
                        que.append(v)

        while que:
            result.append(que.popleft())

        return result

# Example usage:
# sol = Solution()
# n = 4
# edges = [[1, 0], [1, 2], [1, 3]]
# print(sol.findMinHeightTrees(n, edges))

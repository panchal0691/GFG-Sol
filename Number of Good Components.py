from collections import deque

class Solution:
    def bfs(self, adj, start, vis):
        num = 0
        edges = 0
        q = deque()
        q.append(start)
        vis[start] = 1
        
        while q:
            node = q.popleft()
            num += 1
            edges += len(adj[node])
            
            for neighbor in adj[node]:
                if not vis[neighbor]:
                    q.append(neighbor)
                    vis[neighbor] = 1
        
        return num * (num - 1) == edges
    
    def findNumberOfGoodComponent(self, e, v, edges):
        adj = [[] for _ in range(v + 1)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        vis = [0] * (v + 1)
        ans = 0
        for i in range(1, v + 1):
            if self.bfs(adj, i, vis):
                ans += 1
        
        return ans

# Example usage:
# e = number of edges
# v = number of vertices
# edges = list of edges (each edge represented as [from_vertex, to_vertex])
# solution = Solution()
# result = solution.findNumberOfGoodComponent(e, v, edges)

class Solution:
    def sumOfDependencies(self,adj,V):
        ans = 0

        for i in range(V):
            ans += len(adj[i])

        return ans

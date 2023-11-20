class Solution:
    def sumK(self,root,k):
        from collections import defaultdict
        
        f = defaultdict(int)
        f[0] = 1
        
        ans = 0
        mod = 10**9 + 7
        
        def dfs(node, summ):
            nonlocal ans
            
            if node is None:
                return
            
            summ += node.data
            
            if summ - k in f:
                ans = (ans + f[summ - k]) % mod
            
            f[summ] += 1
            
            dfs(node.left, summ)
            dfs(node.right, summ)
                
            f[summ] -= 1
            
            if f[summ] == 0:
                del f[summ]
        
        dfs(root, 0)
        
        return ans
        # code here

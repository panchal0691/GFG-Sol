from collections import defaultdict

class Solution:
    def countPairs(self, root1, root2, x):
        f = defaultdict(int)
        ans = 0
        
        def dfs1(node):
            nonlocal f
            if not node:
                return
            
            f[node.data] += 1
            
            dfs1(node.left)
            dfs1(node.right)
        
        def dfs2(node):
            nonlocal ans
            if not node:
                return
            
            if x - node.data in f:
                ans += f[x - node.data]
                
            dfs2(node.left)
            dfs2(node.right)
        
        dfs1(root1)
        dfs2(root2)
        
        return ans

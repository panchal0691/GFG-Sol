class Solution:
    def KDistanceNodes(self, root, target, k):
        ans = []
        
        def dfs(cur, d):
            if cur is None:
                return -1
            
            if d == 0:
                ans.append(cur.data)
            
            if cur.data == target:
                dfs(cur.left, k - 1)
                dfs(cur.right, k - 1)
                
                return 1
            else:
                left = dfs(cur.left, -1 if d == -1 else d - 1)
                right = dfs(cur.right, -1 if d == -1 else d - 1)
                
                if left != -1:
                    if k - left > 0:
                        dfs(cur.right, k - left - 1)
                    
                    if k - left == 0:
                        ans.append(cur.data)
                        
                    return left + 1
                
                if right != -1:
                    if k - right > 0:
                        dfs(cur.left, k - right - 1)
                        
                    if k - right == 0:
                        ans.append(cur.data)
                        
                    return right + 1
                
                return -1
        
        dfs(root, -1)
        
        ans.sort()
        
        return ans

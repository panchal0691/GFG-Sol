class Solution:
    def __init__(self):
        self.mp = {}
    
    def preorder(self, node, level):
        if node is not None:
            if level in self.mp:
                self.mp[level] += node.data
            else:
                self.mp[level] = node.data
            
            self.preorder(node.left, level - 1)
            self.preorder(node.right, level + 1)
  
    def verticalSum(self, root):
        self.preorder(root, 0)
        ans = []
        for val in sorted(self.mp.keys()):
            ans.append(self.mp[val])
        return ans

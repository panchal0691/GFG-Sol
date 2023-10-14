class Solution:
    
    #Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        ans = []
        nodesInTree1 = {}
        self.inorder(root1, nodesInTree1)
        self.commonNodes(root2, nodesInTree1, ans)
        return sorted(ans)
 
    def inorder(self, root, m):
        if root is None:
            return
        self.inorder(root.left, m)
        m[root.data] = m.get(root.data, 0) + 1
        self.inorder(root.right, m)
 
    def commonNodes(self, root, nodesInTree1, ans):
        if root is None:
            return
        if root.data in nodesInTree1 and nodesInTree1[root.data] > 0:
            ans.append(root.data)
            nodesInTree1[root.data] -= 1
        self.commonNodes(root.left, nodesInTree1, ans)
        self.commonNodes(root.right, nodesInTree1, ans)
        # code here

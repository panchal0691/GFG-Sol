class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.result = []
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    def dfs(self, land, i, j, r2, c2):
        land[i][j] = 0
        
        r2[0] = max(r2[0], i)
        c2[0] = max(c2[0], j)
        
        for dir_ in self.directions:
            i_ = i + dir_[0]
            j_ = j + dir_[1]
            
            if 0 <= i_ < self.m and 0 <= j_ < self.n and land[i_][j_] == 1:
                self.dfs(land, i_, j_, r2, c2)
    
    def findFarmland(self, land):
        self.m = len(land)
        self.n = len(land[0])
        
        for i in range(self.m):
            for j in range(self.n):
                if land[i][j] == 1:
                    r1, c1 = i, j
                    r2, c2 = [-1], [-1]
                    
                    self.dfs(land, i, j, r2, c2)
                    self.result.append([r1, c1, r2[0], c2[0]])
        
        return self.result

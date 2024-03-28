class Solution {
  public:
    int findCity(int n, int m, vector<vector<int>>& edges, int distanceThreshold) {
        vector<vector<int>> d(n, vector<int> (n, 1e9));
        for(int i = 0; i < n; i++)
            d[i][i] = 0;
            
        for(auto i : edges) {
            d[i[0]][i[1]] = i[2];
            d[i[1]][i[0]] = i[2];
        }
            
        for(int k = 0; k < n; k++) {
            for(int i = 0; i < n; i++) {
                for(int j = 0; j < n; j++) {
                    if(d[i][k] != 1e9 and d[k][j] != 1e9)
                        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                }
            }
        }
        
        int best = n + 1;
        int ans = 0;
        for(int i = 0; i < n; i++) {
            int count = 0;
            
            for(int j = 0; j < n; j++) {
                if(d[i][j] <= distanceThreshold)
                    ++count;
            }
            
            if(count <= best)
                ans = i;
                
            best = min(best, count);
        }
        
        return ans;
    }
};

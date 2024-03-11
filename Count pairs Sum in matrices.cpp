class Solution{
public:	
	
	int countPairs(vector<vector<int>> &mat1, vector<vector<int>> &mat2, int n, int x)
	{
	    unordered_map<int, int> f;
	    
	    for(int i = 0; i < n; i++) {
	        for(int j = 0; j < n; j++)
	            ++f[mat2[i][j]];
	    }
	    
	    int ans = 0;
	    
	    for(int i = 0; i < n; i++) {
	        for(int j = 0; j < n; j++) {
	            ans += f[x - mat1[i][j]];
	        }
	    }
	    
	    return ans;
	}
};

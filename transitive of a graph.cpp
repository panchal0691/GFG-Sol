
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// Back-end complete function Template for C++

class Solution{
public:
    vector<vector<int>> transitiveClosure(int n, vector<vector<int>> graph)
    {
        vector<vector<int>> d = graph;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(!d[i][j])
                    d[i][j] = 1e8;
            }
            
            d[i][i] = 1;
        }
        
        for(int k = 0; k < n; k++){
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                }
            }
        }
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                d[i][j] = d[i][j] == 1e8 ? 0 : 1;
            }
        }
        
        return d;
    }
};

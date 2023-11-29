class Solution {
public:
	int isEulerCircuit(int V, vector<int>adj[]){
	    vector<bool> vis(V, 0);
	    int left = V;
	    
	    int ans = 0;
	    
	    function<void(int)> dfs = [&](int node) {
	        vis[node] = 1;
	        --left;
	        
	        for(auto child : adj[node]){
	            if(!vis[child]){
	                dfs(child);
	            }
	        }
	    };
	    
	    dfs(0);
	    
	    int odd = 0;
	    
	    for(int i = 0; i < V; i++){
	        if(!adj[i].size())
	            --left;
	    }
	    
	    for(int i = 0; i < V; i++){
	        if(adj[i].size() & 1){
	            ++odd;
	        }
	    }
	    
	    if(left or odd > 2)
	        return 0;
	    else if(odd)
	        return 1;
	    else 
	        return 2;
	}
};

class Solution {
  public:
    vector<int> eventualSafeNodes(int n, vector<int> adj[]) {
        vector<int> out(n, 0);
        
        vector<vector<int>> tg(n);
        
        for(int i = 0; i < n; i++){
            out[i] = adj[i].size();
            
            for(auto c : adj[i])
                tg[c].push_back(i);
        }
        
        vector<int> ans;
        queue<int> q;
        
        for(int i = 0; i < n; i++){
            if(!out[i]){
                ans.push_back(i);
                q.push(i);
            }
        }
        
        while(!q.empty()){
            int node = q.front();
            q.pop();
            
            for(auto child : tg[node]){
                --out[child];
                
                if(!out[child]){
                    q.push(child);
                    ans.push_back(child);
                }
            }
        }
        
        sort(ans.begin(), ans.end());
        
        return ans;
    }
};

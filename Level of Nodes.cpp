 vector<int> ans(V, 1e9);
        
        queue<int> q;
        ans[0] = 0;
        q.push(0);
        
        while(!q.empty()){
            int node = q.front();
            q.pop();
            
            for(auto child : adj[node]){
                if(ans[child] > ans[node] + 1){
                    ans[child] = ans[node] + 1;
                    q.push(child);
                }
            }
        }
        
        return ans[X] == 1e9 ? -1 : ans[X];
	}

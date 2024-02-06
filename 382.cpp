class Solution
{
    public:
    //Function to return count of nodes at a given distance from leaf nodes.
    int printKDistantfromLeaf(Node* root, int k)
    {
    	vector<Node*> path;
    	unordered_set<Node*> ans;
    	
    	function<void(Node *)> dfs = [&](Node * node) {
    	    if(!node)
    	        return;
    	        
    	    path.push_back(node);
    	        
    	    if(!(node -> left) and !(node -> right)){
    	        int p = (int)path.size() - 1 - k;
    	        
    	        if(p > -1)
    	            ans.insert(path[p]);
    	    }
    	    
    	    dfs(node -> left);
    	    dfs(node -> right);
    	    
    	    path.pop_back();
    	};
    	
    	dfs(root);
    	
    	return ans.size();
    }
};

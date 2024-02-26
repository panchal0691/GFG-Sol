class Solution{
	public:
		vector<string> AllPossibleStrings(string s){
		    vector<string> ans;
		    string cur = "";
		    
		    function<void(int)> sub = [&](int p) {
		        if(p == s.size()){
		            if(cur.size())
    		            ans.push_back(cur);
		            return;
		        }
		        
		        cur.push_back(s[p]);
		        sub(p + 1);
		        cur.pop_back();
		        sub(p + 1);
		    };
		    
		    sub(0);
		    
		    sort(ans.begin(), ans.end());
		    
		    return ans;
		}
};

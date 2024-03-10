class Solution{
public:
	string removeDuplicates(string str) {
	    unordered_map<char, bool> f;
	    string ans = "";
	    
	    for(auto i : str){
	        if(f.find(i) == f.end()){
	            ans += i;
	            f[i] = 1;
	        }
	    }
	    
	    return ans;
	}
};

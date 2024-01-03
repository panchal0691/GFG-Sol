class Solution {
  public:
    int smallestSubstring(string S) {
        vector<int> f(3, 0);
        int l, r;
        l = r = 0;
        bool ok = 0;
        int ans = 1e8;
        
        while(r < S.size() or l < r){
            if(!ok and r < S.size()){
                ++f[S[r++] - '0'];
                
                if(f[0] and f[1] and f[2])
                    ok = 1;
                else
                    ok = 0;
            }
            else if(l < r){
                --f[S[l++] - '0'];
                
                if(f[0] and f[1] and f[2])
                    ok = 1;
                else
                    ok = 0;
            }
            
            if(ok)
                ans = min(ans, r - l);
        }
        
        return ans == 1e8 ? -1 : ans;
    }
};

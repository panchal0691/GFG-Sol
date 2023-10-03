class Solution{
    public:
    string colName (long long int n)
    {
        --n;
        
        string ans = "";
        while(n > -1){
            int cur = n % 26;
            
            ans += (char)(cur + 'A');
            
            n /= 26;
            --n;
        }
        
        reverse(ans.begin(), ans.end());
        
        return ans;
    }
};

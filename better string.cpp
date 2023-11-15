class Solution {
  public:
    string betterString(string str1, string str2) {
        int n = str1.size();
        
        vector<int> sum(n + 1, 1), last(26, -1);
        
        for(int i = n - 1; i > -1; i--){
            int cur = sum[i + 1];
            int pos = last[str1[i] - 'a'];
            
            if(pos != -1)
                cur -= sum[pos + 1];
                
            last[str1[i] - 'a'] = i;
            sum[i] = sum[i + 1] + cur;
        }
        
        int a = sum[0];
        
        fill(last.begin(), last.end(), -1);
        
        for(int i = n - 1; i > -1; i--){
            int cur = sum[i + 1];
            int pos = last[str2[i] - 'a'];
            
            if(pos != -1)
                cur -= sum[pos + 1];
                
            last[str2[i] - 'a'] = i;
            sum[i] = sum[i + 1] + cur;
        }
        
        int b = sum[0];
        
        return (a >= b) ? str1 : str2;
    }
};

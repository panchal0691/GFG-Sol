
class Solution
{
  public:
    int minOperation(int n)
    {
        int ans = 0;
        
        for(int i = 0; i < 21; i++){
            if((n >> i) & 1)
                ans = i;
        }
        
        ans += __builtin_popcount(n);
        
        return ans;
    }
};

class Solution{
public:
    int knapSack(int N, int W, int val[], int wt[])
    {
        int dp[N + 1][W + 1];
        
        for(int i = 0; i < W + 1; i++)
            dp[N][i] = 0;
        
        for(int i = N - 1; i > -1; i--){
            for(int j = W; j > -1; j--){
                int take, notake;
                
                take = notake = 0;
                
                if(j + wt[i] <= W)
                    take = val[i] + dp[i][j + wt[i]];
                    
                notake = dp[i + 1][j];
                
                dp[i][j] = max(take, notake);
            }
        }
        
        return dp[0][0];
    }
};

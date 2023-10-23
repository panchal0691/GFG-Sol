class Solution{
		

	public:
	int maxSumIS(int arr[], int n)  
	{  
	    vector<int> dp(n + 1, 0);
	    
	    for(int i = n - 1; i > -1; i--){
            int take = arr[i];
	        
	        for(int j = i + 1; j < n; j++){
	            if(arr[j] > arr[i])
	                take = max(take, arr[i] + dp[j]);
	        }
	        
	        dp[i] = take;
	    }
	    
	    return *max_element(dp.begin(), dp.end());
	}  
};

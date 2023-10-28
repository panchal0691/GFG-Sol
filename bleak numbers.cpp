class Solution
{
public:
	int is_bleak(int n)
	{
	    for(int i = 0 ; i < 32; i++){
	        if(n - i > -1 and __builtin_popcount(n - i) == i)
	            return 0;
	    }
	    
	    return 1;
	}
};

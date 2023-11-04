class Solution
{
public:    
    
    int transitionPoint(int arr[], int n) {
        if(arr[0] == 1)
            return 0;
            
        int low = 0;
        int high = n;
        
        while(low < high - 1){
            int mid = low + (high - low) / 2;
            
            if(arr[mid] == 0)
                low = mid;
            else
                high = mid;
        }
        
        return high == n ? -1 : high;
    }
};

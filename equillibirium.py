def equilibriumPoint(self,A, N):
        
        sumArray=sum(A);
        
        ss=0
        
        for i in range(N):
            if(ss==sumArray-ss-A[i]): return i+1;
            
            ss+=A[i]
        
        return -1
        # Your code here


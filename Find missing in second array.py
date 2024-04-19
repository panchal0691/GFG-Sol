class Solution:
    def findMissing(self,a,b,n,m):
        st = set(b)
        
        ans = []
        for i in range(n):
            if a[i] not in st:
                ans.append(a[i])
                
        return ans

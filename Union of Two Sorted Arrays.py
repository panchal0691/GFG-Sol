class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        if arr1[0] > arr2[0]:
            return self.findUnion(arr2, arr1, m, n)
        
        ans = [arr1[0]]
        i, j = 1, 0
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if ans[-1] != arr1[i]:
                    ans.append(arr1[i])
                i += 1
            else:
                if ans[-1] != arr2[j]:
                    ans.append(arr2[j])
                j += 1
        
        while i < n:
            if ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i += 1
        
        while j < m:
            if ans[-1] != arr2[j]:
                ans.append(arr2[j])
            j += 1
        
        return ans

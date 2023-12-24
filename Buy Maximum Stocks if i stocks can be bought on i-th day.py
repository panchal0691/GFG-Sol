class Solution:
    def buyMaximumProducts(self, n, k, price):
        info = [(price[i], i + 1) for i in range(n)]
        info.sort()
        
        ans = 0
        
        for i in range(n):
            qty = k // info[i][0]
            qty = min(qty, info[i][1])
            
            ans += qty
            k -= qty * info[i][0]
        
        return ans

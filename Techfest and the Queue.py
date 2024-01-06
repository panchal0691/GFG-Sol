MAX = 2 * 10**5 + 10
smol = [MAX] * MAX
computed = False

def pre():
    global smol, computed
    smol[1] = 1
    for i in range(2, MAX):
        if smol[i] == MAX:
            smol[i] = i
            for j in range(i + i, MAX, i):
                smol[j] = min(smol[j], i)
    
    computed = True

class Solution:
    def sumOfPowers(self, a, b):
        global computed
        if not computed:
            pre()
        
        ans = 0
        for i in range(a, b + 1):
            cur = i
            while cur > 1:
                ans += 1
                cur //= smol[cur]
        
        return ans

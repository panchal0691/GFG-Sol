
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        # frac = []
        # for i in range(n):
        #     x = val[i]/w[i]
        #     frac.append(x)
        
        # frac.sort()
        
        
        
        arr.sort(key = lambda x: x.value / x.weight, reverse = True)
        curWeight = 0
        finalvalue = 0.0
        for i in range(n):
            if curWeight + arr[i].weight <=W:
                curWeight += arr[i].weight
                finalvalue += arr[i].value
            else:
                remain = W- curWeight
                finalvalue += arr[i].value / arr[i].weight *remain
                break 
        return finalvalue

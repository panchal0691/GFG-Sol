class Solution:
    def convertToEven(self, s):
        count = 0
        for i in range(len(s)):
            if (s[i] =="O" and i==0):
                count += 1
                
            elif i>0 and s[i]=='O' and s[i-1] == 'E':
                count +=1
        return count


class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        s1 += s1
        return s1.find(s2) != -1
        #code here

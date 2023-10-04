
class Solution:
    def romanToDecimal(self, s): 
        roman_to_decimal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
 
        sum = roman_to_decimal[s[-1]]
        for i in range(len(s) - 1):
            if roman_to_decimal[s[i]] < roman_to_decimal[s[i + 1]]:
                sum -= roman_to_decimal[s[i]]
            else:
                sum += roman_to_decimal[s[i]]
 
        return sum

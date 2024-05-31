
class Solution:
    def swapNibbles(self, n: int) -> int:
        # Get the right nibble
        rn = n & 0b11110000
        # Get the left nibble
        ln = n & 0b00001111
        
        # Shift right nibble to the right by 4 bits
        rn = rn >> 4
        # Shift left nibble to the left by 4 bits
        ln = ln << 4
        
        # Combine the nibbles
        return rn | ln

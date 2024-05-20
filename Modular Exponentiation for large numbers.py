class Solution:
    def PowMod(self, x: int, n: int, M: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return x % M

        val = self.PowMod(x, n // 2, M)
        val = (val * val) % M

        if n % 2 == 1:
            return (val * x) % M

        return val

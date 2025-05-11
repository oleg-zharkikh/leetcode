class Solution:
    def mySqrt(self, x: int) -> int:
        """Returns the square root of x rounded down to the nearest integer."""
        i = 1
        while i*i <= x:
            i += 1
            if i*i > x:
                return i-1
        return i-1


s = Solution
print(s.mySqrt(s, 26))

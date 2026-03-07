class Solution:
    def reverse(self, x: int) -> int:

        minus_mult = -1 if x < 0 else 1
        if x < 0:
            x *= -1
        r = 0
        while x > 0:
            a = x % 10
            x = x // 10
            r = r * 10 + a
            if r > 2147483647:
                return 0
        return r * minus_mult

print(Solution().reverse(-2147483412))

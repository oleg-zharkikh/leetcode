class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = 0
        n = 0
        while 10**i <= x:
            d = (x // 10**i) % 10
            n = n * 10 + d
            i += 1
        return n == x


a = Solution
print(a.isPalindrome(a, 12345654321))

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s if s[0] == s[-1] else s[0]
        max_len = 0
        l_max = 0
        r_max = 0
        for i in range(len(s) - 1):
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    max_len = right - left + 1
                    l_max = left
                    r_max = right
                left -= 1
                right += 1
            left, right = i, i + 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    max_len = right - left + 1
                    l_max = left
                    r_max = right
                left -= 1
                right += 1
        return s[l_max:r_max + 1]

        
        

#    0123456789012345678
s = "aaadabcbaaaac"

a = Solution()
print(a.longestPalindrome(s))

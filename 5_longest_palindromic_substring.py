class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s if s[0]==s[-1] else s[0]
        candidates = {i: (3 if s[i] == s[i+2] else 2) for i in range(len(s) - 2) if s[i] == s[i+1] or s[i] == s[i+2]}
        if s[-1] == s[-2]:
            candidates[len(s)-2] = 2
        if not candidates:
            return s[0]
        max_length_candidate_start_with = None
        max_length = 0

        for candidate_start_with in candidates:
            if max_length_candidate_start_with is None:
                max_length_candidate_start_with = candidate_start_with
                
            start = candidate_start_with
            end = start + candidates[candidate_start_with] - 1
            candidates[candidate_start_with] = end - start + 1
            while start - 1 > 0 and end + 1 < len(s):
                if s[start - 1] == s[end + 1]:
                    start -= 1
                    end += 1
                    candidates[candidate_start_with] = end - start + 1
                else:
                    break
            if candidates[candidate_start_with] > max_length:
                max_length = candidates[candidate_start_with]
                max_length_candidate_start_with = start
                
        return s[max_length_candidate_start_with:max_length_candidate_start_with + max_length]

#    0123456789012345678
s = "aaaa"
a = Solution()
print(a.longestPalindrome(s))

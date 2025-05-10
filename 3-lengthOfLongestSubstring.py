class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Find the length of the longest substring of s
        without duplicate characters."""
        if len(s) == 0:
            return 0
        map = dict()
        map[s[0]] = 0
        left = right = 0
        result = 1
        while right < len(s) - 1:
            right += 1
            if s[right] in map and map[s[right]] >= left:
                left = map[s[right]] + 1
            else:
                curr_length = right - left + 1
                result = curr_length if curr_length > result else result
            map[s[right]] = right
        return result


def main():
    print(Solution().lengthOfLongestSubstring('tmmzuxt'))
    print('expected: 5')

if __name__ == '__main__':
    main()

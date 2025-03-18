class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = s.split(' ')
        while '' in strs:
            strs.remove('')
        return len(strs[len(strs)-1])


a=Solution

s = "1"

print(a.lengthOfLastWord(a,s))

 
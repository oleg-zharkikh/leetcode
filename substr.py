class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #return str.find(haystack, needle)
        if len (needle) > len (haystack):
            return -1
        for i in range (0,len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

a = Solution
print(a. strStr(a,"a3453","a"))
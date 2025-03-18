class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ''
        for current_index in range(0,len(strs[0])):
            current_common_prefix = strs[0][current_index]
            for j in range(0,len(strs)):
                if len(strs[j]) == current_index:
                    return common_prefix
                if strs[j][current_index] != current_common_prefix:
                    return common_prefix
            common_prefix += current_common_prefix
        return common_prefix
            

a = Solution
str_1 = ["flower","flow","flight"]
print(a.longestCommonPrefix(a,str_1))

str_1 = ["dog","racecar","car"]
print(a.longestCommonPrefix(a,str_1))


str_1 = ["ab", "a"]
print(a.longestCommonPrefix(a,str_1))

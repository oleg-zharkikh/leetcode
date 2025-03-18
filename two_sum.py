class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_of_delta = {}
        for i in range(0, len(nums)):
            if nums[i] in dict_of_delta:
                return list((i, dict.get(dict_of_delta, nums[i])))
            delta = target - nums[i]
            dict_of_delta[delta] = i


#a = Solution
# print(a.twoSumOld(a, [2, 1, 4, 3], 5))
#print(a.twoSum(a, [2, 1, 4, 3], 5))




a = 82 // 3**2 % 7
print(a)
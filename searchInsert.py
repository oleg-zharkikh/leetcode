class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = 0
        if nums == []:
            return 0
        ln = len(nums)
        while i <ln:
            if nums[i] >= target:
                return i
            i += 1
        return i

a = Solution
nums = [1,3,5,6] #4
target = 7
print(a.searchInsert(a,nums,target))
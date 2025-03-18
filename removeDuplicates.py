class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nn = ['_' for i in range(0,len(nums))]
        nni = 0
        i = 0
        li = len(nums)-1
        dc = 0
        if len(nums) == 1:
            return 1
        while i <= li:
            if (i + 1) <= li:
                if nums[i] == nums[i+1]:
                    i += 1 
                else:
                    nn[nni] = nums[i]
                    nni += 1
                    i += 1
                    dc += 1
            else:
                nn[nni] = nums[i]
                nni += 1
                i += 1
                dc += 1
        for i in range(len(nums)):
            nums[i] = nn[i]
        return dc

a = Solution
nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1]
# nums = [1,2]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
print (a.removeDuplicates(a,nums))
print (nums)
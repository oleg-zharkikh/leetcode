class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        new_nums = []
        counter = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                new_nums.append(nums[i])
                counter += 1
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        return counter
    
a = Solution

#nums = [3,2,2,3]
#val = 3

nums =[0,1,2,2,3,0,4,2]
val = 2
print(a.removeElement(a,nums,val))
print(nums)
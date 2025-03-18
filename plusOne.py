class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        r = []
        flag = True
        i = len(digits)-1
        while flag and i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                flag = False
            else:
                digits[i] = 0
            i -= 1
        if flag == True:
            r.append(1)
        list.extend(r, digits) 
        return r
a = Solution

digits = [9,9,9,9]
print(a.plusOne(a,digits))

def  in_place_calc(nums: list[int]):
        new_num = [0 for i in range(0,len(nums))]
        for i in range(len(nums)):
            nums[i] = new_num[i]

def  why_does_not_assignment_work(nums: list[int]):
        new_num = [0 for i in range(0,len(nums))]
        nums = new_num  # почему при выходе из функции, значение nums не изменится?


nums = [0,1,2,4]
print (f'Массив ДО вызова функции: {nums}') 
in_place_calc(nums)
print (f'Массив после вызова функции: {nums}') # выдаст [0, 0, 0, 0]

nums = [0,1,2,4]
print (f'Массив ДО вызова функции: {nums}')
why_does_not_assignment_work(nums)
print (f'Массив после вызова функции: {nums}') # выдаст [0, 1, 2, 4]
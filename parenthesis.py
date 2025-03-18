class Solution:
    def isValid(self, s: str) -> bool:
        stack_of_p = []
        open_p = ['(','[','{']
        dict_of_close_p = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in open_p: # parentheses is oppening 
                stack_of_p.append(i)
            if i in dict_of_close_p: # parentheses is closing 
                len_of_stack = len(stack_of_p)
                if len_of_stack > 0 and stack_of_p[len_of_stack-1] == dict_of_close_p[i]:
                    stack_of_p = stack_of_p[0:len_of_stack-1]
                else: # there is no coincidence 
                    return False
        return True if stack_of_p == [] else False
                                


        

a = Solution
test_str = '()'
print(a.isValid(a,test_str))
class Solution:
    def romanToInt(self, s: str) -> int:
        i = len(s) - 1
        sum_digit = 0
        while i >= 0:
            digit = 0
            if s[i] == 'I':  # I
                if (i > 0) and s[i - 1] == 'I':  # II
                    if (i - 1 > 0) and s[i - 2] == 'I':  # III
                        digit = 3
                        i -= 2
                    else:
                        digit = 2
                        i -= 1
                else:
                    digit = 1
            if s[i] == 'V':  # V
                if (i > 0) and s[i - 1] == 'I':  # IV
                    digit = 4
                    i -= 1
                else:
                    digit = 5
            if s[i] == 'X':  # X
                if (i > 0) and s[i - 1] == 'I':  # IX
                    digit = 9
                    i -= 1
                else:
                    digit = 10
            if s[i] == 'L':  # L
                if (i > 0) and s[i - 1] == 'X':  # XL
                    digit = 40
                    i -= 1
                else:
                    digit = 50
            if s[i] == 'C':  # C
                if (i > 0) and s[i - 1] == 'X':  # XC
                    digit = 90
                    i -= 1
                else:
                    digit = 100
            if s[i] == 'D':  # D
                if (i > 0) and s[i - 1] == 'C':  # CD
                    digit = 400
                    i -= 1
                else:
                    digit = 500   
            if s[i] == 'M':  # M
                if (i > 0) and s[i - 1] == 'C':  # CM
                    digit = 900
                    i -= 1
                else:
                    digit = 1000          
            i -= 1 
            sum_digit += digit
        return sum_digit


a = Solution
print(a.romanToInt(a, 'LVIII'))  # 58
print(a.romanToInt(a, 'MCMXCIV'))  # 1994

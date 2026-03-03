class Solution:
    def myAtoi(self, s: str) -> int:
        """Converts a string to a 32-bit signed integer."""
        if s == '':
            return 0
        idx = 0
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        # 1. Whitespace: Ignore any leading whitespace (" ").
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        if idx == len(s):
            return 0
        # 2. Signedness: Determine the sign.
        multiplexer = 1
        if s[idx] == '-':
            multiplexer = -1
            idx += 1
        elif s[idx] == '+':
            multiplexer = 1
            idx += 1
        # 3. Conversion.
        while idx < len(s) and s[idx] in digits & {'0'}:
            idx += 1
        if idx == len(s):
            return 0
        number = ''
        while idx < len(s) and s[idx] in digits:
            number += s[idx]
            idx += 1
        # 4. Rounding.
        if (len(number) == 10 and number > '2147483647') or len(number) > 10:
            number = '2147483647' if multiplexer > 0 else '2147483648'
        digit = int(number) * multiplexer if len(number) > 0 else 0
        return digit


def main():
    s = " "
    print('result:  ', Solution().myAtoi(s))


if __name__ == '__main__':
    main()

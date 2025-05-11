"""Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
    """


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Return visual line of string s writen in a Z-pattern.  """
        DOWN = 0
        UP = 1
        row = 0
        col = 0
        dir = DOWN
        if numRows == 1:
            return s
        else:
            block_capacity = numRows + numRows - 1
            block_need = len(s) // block_capacity + 1
            col_need = block_need * numRows
        indexes = [[''] * col_need for i in range(numRows)]
        for chr in s:
            indexes[row][col] = chr
            if dir == DOWN:
                row += 1
            else:
                row -= 1
                col += 1
            if row == numRows:
                row = numRows - 2
                col += 1
                dir = UP
            elif row < 0:
                col -= 1
                row = 1
                dir = DOWN
        result = ''
        for line in indexes:
            result = result + ''.join(line)
        return result


def main():
    print('result:  ', Solution().convert('PAYPALISHIRING', 4))
    print('expected: PINALSIGYAHRPI')


if __name__ == '__main__':
    main()

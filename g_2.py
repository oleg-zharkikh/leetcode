
"""Робот-пылесос.
https://new.contest.yandex.ru/contests/80790/problems?id=149944%2F2025_08_30%2Ftk05cs1esG
"""
import sys

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def turn_left(cur_dir):
    return (-cur_dir[1], cur_dir[0])

def turn_right(cur_dir):
    return (cur_dir[1], -cur_dir[0])

def solve():
#     test1 = """
# 3 1
# .
# .
# .
# 2 1
# 6
# MLMLMM
# """

    data = iter(sys.stdin.read().split())
    # data = iter(test1.split())
    n, m = int(next(data)), int(next(data))
    # print(f'{n=} {m=}')
    g = [None] * n
    v = [[0 for i in range(m)] for j in range(n)]
    cur_dir = UP
    
    for i in range(n):
        line = [0 if item == '#' else 1 for item in list(next(data))]
        g[i] = line
    r, c = (int(next(data)) - 1, int(next(data)) - 1)
    # print(r)
    # print(c)
    v[r][c] = 1
    visited = 1

    commands_count = int(next(data))
    comms = list(next(data))
    # print(comms)
    for com in comms:
        # print(com)
        # print(f'direction:', cur_dir)
        if com == 'R':
            # print(f'→ Right')
            cur_dir = turn_right(cur_dir)
        elif com == 'M':
            # проверка, что есть куда двигаться
            if ((r + cur_dir[0] < n) and (r + cur_dir[0] >= 0) and 
                (c + cur_dir[1] < m) and (c + cur_dir[1] >= 0) and 
                g[r + cur_dir[0]][c + cur_dir[1]]):
                # print(f'→ M from {r, c} to {(r + cur_dir[0], c + cur_dir[1])}')
                r += cur_dir[0]
                c += cur_dir[1]
                if not v[r][c]:
                    v[r][c] = 1
                    visited += 1
            # else:
            #     print(r,c)
            #     print((r + cur_dir[0] < n) and (r + cur_dir[0] >= 0))
            #     print((c + cur_dir[1] < m) and (c + cur_dir[1] >= 0))
            #     if ((r + cur_dir[0] < n) and (r + cur_dir[0] >= 0) and 
            #         (c + cur_dir[1] < m) and (c + cur_dir[1] >= 0)):
            #             print(g[r + cur_dir[0]][c + cur_dir[1]])
        elif com == 'L':
            # print(f'→ LEFT')
            cur_dir = turn_left(cur_dir)

    print(visited)
    # for i in g:
    #     print(i)
    # for i in v:
    #     print(i)
        



        



if __name__ == '__main__':
    solve()
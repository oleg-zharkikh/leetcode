"""Матрица достижимости.

https://new.contest.yandex.ru/contests/80790/problems?id=149944%2F2025_09_09%2FpWz0JUQFB3
"""


import sys

def dfs(g: list[list[int]], node: int, visited: set, reacheable: set) -> None:
    if node in visited:
        return
    visited.add(node)
    for i in range(len(g)):
        if g[node][i]:
            dfs(g, i, visited, reacheable)
            reacheable.add(i)


def solve():    
    data = iter(sys.stdin.read().split())
    n = int(next(data))    
    g = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            g[i][j] = int(next(data))

    r = [[0 for i in range(n)] for j in range(n)]
    for ci in range(n):
        visited = set()
        reacheable = set()
        dfs(g, ci, visited, reacheable)
        for dest in reacheable:
            r[ci][dest] = 1
    for line in r:
        print(' '.join(map(str, line)))


if __name__ == '__main__':
    
    solve()
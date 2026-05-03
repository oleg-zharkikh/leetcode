"""Дружный граф.

https://new.contest.yandex.ru/contests/80790/problems?id=149944%2F2025_09_10%2FS714qWxfiv
"""

import sys
from collections import defaultdict

def solve():    
    data = iter(sys.stdin.read().split())
    g = defaultdict(list)
    all_nodes = set()
    n = int(next(data))
    c_group = 1
    for i in range(n):
        k = int(next(data))
        for j in range(k):
            node_idx = int(next(data))
            g[c_group].append(node_idx)
            all_nodes.add(node_idx)
        c_group += 1
    nodes = max(all_nodes) - 1
    gr = [[0 for i in range(nodes + 1)] for j in range(nodes + 1)]
    for group in g.keys():
        connected = g[group]
        for i in connected:
            for j in connected:
                if i != j:
                    gr[i-1][j-1] = 1

    print(len(gr))
    for line in gr:
        print(' '.join(map(str, line)))

if __name__ == '__main__':
    solve()
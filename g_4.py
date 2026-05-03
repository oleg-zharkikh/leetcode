"""Корпоративные связи.

https://new.contest.yandex.ru/contests/80790/problems?id=149944%2F2025_09_10%2FOC6jtHVJG8
"""

import sys
from collections import defaultdict

def solve():    
    data = iter(sys.stdin.read().split())
    departments_data = defaultdict(list)
    d = int(next(data))
    depto_idx = 1
    all_persons = set()
    for i in range(d):
        k = int(next(data))
        for j in range(k):
            person = int(next(data))
            departments_data[depto_idx].append(person)
            all_persons.add(person)
        depto_idx += 1
    
    g = [[0 for i in range(len(all_persons))]  for j in range(len(all_persons))]    
    for dept in departments_data.keys():
        head, *dept_body = departments_data[dept]
        for person in dept_body:
            g[head - 1][person - 1] = 1
            g[person - 1][head - 1] = -1

    for line in g:
        print(' '.join(map(str, line)))

if __name__ == '__main__':
    solve()


def is_good_desicion(a, b) -> bool:
    if len(a) != len(b):
        return False
    for i in range(len(b)):
        if a[i] == b[i]:
            return False
    return True

from collections import Counter

if __name__ == '__main__':
    n = int(input())
    # n = 3
    chars = input()
    # chars = 'aabbc'
    comp = input()
    # comp = 'abcaa'
    # comp_d = {position: comp[position] for position in range(len(comp))}

    result = ''
    chars_counts = Counter(chars)
    # print(chars_counts)
    result = []
    
    def backtrack(position):
        if position == n:
            return True
        for candidate in ('a', 'b' ,'c'):
            if chars_counts[candidate] > 0 and candidate != comp[position]:
                chars_counts[candidate] -= 1
                result.append(candidate)
                # проверяем следующую позицию
                if backtrack(position + 1):
                    return True
                # неудачно - backtracking
                result.pop()
                chars_counts[candidate] += 1
        return False

    backtrack(0)
    result = ''.join(result)
    print(result)

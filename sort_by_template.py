def sort_by_patern(arr, n, pattern, k):
    position = dict()
    for idx, item in enumerate(pattern):
        position[item] = idx
    s_p = set(pattern)
    s_a = set(arr)
    delta = sorted(list(s_a - s_p))
    for item in delta:
        idx += 1
        position[item] = idx

    for i in range(1, len(arr)):
        current = arr[i]
        prev = i - 1
        while prev >= 0 and position[arr[prev]] > position[current]:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = current
    return arr

def main() -> None:
    n = int(input())
    arr = [int(x) for x in input().split()]
    k = int(input())
    pattern = [int(x) for x in input().split()]

    # n = 10
    # arr = [6, 4, 3, 5, 2, 0, 9, 8, 7, 7]
    # k = 6
    # pattern = [2, 4, 3, 5, 6, 0]

    result = sort_by_patern(arr, n, pattern, k)
    for _ in result:
        print(_, end=' ')


if __name__ == '__main__':
    main()

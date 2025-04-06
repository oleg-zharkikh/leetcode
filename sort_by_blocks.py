def is_there_smaller_next(arr, pointer, max_value):
    for i in range(pointer, len(arr)):
        if arr[i] < max_value:
            return True
    return False


def sort_by_blocks(arr, n):
    block_counter = 0
    pointer = 0
    max_value = 0
    r = 0
    while pointer < len(arr):
        if arr[pointer] > max_value:
            max_value = arr[pointer]
        if arr[pointer] == r:
            while is_there_smaller_next(arr, pointer + 1, max_value):
                pointer += 1
            r = max_value + 1
            block_counter += 1
        pointer += 1
    return block_counter


def main() -> None:
    n = int(input())
    arr = [int(x) for x in input().split()]

    result = sort_by_blocks(arr, n)
    print(result)


if __name__ == '__main__':
    main()

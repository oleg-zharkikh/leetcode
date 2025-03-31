def main(nums):
    cache = dict()
    ns = [0] * len(nums)
    nn = [0] * len(nums)
    for i in range(0, len(nums)):
        ns[i] = int(nums[i])
        nn[i] = int(nums[i])
    ns.sort(reverse=True)
    result = [0] * len(nums)

    for i in range(0, len(nums)):
        if nn[i] in cache:
            result[i] = str(cache[nn[i]])
        else:
            j = len(nums)-1
            cnt = 0
            while ns[j] < nn[i]:
                j -= 1
                cnt += 1
            result[i] = str(cnt)
            cache[nn[i]] = cnt # сохраняем данные в кеш
    return result


if __name__ == '__main__':
    #nums = '6 5 4 8'.split()
    nums = input().split()
    result = main(nums)
    print(' '.join(result))

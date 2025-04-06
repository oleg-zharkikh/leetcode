def distribute_samples(orders, n, samples, k):
    satisfied_customers = 0
    orders.sort()
    samples.sort()

    idx_sample = 0
    while idx_sample < len(samples) and len(orders) > 0:
        if samples[idx_sample] >= orders[0]:
            del orders[0]
            satisfied_customers += 1
        idx_sample += 1
    return satisfied_customers


def main() -> None:
    n = int(input())
    orders = [int(x) for x in input().split()]
    k = int(input())
    samples = [int(x) for x in input().split()]

    # n = 10
    # orders = [8, 2, 4, 7, 8, 5, 5, 8, 6, 9]
    # k = 8
    # samples = [9, 8, 1, 1, 1, 5, 10, 8, 2, 7, 4, 3, 15]

    print(distribute_samples(orders, n, samples, k))


if __name__ == '__main__':
    main()

def get_counterer(p, k, s):
    if len(p) == 1:
        return p[0]
    else:
        pointer = (s + k - 1) % len(p)
        del p[pointer]
        return get_counterer(p, k, pointer)


def main() -> None:
    n = int(input())
    k = int(input())

    persons = [i+1 for i in range(n)]

    winner = get_counterer(persons, k, 0)
    print(winner)


if __name__ == '__main__':
    main()

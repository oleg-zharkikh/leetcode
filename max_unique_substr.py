def is_set(text):
    s = set()
    for i in text:
        if i not in s:
            s.add(i)
    return len(s) == len(text)


def is_window_unuque(text, size):
    s = set()
    for i in range(0, len(text)-size + 1):
        for j in range(0, size):
            if is_set(text[i:i+size]):
                return True
    return False


def main(text):
    i = 1
    while is_window_unuque(text, i):
        i += 1
    return i - 1


if __name__ == '__main__':
    text = input()
    #text = 'awe' #3
    #fprarfpoz 6

    result = main(text)
    print(result)


# import math

def decision(n):
    # t = 7 * 24 * 60 # минут в неделе

    if n == 1:
        print(0)
        return

    if n % 2 == 0:
        print(-1)
        return

    c = n * n - 1
    # E = (n ** 2 - 1) / 2
    # prob = 1 - math.exp(-1 * t / E)
    if n >= 83:
    # if prob < 0.95:
        print(-1)
        return

    print(c)

if __name__ == '__main__':
    n = int(input())
    
    decision(n)
    
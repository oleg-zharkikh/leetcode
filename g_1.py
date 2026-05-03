"""
Граф из списка маршрутов
https://new.contest.yandex.ru/contests/80790/problems?id=149944%2F2025_08_30%2FesfoDkMjLn
"""

def main():
    # ввод данных
    line_1 = input()
    n, m = line_1.split()
    n = int(n)
    m = int(m)

    # инициализация пустой матрицы смежности
    g = [[0 for i in range(n)] for j in range(n)]
    g_1 = [[0 for i in range(n)] for j in range(n)]

    for i in range(m):
        line = input()
        stops = list(map(int, line.split()))
        k = stops.pop(0)
        # G - остановки -- вершины, ребра -- соседние остановки на любом из маршрутов.
        for idx in range(len(stops) - 1):
            g[stops[idx]-1][stops[idx + 1]-1] = 1
            g[stops[idx + 1]-1][stops[idx]-1] = 1
        # остановки -- вершины, ребра -- любые две остановки, достижимые без пересадок
        for s1 in stops:
            for s2 in stops:
                g_1[s1-1][s2-1] = 1
                g_1[s2-1][s1-1] = 1

    for i in range(n):
        g[i][i] = 0
        g_1[i][i] = 0
    # вывод данных
    for line in g:
        print(' '.join(list(map(str, line))))
    for line in g_1:
        print(' '.join(list(map(str, line))))



if __name__ == '__main__':
    main()
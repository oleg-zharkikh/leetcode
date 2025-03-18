def find_lcs(seq1, seq2):
    # Длины последовательностей
    m = len(seq1)
    n = len(seq2)
    # Создаем таблицу dp размером (m+1) x (n+1), заполненную нулями
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Заполняем таблицу dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # Восстановление LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.append(seq1[i - 1])  # Добавляем совпадающий элемент
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    # LCS строился с конца, поэтому разворачиваем его
    lcs.reverse()
    return lcs


text_1 = 'Queretaro'
text_2 = 'Qrt'
seq1 = list(text_1)
seq2 = list(text_2)

result = find_lcs(seq1, seq2)
print("LCS:", ''.join(result))
import re


def parse_csv_line(line, delimiter=',', quote_char='"'):
    """
    Парсит строку CSV с учетом кавычек и вложенных кавычек.

    Args:
        line (str): Входная строка CSV
        delimiter (str): Символ-разделитель (по умолчанию ',')
        quote_char (str): Символ кавычки (по умолчанию '"')

    Returns:
        list: Список значений колонок
    """
    pattern = re.compile(
        f'''((?:{quote_char}(?:[^{quote_char}]|{quote_char}{quote_char})*{quote_char}|[^{delimiter}{quote_char}])+)(?:{delimiter}|$)''')

    matches = pattern.finditer(line)
    result = []

    for match in matches:
        value = match.group(1).strip()
        # Удаляем обрамляющие кавычки, если они есть
        if value.startswith(quote_char) and value.endswith(quote_char):
            value = value[1:-1]
            # Заменяем двойные кавычки на одинарные
            value = value.replace(quote_char * 2, quote_char)
        result.append(value)

    return result


# Пример использования
if __name__ == "__main__":
    test_line = 'one,two,"three with, comma","four with ""quotes"" inside",five'
    print(parse_csv_line(test_line))
    # Вывод: ['one', 'two', 'three with, comma', 'four with "quotes" inside', 'five']

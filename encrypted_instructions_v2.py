# Номер успешной посылки по задаче:
# 136370929

CURRENT_MULTIPLIER = 0
"""Индекс хранения множителя в парах значений стека."""

CURRENT_MESSAGE = 1
"""Индекс хранения подстроки в парах значений стека."""

BLOCK_START_CHR = '['
"""Символ начала мультиплицируемой строки."""

BLOCK_END_CHR = ']'
"""Символ окончания мультиплицируемой строки."""


def decrypt_message(short_message: str) -> str:
    """Возвращает полную форму команды управления Марсоходом.

    Args:
        short_message (str): сжатое сообщение с командами.

    Returns:
        str: полная форма команды.
    """
    pointer = 0
    stack = []
    stack.append(['1', ''])
    multiplier = ''
    while pointer < len(short_message):
        if short_message[pointer].isdecimal():
            multiplier += short_message[pointer]
        elif short_message[pointer] == BLOCK_START_CHR:
            stack.append([multiplier, ''])
            multiplier = ''
        elif short_message[pointer] == BLOCK_END_CHR:
            multiplier, multiplied_message = stack.pop()
            stack[len(stack)-1][CURRENT_MESSAGE] += (
                multiplied_message * int(multiplier)
            )
            multiplier = ''
        else:
            stack[len(stack)-1][CURRENT_MESSAGE] += short_message[pointer]
        pointer += 1
    return stack[len(stack)-1][CURRENT_MESSAGE]


def main() -> None:
    """Обрабатывает ввод, выполняет вычисления и выводит результат.

    Считывает команду в сжатом формате, вызывает функцию декодирования,
    затем выводит результат на экран.
    """
    short_command = input()
    full_command = decrypt_message(short_command)
    print(full_command)


if __name__ == '__main__':
    main()

# Номер успешной посылки по задаче:
# 136255345

def get_multiplied_part(pointer: int, message: str) -> tuple[int, str]:
    """Возвращает всю мультиплицируемую часть подстроки, которая заключена
    в квадратные скобки после множителя. Может содержать вложенные
    скобки.

    Args:
        pointer (int): начальная позиция мультиплицируемой подстроки.
        message (str): полная строка с сообщением.

    Returns:
        tuple[int, str]: кортеж, содержащий индекс элемента, следующего после
        найденной подстроки и мультиплицируемую строку.
    """
    bracket_stack = ['[']
    index = pointer + 1
    inner_message = ''
    while index < len(message) and len(bracket_stack) > 0:
        if message[index] == '[':
            bracket_stack.append('[')
        elif message[index] == ']':
            bracket_stack.pop()
        inner_message += message[index]
        index += 1
    return index-1, inner_message[:-1]


def decrypt_message(short_message: str) -> str:
    """Возвращает полную форму команды управления Марсоходом.

    Args:
        short_message (str): сжатое сообщение с командами.

    Returns:
        str: полная форма команды.
    """
    result = ''
    pointer = 0
    while pointer < len(short_message):
        if short_message[pointer].isdecimal():
            multiplier_part = short_message[pointer]
            while short_message[pointer + 1].isdecimal():
                multiplier_part += short_message[pointer + 1]
                pointer += 1
            multiplier = int(multiplier_part)
            pointer, inner_message = get_multiplied_part(
                                        pointer + 1,
                                        short_message
                                        )
            result += multiplier * decrypt_message(inner_message)
        else:
            result += short_message[pointer]
        pointer += 1
    return result


def main() -> None:
    """Ввод сжатого сообщения с командой,
    расшифровка и вывод на экран полной формы команды.
    """
    short_command = input()
    full_command = decrypt_message(short_command)
    print(full_command)


if __name__ == '__main__':
    main()

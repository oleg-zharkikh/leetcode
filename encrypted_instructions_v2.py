# Номер успешной посылки по задаче:
# 136314336

# Константы адресной части элементов стека
MUL = 0
MESSAGE = 1

# Константы, задающие символы управления в сжатой инструкции
BLOCK_START_CHR = '['
BLOCK_END_CHR = ']'


class Stack(list):
    """Реализация стека на основе списка.

    Каждый элемент стека - пара "множитель" - "текущая подстрока".
    """

    def __init__(self, *args) -> None:
        """Инициализирует стек, добавляя начальный элемент."""
        super().__init__(*args)
        self.append(['1', ''])

    def modify_top(self, part: int, value: str) -> None:
        """Добавляет значение в указанную часть верхнего элемента стека.

        Args:
            part (int): Индекс редактируемой части верхнего элемента.
            value (str): Строка, которая будет добавлена к выбранной части.
        """
        top_index = len(self) - 1
        self[top_index][part] += value

    def multiplx_pop(self) -> str:
        """Возвращает мультиплицированную строку из стека.

        Returns:
            str: мультиплицированная строка.
        """
        multiplier, current_block = self.pop()
        return int(multiplier) * current_block


def decrypt_message(short_message: str) -> str:
    """Возвращает полную форму команды управления Марсоходом.

    Args:
        short_message (str): сжатое сообщение с командами.

    Returns:
        str: полная форма команды.
    """
    pointer: int = 0
    stack = Stack()
    multiplier: str = ''
    while pointer < len(short_message):
        if short_message[pointer].isdecimal():
            multiplier += short_message[pointer]
        elif short_message[pointer] == BLOCK_START_CHR:
            stack.append([multiplier, ''])
            multiplier = ''
        elif short_message[pointer] == BLOCK_END_CHR:
            stack.modify_top(MESSAGE, stack.multiplx_pop())
            multiplier = ''
        else:
            stack.modify_top(MESSAGE, short_message[pointer])
        pointer += 1
    return stack.multiplx_pop()


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

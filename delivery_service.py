# номер успешной посылки:
# 135826469
def get_min_count_of_platforms(
        robot_weights: list[int],
        platform_payload: int
        ) -> int:
    """Вычисляет минимальное количество платформ для отправки роботов.

    Args:
        robot_weights (list): отсортированный по возрастанию массив,
        содержащий массу каждого робота.
        platform_payload (int): максимальная грузоподъемность каждой платформы.

    Returns:
        int: минимальное число платформ для транспортировки всех роботов.
    """
    sent_platform = 0
    left_pointer = 0
    right_pointer = len(robot_weights) - 1
    while left_pointer <= right_pointer:
        if left_pointer == right_pointer:
            return sent_platform + 1
        result = robot_weights[left_pointer] + robot_weights[right_pointer]
        if result > platform_payload:
            right_pointer -= 1
        else:
            right_pointer -= 1
            left_pointer += 1
        sent_platform += 1
    return sent_platform


def main() -> None:
    """Ввод входных данных, подсчет числа необходимых платформ и вывод
    результата вычисления.
    """
    robot_data = input().split()
    platform_payload = int(input())
    robot_weights = [int(robot_weight) for robot_weight in robot_data]
    robot_weights.sort()
    print(get_min_count_of_platforms(robot_weights, platform_payload))


if __name__ == '__main__':
    main()

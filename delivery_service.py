# номер успешной посылки:
# 135884373
def get_min_count_of_platforms(
        robot_weights_arr: list[int],
        platform_payload: int
        ) -> int:
    """Вычисляет минимальное количество платформ для отправки роботов.

    Args:
        robot_weights (list): массив, содержащий массу каждого робота.
        platform_payload (int): максимальная грузоподъемность каждой платформы.

    Returns:
        int: минимальное число платформ для транспортировки всех роботов.
    """
    robot_weights = sorted(robot_weights_arr)
    sent_platform = 0
    left_pointer = 0
    right_pointer = len(robot_weights) - 1
    while left_pointer <= right_pointer:
        total_weight = (robot_weights[left_pointer] +
                        robot_weights[right_pointer])
        if total_weight <= platform_payload:
            left_pointer += 1
        right_pointer -= 1
        sent_platform += 1
    return sent_platform


def main() -> None:
    """Ввод входных данных, преобрадование данных,
    подсчет числа необходимых платформ и вывод
    результата вычисления.
    """
    robot_data = input()
    platform_data = input()

    robot_weights = [int(robot_weight) for robot_weight in robot_data.split()]
    platform_payload = int(platform_data)

    number_of_vehicles = get_min_count_of_platforms(
        robot_weights,
        platform_payload
        )
    print(number_of_vehicles)


if __name__ == '__main__':
    main()

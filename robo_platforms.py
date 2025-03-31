# номер успешной посылки:
# 135746317
def transportation(robot_weights: list, max_payload: list) -> int:
    """Вычисляет мин. количество платформ для отправки роботов.

    Args:
        robot_weights (list): список, содержащий массу каждого робота.
        max_payload (list): максимальная грузоподъемность каждой платформы.

    Returns:
        int: минимальное число платформ для транспортировки всех роботов.
    """
    sent_platforms = 0
    current_payload = max_payload
    # на каждой итерации добиваемся максимальной загрузки платформы
    # одним или двумя роботами с максимально допустимым общим весом
    while len(robot_weights) > 1 and current_payload > 0:
        delta_to_payload = dict()
        is_robot_sent = False
        current_position = 0
        for idx in range(current_position, len(robot_weights)):
            robot_weight = robot_weights[idx]
            # если найден робот с весом грузоподъемности платформы - отправляем
            if robot_weight == current_payload:
                del robot_weights[idx]
                sent_platforms += 1
                is_robot_sent = True   # могут быть еще роботы ...
                current_position = idx - 1   # ... ищем робота дальше по списку
                break
            else:
                # если есть пара роботов для отправки на 1 платформе
                if robot_weight in delta_to_payload:
                    position = delta_to_payload[robot_weight]
                    del robot_weights[idx]
                    del robot_weights[position]
                    del delta_to_payload[robot_weight]
                    sent_platforms += 1
                    is_robot_sent = True   # могут быть еще пары для отправки
                    break
                else:
                    # Пара не найдена.
                    # Добавляем в словарь,
                    # где ключ - целевая "дельта" до макс. грузоподъемности
                    delta_to_payload[current_payload-robot_weight] = idx
        if not is_robot_sent:
            current_payload -= 1
    # может оставаться робот, для которого не нашлось пары
    if len(robot_weights) > 0:
        sent_platforms += 1
    return sent_platforms


robots = input().split()
max_payload = int(input())
robots = [int(i) for i in robots]
print(transportation(robots, max_payload))

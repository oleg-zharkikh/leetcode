def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.
    if len(list_set_1) >= len(list_set_2):
        short_set = list_set_2
        long_set = list_set_1
    else:
        short_set = list_set_1
        long_set = list_set_2
    is_all_equal = True
    for i in short_set:
        if i not in long_set:
            is_all_equal = False
    if is_all_equal and len(list_set_1) == len(list_set_2):
        message = 'Наборы равны.'
    elif is_all_equal:
        message = f'Набор {long_set} - супермножество.'
    else:
        message = 'Супермножество не обнаружено.'
    return message

# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
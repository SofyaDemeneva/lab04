def count_common_elements(*lists):
    if not lists:
        return 0

    # Используем set для нахождения общих элементов во всех списках
    common_elements = set(lists[0])  # Начинаем с первого списка
    for lst in lists[1:]:
        common_elements &= set(lst)  # Берём пересечение с каждым последующим списком

    return len(common_elements)


# Пример использования
if __name__ == "__main__":
    # Пример списков
    list1 = [1, 2, 3, 4, 0]
    list2 = [3, 4, 5, 6, 0]
    list3 = [4, 7, 8, 3, 0]

    # Вызов функции и вывод результата
    result = count_common_elements(list1, list2, list3)
    print(f"Количество одинаковых элементов во всех списках: {result}")

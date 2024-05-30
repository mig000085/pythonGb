def find_indices_in_range(list_1, min_number, max_number):
    # Создаем список для хранения индексов элементов, которые попадают в заданный диапазон
    indices = []
    # Проходим по всем элементам списка и их индексам
    for i, value in enumerate(list_1):
        # Проверяем, попадает ли значение в диапазон
        if min_number <= value <= max_number:
            indices.append(i)
    return indices

# Примеры использования:
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10
result = find_indices_in_range(list_1, min_number, max_number)

# Выводим результат
for index in result:
    print(index)

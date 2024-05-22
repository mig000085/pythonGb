# Встречаемость элемента в массиве
# Инструкция по использованию платформы
# Требуется вычислить, сколько раз встречается некоторое
# число k в массиве list_1.
# Найдите количество и выведите его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# 1

list_1 = [1, 2, 3, 4, 5]
k = 3

# Введите ваше решение ниже
def count_occurrences(list_1, k):
    count = 0
    for num in list_1:
        if num == k:
            count += 1
    return count


result = count_occurrences(list_1, k)
print(result)
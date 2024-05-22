# Ближайший элемент в массиве
# Требуется найти в массиве list_1 самый близкий 
# по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один.
# Если значение k совпадает с этим элементом - выведите его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

list_1 = [1, 2, 3, 4, 5]
k = 6

# Введите ваше решение ниже

def find_closest(list_1, k):
    closest = list_1[0]
    min_diff = abs(list_1[0] - k)

    for num in list_1:
        diff = abs(num - k)
        if diff < min_diff:
            min_diff = diff
            closest = num

    return closest

result = find_closest(list_1, k)
print(result)
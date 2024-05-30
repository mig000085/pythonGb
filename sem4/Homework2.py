def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)

# Примеры использования:
print(sum(2, 2))  # Вывод: 4
print(sum(3, 5))  # Вывод: 8
print(sum(0, 0))  # Вывод: 0

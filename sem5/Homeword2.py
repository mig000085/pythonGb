def arithmetic_progression(a1, d, n):
    # Создаем список для хранения элементов прогрессии
    progression = []
    # Заполняем список элементами прогрессии
    for i in range(n):
        an = a1 + i * d
        progression.append(an)
    return progression

# Примеры использования:
a1 = 2
d = 3
n = 4
result = arithmetic_progression(a1, d, n)

# Выводим результат
for value in result:
    print(value)

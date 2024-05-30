def f(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / f(a, -b)
    else:
        return a * f(a, b - 1)

# Примеры использования:
a = 3
b = 5
print(f(a, b))  # Вывод: 243

a = 2
b = 3
print(f(a, b))  # Вывод: 8

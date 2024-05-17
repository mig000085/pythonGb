# Создать новый проект в пустой папке (рабочего пространства)
# python3 -m venv .folder
 
# print(5)
# чтобы запустить программный код, 
# используйте следующую командув терминале
# python name_file.py
# Где name_file - имя вашего файла

# Базовые типы данных Python:
# int Целые числа
# float Дробные числа
# bool Логический тип данных (True/False)
# str Строка

# a = 123
# b = 1.23
# print(a)
# print(b)

# value = None
# a = 123
# b = 1.23
# print(a)
# print(b)
# value = 1234
# print(value)

# print(type(name)) функция, которая указывает на тип данных

# s = ‘hello,’ # создание 1-ой строки
# s = “world” # создание 2-ой строки
# print(s, w)
 
# a = 3
# b = 11
# s = 2022
# print(a, b, s)
# print(a,' - ',b,' - ',s)
# print('{} - {} - {}'.format(a,b,s))
# print(f'first - {a} second - {b} third - {s}')

#input() #ввод даных
# print('введите первоую строку: ')
# a = int (input())
# b = int (input('Введите второе число: '))
# print(a, '+',b,'=',a+b)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# a = 5.5858
# b = 6.586849
# print(round(a*b, 3))

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# a = 1 > 4
# print(a) # False

# a = 1 < 4 and 5 > 2
# print(a) # True

# a = 1 == 2
# print(a) # False

# a = 1 != 2
# print(a) # True

# a = 'qwe'
# b = 'qwe'
# print(a == b) # True

# a = 1 < 3 < 5 < 10
# print (a) # True

# # username = input('Введите имя: ')
# # if username == 'Маша':
# #     print('Ура, это же МАША!')
# # elif username == 'Марина':
# #     print('Я так ждала Вас, Марина!')
# # elif username == 'Ильнар':
# #     print('Ильнар - топ)')
# # else:
# #     print('Привет, ', username)

# # i = 0
# # while i < 5:
# #     if i == 3:
# #         break
# #     i = i + 1
# # else:
# #     print('Пожалуй')
# #     print('хватит )')
# # print(i)


# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленноена 2
#         print(n)
#         flag = False
#     i += 1

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # 39
#print('ещё' in text) # True
#print(text.lower()) # съешь ещё этих мягких французских булок
#print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
#print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

#text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
#text = text[2:9] + text[-5] + text[:2] # ...

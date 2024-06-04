from logger import input_data, print_data, modify_data, select_and_delete_data

def interface():
    print("Добрый день! Вы попали на спецальный бот справочник от GeekBrains! \n 1-запись данных \n 2- вывод данных  \n 3- изменить даныее \n 4- Удалить данные")
    command = int(input('Введите число '))


    while command < 1 and command > 4:
        print("Неправильный ввод")    
        command = int(input('Введите число '))
    
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        modify_data()
    elif command == 4:
        select_and_delete_data()
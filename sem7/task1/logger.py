from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каои формате записать данные \n\n"
    f"1 Вариант: \n" 
    f"{name}/n{surname}/n{phone}/n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")    
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
        
        
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")
    

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list)) 
        
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)
        
def modify_data():
    with open("data_first_variant.csv", "r+", encoding="utf-8") as file:
        data = file.readlines()
        print("Доступные данные из файла 'data_first_variant.csv':")
        for i, line in enumerate(data):
            print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно изменить: "))
        if selection>0 and selection<= len(data):
            new_data = input("Введите новые данные: ")
            data[selection-1] = new_data + '\n'
            file.seek(0)
            file.writelines(data)
            file.truncate()
        else:
            print("Некорретный номер данных.")
    print ()
    with open("data_second_variant.csv", "r+", encoding="utf-8") as file:
        data = file.readlines()
        print("Доступные данные из файла 'data_second_variant.csv':")
        for i, line in enumerate(data):
            print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно изменить: "))
        if selection>0 and selection<= len(data):
            new_data = input("Введите новые данные: ")
            data[selection-1] = new_data + '\n'
            file.seek(0)
            file.writelines(data)
            file.truncate()
        else:
            print("Некорретный номер данных.")

def select_and_delete_data():
        with open("data_first_variant.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
        print("Доступные данные из файла 'data_first_variant.csv' (введите 0 чтобы перейти к следующему файлу):")
        for i, line in enumerate(data):
            print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно удалить: "))
        with open("data_first_variant.csv", "w", encoding="utf-8") as file:
            for i, line in enumerate(data):
                if i+1 != selection:
                    file.write(line)
                    
        with open("data_second_variant.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
        print("Доступные данные из файла 'data_second_variant.csv' (введите 0 чтобы выйти):")
        for i, line in enumerate(data):
            print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно удалить: "))
        with open("data_second_variant.csv", "w", encoding="utf-8") as file:
            for i, line in enumerate(data):
                if i+1 != selection:
                    file.write(line)



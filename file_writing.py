'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''
# ДЗ 
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt
def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue

    last_name = "Иванов"

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]


def create_file(file_name):
    # with - Менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телофон уже есть")
            return

    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

# Выполнение ДЗ 
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def del_contact_file(file_name):
    del_id = int(input("Введите номер строки для удаления: "))
    res = read_file(file_name)
    for el in res:
        if res.index(el) == del_id - 2:
            print(f"Запись №{res.index(el)+2}:")
            print(*el.values(), " - удалена")
            res.remove(el)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)
        
def get_first_name():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue
    return first_name
def get_last_name():
    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input("Введите фамилию: ")
            if len(last_name) < 2:
                raise NameError("Не валидная фамилия")
            else:
                is_valid_last_name = True
        except NameError as err:
            print(err)
            continue
    return last_name
def get_phone_number():
    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер телефона: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера телефона")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except LenNumberError as err:
            print(err)
            continue
    return phone_number

def editing_contact_file(file_name):
    res = read_file(file_name)
    print (res)
    is_valid_line_number = False
    while not is_valid_line_number:
        try:
            line_number = int(input("Введите номер строки для изменения: "))
            if line_number == 1:
                raise NameError("Это заголовок, контакты начинаются со второй строки")
            else:
                is_valid_line_number = True
        except NameError as err:
            print(err)
            continue
    editing_el = int(input("Выберете команду:\n1 - Изменить имя\n2 - Изменить фамилию\n3 - Изменить номер\n> "))
    for el in res:
        if line_number - 2 == res.index(el):
            if editing_el == 1:
                editing_first_name = get_first_name()
                print(f"Имя {el["Имя"]} изменена на {editing_first_name}")
                el.update({'Имя':editing_first_name}) 
            elif editing_el == 2:
                editing_last_name = get_last_name()
                print(f"Фамилия {el["Фамилия"]} изменена на {editing_last_name}")
                el.update({'Фамилия':editing_last_name})  
            elif editing_el == 3:
                editing_phone_number = get_phone_number()
                print(f"Телефон {el["Телефон"]} изменена на {editing_phone_number}")
                el.update({'Телефон':editing_phone_number})               
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'


def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            print(*read_file(file_name))
        elif command == 'd': #Удаление контакта по вводу порядкового номера строки в файле (вклячая заголовки)
            if not exists(file_name):
                print("Файл отсутствует.")
                continue
            del_contact_file(file_name)
        elif command == 'e': #Изменение имени, фамилии или телефона записи (по порядковому номеру строки в файле)
            if not exists(file_name):
                print("Файл отсутствует.")
                continue
            editing_contact_file(file_name)


main()
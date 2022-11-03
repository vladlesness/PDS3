from os import listdir


# Створити функцію last_lines() яка приймає шлях до файлу та кількість останніх рядків та виводить їх у консолі
def last_lines(path, line_number):
    with open(path) as file:
        lines = file.readlines()
    for i in range(1, line_number + 1):
        print(lines[-i], end='')


# Написати програму, яка створює новий файл і записує у нього усі числа від 0 до 100, що кратні 5
def write_numbers():
    lst = [str(i) + '\n' for i in range(101) if i % 5 == 0]
    with open('numbers.txt', 'w') as file:
        file.writelines(lst)


# Створити функцію, яка отримує шлях до файлу та повертає кількість рядків у ньому
def number_of_lines(path):
    with open(path) as file:
        lines = file.readlines()
    return len(lines)


# Створити функцію, яка приймає шлях до каталогу та повертає список з його вмістом
def list_directory(path):
    return listdir(path)


# write_numbers()
# print(number_of_lines('numbers.txt'))
# print(list_directory(r'D:\Python and Data Science\Studies Startup IT Academy\Lessons\Lesson tasks'))
# last_lines('numbers.txt', 5)
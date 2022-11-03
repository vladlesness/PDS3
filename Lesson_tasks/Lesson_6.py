# Написати рекурсивну функцію, яка б вертала ряд Фібоначі у вигляді списку цифр.
# Функція повинна мати вхідний цифровий параметр максимального значення у списку.
# 1, 2, 3, 4, 5, 6, 7, 8,  9,  10
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fib(n, a=0, b=1, fib_list=[0]):
    if len(fib_list) < n:
        fib_list.append(b)
        a, b = b, a + b
    else:
        return fib_list
    return fib(n, a, b, fib_list)
# print(fib(7))


# Написати функцію, яка б вираховувала кількість від’ємних чисел у списку [ 20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4].
def negative_num_count(count_list):
    count_list = [i for i in count_list if i < 0]
    return len(count_list)
# print(negative_num_count([20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4]))


# Написати функцію визначення максимального елементу списку.
def max_list_num(lst):
    max_num = lst[0]
    for i in lst[1:]:
        if i > max_num:
            max_num = i
    return max_num
# print(max_list_num([20, -33, 16, 21, -5, -66, 74, 100, -3, 27, 87, -4]))


# Написати рекурсивну функцію, яка вертає суму чисел, що є елементами списку.
def list_elements_sum(lst, total=0):
    if lst:
        total += lst[0]
    else:
        return total
    return list_elements_sum(lst[1:], total)
#print(list_elements_sum([20, -33, 16, 21, -5, -66, 74, 100, -3, 27, 87, -4]))
# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.

# a = int(input("Введите первое число (A): "))
# b = int(input("Введите второе число (B): "))
#
# for i in range(a, b + 1):
#     print(i)


# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания,
# если A < B, или в порядке убывания в противном случае.

# a = int(input("Введите первое число (A): "))
# b = int(input("Введите второе число (B): "))
#
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# else:
#     for i in range(a, b - 1, -1):
#         print(i)

# Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания.
# В этой задаче можно обойтись без инструкции if.

# a = int(input("Введите первое число (A): "))
# b = int(input("Введите второе число (B): "))
#
# for i in range(a, b - 1, -2):
#     print(i)

# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна вывести номер потерянной карточки.
# Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.


# n = int(input("Введите общее количество карт: "))
# summa_card = n * (n + 1) // 2
# sum_remain = 0
#
# for i in range(n - 1):
#     x = int(input("Введите номер оставшейся карты: "))
#     sum_of_remaining_cards += x
#
# lost_card = sum_of_cards - sum_of_remaining_cards
# print("Потерянная карта это:", lost_card)

# Вводится строка, включающая строчные и прописные буквы.
# Требуется вывести ту же строку в одном регистре, который зависит от того, каких букв больше.
# При равном количестве преобразовать в нижний регистр.
# Например, вводится строка "HeLLo World", она должна быть преобразована в "hello world",
# потому что в исходной строке малых букв больше. В коде используйте цикл for, строковые методы upper()
# (преобразование к верхнему регистру) и lower() (преобразование к нижнему регистру),
# а также методы isupper() и islower(), проверяющие регистр строки или символа.

# string = input("Enter a string: ")
#
# upper_count = 0
# lower_count = 0
#
# for char in string:
#     if char.islower():
#         lower_count += 1
#     elif char.isupper():
#         upper_count += 1
#
# if lower_count >= upper_count:
#     print(string.lower())
# else:
#     print(string.upper())


while True:
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")

    if num1.isdigit() and num2.isdigit():
        result = int(num1) + int(num2)
        print("Сумма цифр: ", result)
        break
    else:
        print("Ошибка! Пожалуйста, введите число.")



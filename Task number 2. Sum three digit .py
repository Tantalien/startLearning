'''Нужно написать программу, которая суммирует цифры в случайном трехзначном числе.
Случайное трехзначное число программа генерирует сама'''

from random import randint
a = randint(100, 999)

print('Рандомное число:', a)

sum = 0                    # объявляем переменную
for digit in str(a):       # преобразуем число 'а' в строку
    sum += int(digit)      # преобразуем обратно в число и прибавляем к sum
 # только не ясно, как программа понимает, что нужно суммировать эти отдельные цифры

print("Сумма цифр числа", a, "равна:", sum)



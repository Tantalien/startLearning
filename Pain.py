'''Напишите функцию sum_range(start, end), которая суммирует все целые числа
от значения start до величины end включительно.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами'''
import math


def sum_range(start, end):
  if start < end:
    a = sum(range(start, end + 1))

  elif start > end:
    a = sum(range(end, start + 1))

  else:
    print('Задайте диапазон чисел')

  return a


start = int(input("Введите первое число: "))
end = int(input("Введите второе число: "))

print(sum_range(start, end))

# пиши сразу нормальный комментарий

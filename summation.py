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


start_str = input("Введите первое число: ")
end_str = input("Введите второе число: ")

try:
  end = int(end_str)
  start = int(start_str)
  print(sum_range(start, end))
except (SystemError, ValueError):
  print('Вы ввели некорректное число')



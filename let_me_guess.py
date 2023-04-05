import random

number = random.randint(1, 100)

try:
    while True:
        guess = int(input('Угадай число (от 1 до 100):'))

        a = 5             # variable very hot
        b = 10            # variable hot
        c = 20            # variable cold
        i = 2             # fire

        if number == guess:
            print('Угадал! Ты умничка')
            break
        else:
            if number - i < guess < number + i:
                print('Огонь!')
            elif number - a < guess < number + a:
                print('Очень горячо')
            elif number - b < guess < number + b:
                print('Горячо, но не сильно')
            elif number - c < guess < number + c:
                print('Холодно')
            elif guess > 100 or guess < 1:
                print('Диапазон загаданного числа от 1 до 100')
            else:
                print('Лёд!')

except ValueError:
    print('Введите корректное значение (не дробное число/не буквы/не символы)')

#опробовать окошко. сделать кнопки рабочими
#сделать так, чтоб после ошибки не приходилось перезапускать программу



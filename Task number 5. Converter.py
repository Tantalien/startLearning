#Перевести Цельсии в Фаренгейты или наоборот

c = int(input('Градусы Цельсия (C):'))
f = 1.8 * c + 32
k = c + 273
print('Градусы Фаренгейта:', format('%.2f' % f), 'F')
print('Градусы Кельвина:', format('%.2f' % k), 'K')

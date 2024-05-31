# os - библиотека для работы с консолью
# random - библиотека для работы со случайными данными
import os
import random

# Устанавим цвет шрифта - голубой
os.system('COLOR B')

LEFT = 0  # LEFT - левая граница
RIGHT = 100  # RIGHT - правая граница

first = random.randint(LEFT, RIGHT)  # first - первое число
second = random.randint(LEFT, RIGHT)  # second - второе число

print('\nЗНАЧЕНИЯ ЧИСЕЛ:')
print('Первое число: ', first, '.', sep='')
print('Второе число: ', second, '.\n', sep='')

# Вычисление суммы
# Сложим числа при помощи оператора +

summa = first + second  # summa - значение суммы

print('ВЫЧИСЛЕНИЕ СУММЫ')
print('Сумма: ', summa, '.\n', sep='')

# Вычисление разности
print('ВЫЧИСЛЕНИЕ РАЗНОСТИ')

# 1-й способ
# Вычтем из first second
diff = first - second
print('1-й способ:')
print('Разность: ', diff, '.\n', sep='')

# 2-й способ
# Вычтем из second first
diff = second - first
print('2-й способ:')
print('Разность: ', diff, '.\n', sep='')

# 3-й способ
# Вычтем из first second или
# из second first и возьмём модуль
diff = abs(diff)
print('3-й способ:')
print('Разность: ', diff, '.\n', sep='')

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли


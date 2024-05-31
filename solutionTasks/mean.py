# os - библиотека для работы с консолью
# math - библиотека для работы с математическими функциями
# numpy - библиотека для работы с матрицами
# statistics - библиотека для работы со статистическими данными
# random - библиотека для работы со случайными данными

import os
import math
import numpy
import statistics
import random

# Устанавим цвет шрифта - голубой
os.system('COLOR B')

MULTIPLIIER = 100  # MULTIPLIER - Множитель

first = random.random() * MULTIPLIIER  # first - первое число
second = random.random() * MULTIPLIIER  # second - второе число
third = random.random() * MULTIPLIIER  # third - третье число

# Выведем числа
print('\nЧИСЛА:')
print('Первое число: ', first, '.', sep='')
print('Второе число: ', second, '.', sep='')
print('Третье число: ', third, '.', sep='')

# Найдём среднее арифметическое
print('\nПОИСК СРЕДНЕГО\n')

# 1-й способ:
# Сложим числа и разделим сумму на их количество
mean = (first + second + third) / 3
print('1-й способ:')
print('Среднее: ', mean, '.\n', sep='')

# Создадим список чисел numbers
numbers = [first, second, third]

# Определим количество чисел при помощи функции len
counter = len(numbers)

# Определим сумму чисел при помощи функции sum
summary = sum(numbers)

# 2-й способ:
# Воспользуемся функциями fsum модуля math и len
summary = math.fsum(numbers)
mean = math.fsum(numbers) / counter
print('2-й способ:')
print('Среднее: ', mean, '.\n', sep='')

# 3-й способ:
# Воспользуемся функциями sum и len
mean = summary / counter
print('3-й способ:')
print('Среднее: ', mean, '.\n', sep='')

# 4-й способ:
# Воспользуемся функцией mean модуля numpy
mean = numpy.mean(numbers)
print('4-й способ:')
print('Среднее: ', mean, '.\n', sep='')

# 5-й способ:
# Воспользуемся функцией mean модуля statistics
mean = statistics.mean(numbers)
print('5-й способ:')
print('Среднее: ', mean, '.\n', sep='')

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли


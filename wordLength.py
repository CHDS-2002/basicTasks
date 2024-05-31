# os - библиотека для работы с консолью
# random - библиотека для работы со случайными данными

import os
import random

os.system('COLOR B')  # Устанавливаем цвет шрифта - голубой

LEFT0 = 65  # LEFT0 - левая граница
RIGHT0 = 90  # RIGHT0 - правая граница
LEFT1 = 97  # LEFT1 - левая граница
RIGHT1 = 122  # RIGHT1 - правая граница
LEFT2 = 1040  # LEFT2 - левая граница
RIGHT2 = 1103  # RIGHT2 - правая граница

RANDOM = random.randint(LEFT0, RIGHT0)
# RANDOM - случайное целое число
RANGE = RANDOM - LEFT0
# RANGE - диапозон значений

literals = random.choice([
    [chr(random.choice([random.randint(LEFT0, RIGHT0), random.randint(LEFT1, RIGHT1)])) for _ in range(RANGE)],
    [chr(random.randint(LEFT2, RIGHT2)) for _ in range(RANGE)]
])
# literals - сгенерированный список случайных символов
a = ''.join(literals)  # a - сгенерированная случайная строка

print('\nСтрока: ', a, '.\n', sep='')
# length_a - длина строки

# 1-й способ
# Определим длину строки по значению константы RANGE
length_a = RANGE
print('1-й способ:')
print('Длина строки: ', length_a, '.\n', sep='')

# 2-й способ
# Определим длину строки по длине списка literals при
# помощи функции len
length_a = len(literals)
print('2-й способ:')
print('Длина строки: ', length_a, '.\n', sep='')

# 3-й способ
# Определим длину строки по длине самой строки a при
# помощи функции len
length_a = len(a)
print('3-й способ:')
print('Длина строки: ', length_a, '.\n', sep='')

os.system('PAUSE')  # Останавливаем работу программы
os.system('CLS')  # Очищаем экран консоли

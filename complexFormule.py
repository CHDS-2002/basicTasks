# os - библиотека для работы с консолью
# random - библиотека для работы со случайными данными
import os
import random

# Устанавим цвет шрифта - голубой
os.system('COLOR B')

MULTIPLIER = 100  # MULTIPLIER - множитель

a = random.random() * MULTIPLIER  # a - первое число
b = random.random() * MULTIPLIER  # a - второе число
c = random.random() * MULTIPLIER  # a - третье число

# Выведем числа
print('\nЧИСЛА:\n')
print('Число a: ', a, '.', sep='')
print('Число b: ', b, '.', sep='')
print('Число c: ', c, '.', sep='')

# Найдём значение f тремя способами
# f - числовое значение

# 1-й способ
f = (a * b) + (a * c)
print('\nf: ', f, '.', sep='')

# 2-й способ
f = a * b + a * c
print('f: ', f, '.', sep='')

# 3-й способ
f = a * (b + c)
print('f: ', f, '.\n', sep='')

# Возведём полученное число в третью степень
# тремя способами
# t - числовое значение:

# 1-й способ
# Воспользуемся функцией pow
t = pow(f, 3)
print('t: ', t, '.', sep='')

# 2-й способ
# Воспользуемся оператором **
t = f ** 3
print('t: ', t, '.', sep='')

# 3-й способ
# Воспользуемся оператором *
t = f * f * f
print('t: ', t, '.', sep='')

# 4-й способ
# Воспользуемся циклом for и оператором *
t = 1
POWER = 3  # POWER - степень

for _ in range(POWER):
    t *= f

print('t: ', t, '.', sep='')

# 5-й способ
# Воспользуемся циклом while и оператором *
t = 1
i = 0

while i < POWER:
    t *= f
    i += 1

print('t: ', t, '.', sep='')

# Разделим полученное число на два
number = t / 2  # конечное число

print('\nРезультат: ', number, '.\n', sep='')

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли

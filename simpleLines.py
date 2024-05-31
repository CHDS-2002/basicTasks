# os - библиотека для работы с консолью
import os

# Устанавливаем цвет шрифта - голубой
os.system('COLOR B')

first_string = "Вторник"  # first_string - первая строка
second_string = "Понедельник"  # second_string - вторая строка

print('\nСТРОКИ')

# Выведем строки отдельно
print('Первая строка: ', first_string, '.', sep='')
print('Вторая строка: ', second_string, '.\n', sep='')

# Выведим строки в одну строку через запятую

# 1-й способ
# Выведем сначала second_string, потом first_string
print('1-й способ:')
print("Строка:")
print(second_string, ', ', first_string, '\n', sep='')

# 2-й способ
# Выполним обмен значениями
# переменных first_string и second_string

first_string, second_string = second_string, first_string

print('2-й способ:')
print("Строка:")
print(first_string, ', ', second_string, '\n', sep='')

os.system('PAUSE')  # Останавливаем работу программы
os.system('CLS')  # Очищаем экран консоли

# Импортирование функций из другого файла.

# Позволяет разбивать программу на несколько файлов, чтобы не загромождать один файл большим количеством кода

import recusion # импортирует функции, имеющиеся в файле tuples
import recusion as re # привязка импортируемого файла к сокращению, где tu - сокращенное название.

print(recusion.f())  # Вызов конкретной функции из файла tuples
dir(recusion)        # Чтобы посмотреть все функции импортируемом файле
print(re.f())      # Вызов функции с использованием сокращенного названия файла

# Параметры функции по умолчаниюю

def new_string(symbol, count):
    return symbol*count

print(new_string('!',5)) # задаем оба параметра из строки
print(new_string('!'))   # если второй параметр не задана - выдаст ошибку

def new_string(symbol, count=5): # параметр count задан по умолчанию и программа будет выполняться даже если его не указывать при вводе 
    return symbol*count

# Параметров по умолчанию может быть несколько, но все они должны быть запианы в конце перечня параметров

def MultiPar(*params):
    res: str=''             # Явное указание типа данных "строка" через двоеточие (для чисел res: int=0). !!Не обязательное!!
    for item in params:
        res+=item           # "Склеивание" строчных элементов. Для цифер - сложение
    return res

print(MultiPar('1','2','3','4'))
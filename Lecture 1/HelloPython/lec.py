from turtle import clear


print ('Привет, Питон!')

# типы данных и переменная
# int float boolean str list None

value = None
a = 123
b = 1.23
print(type(value))
print(type(a))
print(type(b))
value = 12334
print(type(value))
s = 'hello world'
print(s) # Вывод строки
print(a, '-',b, '-',s)
print('{} - {} - {}'.format(a,b,s))
print(f'{a} - {b} - {s}')
print('{1} - {2} - {0}'.format(a,b,s))

f = True
print(f)

# списки (массивы)

list = [1,2,3]
print(list)

list2 = ['1', '2', 'hello', 1,2,3,True] # можно, но не нужно. Данные одного типа в списке
print(list2)

# Ввод и вывод данных
# print, input

print('Введите число a');
a = int(input())                 # строковое значение. Для целых чисел - int(input()), Для вещественных - float(input())
print('Введите число b');
b = int(input())
print(a,b)
print(a,'+',b,'=',a+b)
print('{} {}'.format(a,b))
print(f'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **     // - деление в целых числах % - остаток от делегия, ** - возведение  степень
# **,  ,  , *, /, //, %, +, -
# (), Сокращенные опперации

c= 123
d=321
e = c+d
print(e)

# Особенность хранения вещесвенных чисел - в результате много знаков после запятой. Ограничивать количество занок - round(f*g,5)
f= 1.3
g=3
h = f*g
print(h)

temp = 3
temp *= 5
print(temp)

# Логические выражения
# <, >, <=, >= ==, !=
# not, and, or (не путать с &, |, ^)
# is, is not , in, not in - выражения Python
# gen

a = 1 < 3 < 5 # тройные и четверые неравенства
print (a)

f = 1>2 or 4<6
print (f)
g = [1,2,3,4]
print(not 2 in g)

is_Odd = g[0] %2 ==0 # или not g[0] % 2 - тоже самое
print(is_Odd)

# Управояющик конструкции
#  if, if-else
a = int(input('a = '))
b = int(input('b = '))
if a >b:
    print(a)
else:
    print(b)

username = input('Введите имя пользоватля: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Марина, я вас так ждал!')
elif username == 'Саша':
    print('Саща - ТОП 1')
else:
    print('Привет, ', username)

# Управляющие конструкции
# while
# for

original = 233
reverted = 0

while original !=0:
    reverted = reverted*10 + (original%10)
    original //=10  # // - деление в целых числах

print(reverted)

original = 2334
reverted = 0

while original !=0:
    reverted = reverted*10 + (original%10)
    original //=10  # // - деление в целых числах
else:
    print('Пожалуй...')
    print('на этом всё.')

print(reverted)

# for i in 1,2,3,4,5:
#    print(i**2)

list = [1,2,3,4,5]
for i in list:
    print(i**2)

r = range(1,10,2) # способы задать отрезок: range(10) - от 0 до 9, range(1,5) - от 0 до 5,
# range(1,10,2) - от 0 до 9 с удоенным промежутокм

for i in r:
    print(i)


# Работа со строками

text = 'съешь еще этих мягких французских булок'

print(len(text))        # длина текстовой строки
print('еще' in text)    # наличие в строке элемента
print(text.isdigit())   # проверка на цифовую сроку
print(text.islower())   # проверка на строчность
print(text.replace('еще', 'ЕЩЕ')) #замена элемента

# подсказки help(text.islower)

print(text[0])      # выдает соответсвующий элемент строки
print(text[len(text)-1])    # выдаст последний элемент строки (длина строки -1)
print(text[-5])     # выдает 5-й элемент с конца
print(text[:])      # тоже что print(text)
print(text[:2])     # первые два элемента текста в заданном диапазоне
print(text[len(text)-2:])   # последние два элемента взаданном диапазоне
print(text[2:9])    # диапазон от 2 до 9 символа
print(text[6:-18])  # вариат задачи граници диапазона от конца строки
print(text[0:len(text):6])  # от первого элемента до последнего с шагом 6 символов
print(text[::6])     # аналогичн предыдущему без задания конкретного дипазона
text = text[2:9] + text[-5] + text[:2]  # сборка строки из элементов текста: 
                                        # 1. От второго до девятого, 2. пятый с конца, 3. от начала до второго

# Списки

numbers = [1,2,3,4,5]
print(numbers)

ran = range(1,6)            # range и list - разные типы
numbers = list(ran)

numbers[0] = 10 # задача значения списка на прямую

for i in numbers:       #  меняется именно i, а не элемент списка
    i *=2
    print(i)
print(numbers)

colors = ['red', 'green', 'blue']

for e in colors:            # выдает все элементы списка, где есть e
    print(e)

for e in colors:            # выдает все элементы списка, где есть e дважды
    print(e*2)

colors.append('gray')   # добавляет элемент в конец списка
print(colors== ['red', 'green', 'blue', 'grey']) #проверка на наличие всех перечисленных элементов в списке
colors.remove('red') # или del colors[0] - удаляет первый элемент списка

# Функции

def f(x):
    if x ==1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg =1
print(f(arg))
print(type(f(arg)))     # демонстрация типа

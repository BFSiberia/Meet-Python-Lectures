# Кортежи - неизменяемые (в отличие от списков) наборы данных. 
# Можно использовать в качестве ключей словаря. 
# Занимает меньше места, чем список
# Можно проводить все операции со списками, которые не менют список (т.е. кроме +, * на число, методы index() и count() и проч)

# a = tuple()     # Создали пустой кортеж
# b = ()      # Альтернативное создание пустого кортежа
# с = ('s',)  # кортеж из 1 элемента. ""Запятая обязательна!!
# d = 's',    # алетрнативный метод
# e = tuple('Hello, World!') # Каждая буква в строке - элемент кортежа (!!для цифр не работает!!)
# print(e)

# # Можно трансформировать список в кортеж
# colors = ['green', 'blue', 'yellow']
# print(colors)
# t = tuple(colors)
# print(t)

# # Обращение к конкретному элементу кортежа
# print(t[0])
# # Поэлементный вывод на экран кортежа
# for e in t:
#     print(e)

# Распаковка кортежа в переменные
t = tuple(['first','second','third']) # список сконвертированный в кортеж
print(t)
first, second, third = t # создали новые переменные на основе данных кортежа
print('f:{}, S:{}, t:{}'.format(first, second, third))
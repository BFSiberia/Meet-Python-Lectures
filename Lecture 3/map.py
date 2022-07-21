# Функция map - применяет указанную функцию к каждому элементу итерируемого объекта и возвращает
# список c новыи объектами

# li = [x for x in range(1,20)]

# li = list(map(lambda x:x+10, li)) # применяет анонисную функцию x+10 к каждому члену li

# print(li)

# data = list(map(int,input('Введите 5 чисел через пробел: ').split())) # Набор чисел с пробелами. 
# # В аргуменет сплит можно указать разделитель (','). map возрвращает результат функции инт
# print(data)

# Важно! Результат работы map - это итератор - его результаты нужно сохранять

def map(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

with open ('sample.txt', 'r') as f:
    data = f.read().split()
    res = map(int, data) # тоже, но с использованием map
    res= where(lambda x: not x%2, res) # выборка четных чисел
    res = list(map(lambda x: (x, x**2), res)) # состаление кортежей из число + квадрат числа
    print(res)

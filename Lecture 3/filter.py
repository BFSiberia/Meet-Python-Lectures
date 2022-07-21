# Функиця filtr - применяет указанную функицю к каждому элемету итерируемого объекта
#  и возвращает итератор с теми объектами, для которых функция вернула True

# f(x) => чётное
# filter(f, [1,2,3,4,5]) => [2,4]
# Толко 1 проход!!!


# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2,data)) # x%2==0 эквивалент not x%2
# print(res)

def map(f, col):
    return [f(x) for x in col]

# def select(f, col):                   # замена filter
#     return [x for x in col if f(x)]

with open ('sample.txt', 'r') as f:
    data = f.read().split()
    res = map(int, data) # int - функция, преобразующая строки в числа на основе данных data
    res= filter(lambda x: not x%2, res) # выборка четных чисел, x%2==0 эквивалент not x%2
    res = list(map(lambda x: (x, x**2), res)) # состаление кортежей из число + квадрат числа
    print(res)

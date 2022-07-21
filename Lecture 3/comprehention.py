# list=[i for i in range(1,21) if i%2==0]
# print (list)

# with open ('sample.txt', 'r') as f:
#     list_tmp = [int(i) for i in f]
#     print(list_tmp)
#     list_result = [(i, i**2) for i in list_tmp if i%2==0]

# print(list_result)


def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

with open ('sample.txt', 'r') as f:
    data = f.read().split()
    res = select(int, data) # int - функция, преобразующая строки в числа на основе данных data
    res= where(lambda x: not x%2, res) # выборка четных чисел
    res = select(lambda x: (x, x**2), res) # состаление кортежей из число + квадрат числа
    print(res)

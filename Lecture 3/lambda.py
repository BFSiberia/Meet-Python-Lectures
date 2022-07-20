# Лямбда функции

def f(x):
    return x**2
g=f                 # функции можно присвоить имя переменной и вызывать ее через переменную
print(g(10))

def math (op, x):   # передаем в качестве аргументов функцию f и перменную x
    print(op(x))    # (которая тоже может быть функицей)

# math(f,10)

def sum(x,y):
    return x+y

def mult(x,y):
    return x*y

def calc(op,a,b):
    return op(a,b)

# print(calc(mult,5,9))

fsum = lambda q, w: q+w

print(calc(lambda q, w: q+w+1, 4, 5)) # лямбда функиця используется для "разовых" функций
                                      # которые нет необходимости тянуть через весь код
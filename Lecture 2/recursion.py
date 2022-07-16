# Факториал с выводом а экран
def Factorial (number):
    if number in [1]:
        return 1
    else:
        return number*Factorial(number-1)

list_fact =[]

for i in range(1,10):
    list_fact.append(Factorial(i))
print(list_fact)


# Фибоначчи с выводом на экран
def Fibo(number):
    if number in [1,2]:
        return 1
    else:
        return Fibo(number-1)+Fibo(number-2)

list_fibo =[]

for i in range(1,10):
    list_fibo.append(Fibo(i))
print(list_fibo)
def Fuctorial (number):
    if number in [1]:
        return 1
    else:
        return number*Fuctorial(number-1)

list_fact =[]

for i in range(1,10):
    list_fact.append(Fuctorial(i))
print(list_fact)

def Fibo(number):
    if number in [1,2]:
        return 1
    else:
        return Fibo(number-1)+Fibo(number-2)

list_fibo =[]

for i in range(1,10):
    list_fibo.append(Fibo(i))
print(list_fibo)
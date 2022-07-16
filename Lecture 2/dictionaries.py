# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу

from turtle import left


dictionry = {} # создали пустой словарь
dictionry = \
    {
        'up':'u',
        'down':'d',
        'left':'l',
        'right':'r'
    }
# Симвод "\" указывает на продолжение строки (перенос кода ниже)

print(dictionry)
print(dictionry['right']) # Вывод на экран элемента словаря
for e in dictionry.keys(): # keys - ключи, values - значения
    print(e)

for v in dictionry: # по элементам
    print(dictionry[v])  # вывод значений словаря, просто v - только ключей

for item in dictionry:          # Вывод пар "ключ: значение"
    print('{}: {}'.format(item,dictionry[item]))

exit()
dictionry['up'] ='up' # изменение элемента словаря по ключу
del dictionry[left] #удаление элемента словаря

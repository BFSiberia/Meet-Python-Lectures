# Множества. Обозначаются фигурными скобками {}

colors = {'red', 'green', 'blue'}

print(colors)

colors.add('black') # Добавление элемента множества

print(colors)

colors.remove('red') # Удаление элемента множества. Выдает ошибку, если элемента нет во множестве
print(colors)

colors.discard('red') # Удаление элемента множества. Не выдетошибку, если элемента нет во множестве
colors.clear # очистка множества

# Операции со множествами

a = {1,2,3,4,5,8}
b = {2,5,8,13,21}
c = a.copy # копирование множества
u = a.union(b)  # полное объединение двух множеств
i = a.intersection(b)   #  Общие значения множеств
dl = a.difference(b) # различие a от b
dr = b.difference(a) # различие b от a

s = frozenset(a) # неизменяемое множесnво

q = a \
    .union(b) \
    .difference(a.intersection(b))
# a.union(b).difference(a.intersection(b))  1,2,3,4,5,8,13,21 - различие от (2,5,8) = 1,3,4,13,21
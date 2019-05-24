"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint
source = []

for i in range(0, 30):
    source.append(randint(1, 20))

max = source[0]
min = source[0]
ind_max = 0
ind_min = 0
for i in range(1, len(source)):
    if source[i] > max:
        max = source[i]
        ind_max = i
    if source[i] < min:
        min = source[i]
        ind_min = i

result = 0
if ind_max > ind_min:
    for i in range(ind_min + 1, ind_max):
        result += source[i]
elif ind_min > ind_max:
    for i in range(ind_max + 1, ind_min):
        result += source[i]

print(source)
print(f'Минимальный элемент в позиции {ind_min}, максимальный - {ind_max}')
print(f'Сумма: {result}')
#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

source = []
[source.append(randint(1, 20)) for i in range(0, 30)]
print(source)

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

print(f'Минимальное значение {min} на номере {ind_min}')
print(f'Максимальное значение {max} на номере {ind_max}')
a = source[ind_max]
source[ind_max] = source[ind_min]
source[ind_min] = a
print(source)

"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import randint

source = []
[source.append(randint(1, 20)) for i in range(0, 10)]

if source[1] > source[0]:
    min_1 = source[0]
    min_2 = source[1]
else:
    min_2 = source[0]
    min_1 = source[1]

for i in range(2, len(source)):
    if source[i] < min_1:
        min_2 = min_1
        min_1 = source[i]
    else:
        if source[i] < min_2:
            min_2 = source[i]

print(source)
print(f'Минимальный элемент - {min_1}, следующий - {min_2}')

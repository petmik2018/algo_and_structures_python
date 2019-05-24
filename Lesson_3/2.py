"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

from random import randint

def add_if_even(source, target, num):
    if source[num] % 2 == 0:
        target.append(num)

source = []
target = []
[source.append(randint(1, 20)) for i in range(0, 30)]
print(source)

[add_if_even(source, target, i) for i in range(0, len(source))]
print(target)
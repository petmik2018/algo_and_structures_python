#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint

source = []
[source.append(randint(-20, 20)) for i in range(0, 30)]

max = source[0]
ind_max = 0
first_element_found = False

for i in range(1, len(source)):
    if not first_element_found and source[i] < 0: first_element_found = True
    if first_element_found and source[i] < 0 and source[i] > max:
        max = source[i]
        ind_max = i

print(source)
if ind_max == 0 and max >= 0:
    print('В массиве нет отрицательных элементов')
else:
    print(f'Максимальное отрицательное значение {max} на номере {ind_max}')

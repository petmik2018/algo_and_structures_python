# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

# инициализация матрицы
matr = [[randint(0, 9) for j in range(4)] for i in range(5)]
[[print(matr[i][j]) if j == 3 else print(matr[i][j], end=' ') for j in range(4)] for i in range(5)]

# задание начального значение максимального элемента как минимум по первому стролбцу
result = matr[0][0]
for i in range(5):
    if matr[i][0] < result: result = matr[i][0]

# перебор по оставшимся столбцам
for j in range(1, 4):
    min = matr[0][j]
    for i in range(1, 5):
        if matr[i][j] < min:
            min = matr[i][j]
    if min > result:
        result = min

print(f'Результат: {result}')
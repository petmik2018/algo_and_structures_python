"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
from random import randint

# инициализация матрицы
matr = [[0 if j == 3 else randint(0, 9) for j in range(4)] for i in range(5)]

# вычисление последнего элемента каждой строки
for i in range(5):
    sum = 0
    for j in range(3):
        sum += matr[i][j]
    matr[i][3] = sum

# вывод матрицы на печать
[[print(matr[i][j]) if j == 3 else print(matr[i][j], end=' ') for j in range(4)] for i in range(5)]
# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

def calculate(num):
    k = 0
    for i in range(2, 100):
        if i % num == 0:
            k += 1
    print(f'{k} чисел, кратных {num}')

denominators = range(2, 10)
print('В указанном диапазоне:')
[calculate(j) for j in denominators]

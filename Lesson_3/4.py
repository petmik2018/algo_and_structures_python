# 4.	Определить, какое число в массиве встречается чаще всего.

from random import randint
source = []

for i in range(0, 30):
    source.append(randint(1, 20))

source_set = list(set(source))

target = [0]*len(source_set)

for val in source:
    for i in range(0, len(source_set)):
        if val == source_set[i]: target[i] += 1

result = source_set[0]
num_max = target[0]
for i in range(1, len(target)):
    if target[i] > num_max:
        num_max = target[i]
        result = source_set[i]

print(source)
# print(set(source))
# print(target)
print(f'Число {result} встречается в массиве {num_max} раз')
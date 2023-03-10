# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

n = int(input("Введите количество элементов в массиве: "))
x = int(input("Введите X: "))

a = [random.randint(-10, 10) for _ in range(n)]
print(a)

min_diff = abs(x - a[0])
vv = a[0]

for i in range(1, n):
    diff = abs(x - a[i])
    if diff < min_diff:
        min_diff = diff
        vv = a[i]

print(f"Самый близкий элемент к {x} в Вашем массиве {a} равен {vv}")
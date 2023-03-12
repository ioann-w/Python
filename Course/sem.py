# Семинар 2

# Факториал с while

# n = int(input("Введите число: "))
# i = 1 # Счетчик
# res = 1 # Результат

# while i <= n:
#     res = res * i
#     i = i + 1

# print(f"{n}! =  {res}")



# Фибоначи

# a = int(input("Введите число: "))
# c, d = 0, 1 # Первые два числа последовательности Фибоначи
# n = 2 # Порядок с 2 (индекс начинается с 0, порядок с 1)

# while d < a:
#     c, d = d, c + d
#     n += 1

# if d == a:
#     print(n)
# else:
#     print(-1)



# Задача

# a = int(input("Введите количество дней: "))
# # b = input("Введите температуру для каждого дня через пробел: ").split() # .split() делит элементы через пробел и возвращает их в списке
# temp = 0
# max_ = 0

# for i in range(a):
#     t = int(input("Введите температуру: "))

#     if t > 0:
#         temp += 1
    
#     else:
#         max_ = temp
#         temp = 0
#         continue

# print(max_)



# Задача

# n = int(input("Введите количество арбузов: "))

# import math
# l, h = math.inf, -math.inf

# for i in range(n):
#     w = int(input(f"Вес арбуза #{i + 1}: "))
#     if w > h:
#         h = w
#     if w < l:
#         l = w

# print(f"Самый легкий: {l}, Самый тяжелый: {h}")



# Семинар 3

# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# a = [1, 1, 2, 0, -1, 3, 4, 4, 6, 6, -7, -12]
# b = set(a)
#print(len(b))



# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность на K элементов вправо,
# K - положительное число.

# a = [1, 2, 3, 4, 5, 6]
# b = [0] * len(a)
# k = 3 % len(a)

# for i in range(len(a)):
#     b[i] = a[i - k]

# print(a)
# print(b)



# import random

# N = 10

# lst = [random.randrange(10) for _ in range(N)]

# print(f'{lst = }') # Самодокументация

# k = int(input('k = '))

# for _ in range(k):
#     lst.insert(0, lst.pop())

# print(f'{lst = }')



# list_1 = [1, 2, 3, 4, 5]
# list_2 = list_1[-3:] + list_1[:-3]
#print(f'{list_1} ==> {list_2}')



# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит

# lst = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

# lst2 = []

# for dct in lst:
#     for key in dct:
#         lst2.append(dct[key])

# print(set(lst2))



# lst = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
# unique = set()

# for el in lst:
# for _, values in el.items():
#     unique.add(values)

# print(lst)
# print(unique)



# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# lst = []
# length = int(input('Введите длину списка: '))

# for i in range(length):
#     n = int(input(f'Введите элемент {i + 1}: '))
#     lst.append(n)

# print(*lst)

# count = 0
# for i in range(1, len(lst)):
#     if lst[i] > lst[i - 1]:
#         count += 1

# print(count)



# Семинар 4


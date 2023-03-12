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


# Задача:

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()


# Вариант 1:

# a = input('Введите слово: ').split()
# b = []

# for i in range(len(a)):
#     if a[i] in b:
#         b.append(a[i] + '_' + str(a[:i].count(a[i])))
#     else:
#         b.append(a[i])

# print(*b)


# Вариант 2:

# st = 'a a a b c a a d c d d'
# lt = st.split()

# dct = {}
# output = ''

# for i in lt:
#     if i in dct:
#         dct[i] += 1
#         output += f'{i}_{dct[i]} '
#     else:
#         dct[i] = 0
#         output += f'{i} '

# print(f"Наш словарь: {dct}")
# print(f'Решение: {output}')



# Задача: 

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13


# Вариант 1: 

# other_text = 'Other text'
# other_text = set(other_text.upper().split())

# print(other_text)
# print(len(other_text))


# Вариант 2: 

# inpt1 = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure so if she, sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# inpt2 = ''

# for char in inpt1:
#     if char == ' ' or char.isalpha():
#         inpt2 += char

# dct = {}

# for word in inpt2.upper().split():
#     dct[word] = ''

# print(len(dct))


# Задача:

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. Однако 2 друга оказались не такими смышлеными. 
# Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.


# Вариант 1: 

# import random
# n= 20

# a = [random.randint(1, 10) for _ in range(n)]
# print(a)
# b = []

# idx = random.randrange(len(a))

# a.insert(idx, 0)

# for i in range(len(a)):
#     if a[i] != 0:
#         b.append(a[i])
#     else:
#         break

# print(b)
# print(max(b))


# Вариант 2: 

# import random
# lst = []

# while (i := random.randrange(11) != 0)
#     lst.append(i)
# lst.append(i)

# print(lst)
# print(max(lst))


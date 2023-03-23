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



# Семинар 5:

# Задача: 

# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13

# Задание необходимо решать через рекурсию


# def fibo(n):

#     if n in [0, 1]:
#         return n
#     return fibo(n-1)+fibo(n-2)

# print(fibo(int(input())))



# fib = lambda N: N if N in (0, 1) else fib(N - 1) + fib(N - 2) # Анонимная функция, выполняется там же где объявляется
# print(fib(7))



# Задача: 

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные. 
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1


# import random

# n = int(input())

# grades = [random.randint(1, 5)for _ in range(n)]

# print(grades)

# minimum, maximum = sorted(grades)[::n-1]

# for i, value in enumerate(grades): # enumerate возвращает кортеж из двух элементов (индекс, элемент в списке(берется как аргумент)
#     if value == maximum:
#         grades[i] = minimum

# print(*grades)



# Задача: 

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым. Напоминание: Простое число - это число, 
# которое имеет 2 делителя: 1 и n(само число) Input: 5 Output: yes


# n = int(input('Введите число: '))

# res = True

# for i in range(2, int(n ** 0.5) + 1):
#     if n % i == 0:
#         res = False

# print(res)



# Задача: 

# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода). Input: 2 -> 3 4 Output: 4 3

# Вариант 1: 

# n = int(input())

# def rev(n):
#     if n == 0:
#         return
#     else:
#         x = int(input())
#         rev(n-1)
#         print(x, end = ' ')

# rev(n)

# Вариант 2: 

# def foo(n):
#     if n == 1:
#         return input()
#     n -= 1
#     temp = foo(n)
#     return input() + ' ' + temp

# print(foo(int(input())))

# Вариант 3: 

# from random import randrange

# def func(n):
#     if n == 0:
#         return '->'
    
#     print(var := randrange(n), end = ' ')
#     return f'{func(n-1)} {var}'

# print(func(5))



# Семинар 6:

# Задача: 

# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)



# n = int(input("введите разммерность 1 массива: "))

# mass1 = []
# mass2 = []

# for i in range(n):
#     mass1.append(int(input(f"элемент {i + 1}: ")))

# m = int(input("введите разммерность 2 массива: "))

# for i in range(m):
#     mass2.append(int(input(f"элемент {i + 1}: ")))


# for i in mass1:
#     if i not in mass2:
#         print(i, end = " ")



# Задача: 

# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве.
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1

# Вывод: Вывод:
# 0 2

# (каждое число вводится с новой строки)


# Вариант 1: 

# # import random as ran

# # n = int(input('Введите длину массива: '))
# # rand_lst = [ran.randint(1, 10) for _ in range(n)]
# # print(rand_lst)

# rand_lst = []
# n = int(input('Введите длину списка: '))

# for i in range(n):
#     rand_lst.append(int(input(f'Введите элемент {i + 1}: ')))

# count = 0

# for k, v in enumerate(rand_lst):
#     if 0 < k < len(rand_lst) - 1:
#     # if k == 0 or k == len(rand_lst) - 1:
#     #     continue
#         if rand_lst[k + 1] < v > rand_lst[k - 1]:
#             count += 1

# print(rand_lst)
# print(count)


# Вариант 2: 

# from random import randrange

# lst = [randrange(0, 10) for _ in range(int(input('Введите размер массива: ')))]

# count_nums = 0

# for i in range(2, len(lst)):
#     if lst[i] < lst[i - 1] > lst[i - 2]:
#         count_nums += 1

# print(lst, '-->', count_nums)


# Вариант 3: 

# n = int(input("введите разммерность 1 массива: "))
# lst = []

# for i in range(n):
#     lst.append(int(input(f"элемент {i + 1}: ")))

# print(lst)

# c = 0

# for i in range(len(lst[1:-1])):
#     if lst[i] < lst[i+1] > lst[i+2]:
#         c += 1

# print(c)



# Задача: 

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод: Вывод:
# 1 2 3 2 3 2


# Вариант 1: 

# lst = []
# n = int(input('Введите длину списка: '))
# for i in range(n):
#     lst.append(int(input(f'Введите элемент {i + 1}: ')))
# print(*lst)

# count = 0

# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if lst[i] == lst[j]:
#             count += 1
# print(count)


# Вариант 2: 

# def func(lst: list) -> int:
#     el, *lst = lst # el = lst[0], lst = [1:]
#     if lst:
#         return func(lst) + lst.count(lst)
#     return 0

# print(func(5, 5, 5, 5, 5))



# Задача: 

# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1,
# но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k
# выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно
# натуральное число k, не превосходящее 10^5. Программа должна вывести все пары дружественных чисел,
# каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод: Вывод:
# 300 220 284

# Вариант 1: 

# k = int(input('Введите число: '))

# s1, s2 = 0, 0

# for i in range (1, k):
#     s1 = 0
#     for s in range(1, i // 2 + 1):
#         if i % s == 0:
#             s1 += s
#         if i == s1:
#             continue
#         s2 = 0
#         for j in range(1, s1 // 2 + 1):
#             if s1 % j == 0:
#                 s2 += j
#         if s2 == i and i < s1:
#             print(i, s1)



# Семинар 7: 

# Задача:

# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз 
# и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
# print(‘ok’)
# else:
# print(‘fail’)

# Вывод:
# ok


# values = [1, 23, 42, 'asdfg']

# trasformation = lambda x: x
          
# transformed_values = list(map(trasformation, values))

# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')



# Задача:

# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, 
# по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены 
# на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле 
# S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. 
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, 
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))



# Вариант 1: 

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(list_of_orbits):
#     tmplst = [0, 0]
#     s = 0
#     for i in list_of_orbits:
#         a, b = i
#         if a != b:
#             tmp = a * b
#             if tmp > s:
#                 s = tmp
#                 tmplst[0], tmplst[1] = a, b
#     return tmplst

# print(*find_farthest_orbit(orbits))



# Вариант 2: 

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(list_of_orbits):
#     return max(list_of_orbits, key = lambda i: (i[0] != i[1]) * i[0] * i[1])

# print(*find_farthest_orbit(orbits))



# Вариант 3: 

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(lst):
#     max = 0
#     max_i = 0
#     new_lst = enumerate(lst)
#     for i, (k, v) in new_lst:
#         if k != v:
#             if k * v > max:
#                 max = k * v
#                 max_i = i
#     return lst[max_i]

# print(*find_farthest_orbit(orbits))


# Задача: 

# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, 
# функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')



# Вариант 1: 


# def same_by(func, values):
#     for i in range(1, len(values)):
#         if func(values[i]) != func(values[i - 1]):
#             return False
#     return True

# values = [1, 3, 6, 7]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')



# Семинар 8: 

# Задача на весь семинар по справочнику, продолжение задачи в hw8



# Семинар 9: 


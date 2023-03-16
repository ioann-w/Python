# Лекция 1

# n = 'hi"!"'

# print(n)
# print(type(n))


# Два способа поставить коммент, 
# 1й - тройной апостроф в начале и вконце
# 2й - выделенный текст ctrl + K -> ctrl + C; (ctrl + K -> ctrl + U) - раскомментировать

# print("this is comment") 



# Интерполяция - 3 способа вывода простых "строк" в одну сложную строку

# Пример простых строк:
# a = 0
# b = 6.9
# c = 'hi'

# Пример вывода:
# print(a, b, c)
# print(f'{a} - {b} - {c}')
# print('{} - {} - {}'.format(a,b,c))



# print('Введите значение: ') # Значение будет вводиться с новой строки
# a = input()

# a = input('Введите значение: ') # Значение будет вводиться справа от текста

# print(a)


# c = 0.69
# print(type(c))
# print(c)

# c = str(c)
# print(type(c))
# print(c)



# a = 1.696969
# b = 1.609609

# print(round(a*b, 3)) # round на вход берет два аргумента, 1 число, 2 сколько оставить знаков после запятой



# Лекция 2

# list_1 = [] # Примеры создания списка
# list_1 = list()
# list_1 = [1, 2, 3, 4]

# print(*list_1) # * Убирает все скобки, запятые и прочее

# for i in list_1:  # Цикл по списку
#     print(i)

# print(len(list_1)) # Количество элементов в списке

# print(list_1[0]) # Обращение к элементу списка по индексу

# list_1 = [1, 5]

# print(list_1)

# list_1.append(8) # append позволяет добавить элемент в конец списка

# print(list_1)

# list_1 = []
# print(list_1)

# for i in range(5): # На каждую итерацию цикла, добавляем i в конец списка
#     list_1.append(i)
#     print(list_1)

# list_1 = [1, 2, 3, 4, 5]

# print(list_1.pop()) # pop убирает элемент с конца списка #5 (можно указать индекс удаляемого элемента .pop(0) - удаляет первый элемент)
# print(list_1) # [1, 2, 3, 4]
# print(list_1.pop()) #4
# print(list_1) #[1, 2, 3]

# list_1 = [1, 2, 3, 4, 5]

# print(list_1.insert(2, 69)) # .insert(0, 0) - добавляет элемент на нужную позицию в списке, первый аргумент позиция, второй добавляемый элемент
# print(list_1)



#  Кортеж - неизменяемый список

# t = ()

# print(type(t))

# t = (1, ) # Создание кортежа, без запятой создастся перменна с целым числом

# print(type(t))

# v = [0, 6, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# # a, b = 1, 2 # Быстрые присваивания
# # a = b = 1

# a,b,c = v # Поместили из кортежа в переменные

# print(a, b, c)



# Словари | пара ключ - значение

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# d['w'] = 'wasd'
# d['o'] = 'ooo'

# print(d['w']) # Обращаемся по ключу w

# del d["w"] # Удаление элемента по ключу
# print(d)

# for item in d: # Красивый вывод ключ-значения
#     print("{}: {}".format(item, d[item]))



# Множества - уникальные неупорядочные значения

# colors = {'red', 'green', 'blue'}
# print(colors)

# colors.add('red') # add добавить(только уникальные элементы, повторно добавить не получится)
# print(colors)

# colors.add('gray')
# print(colors)

# colors.remove('red') # remove удалить элемент
# print(colors)

# colors.discard('red') # discard удаляет значение если оно есть во множестве, если его нет, то пропускает
# print(colors)

# colors.clear() # clear удаляет все элементы из множества
# print(colors)

# a = {1, 2, 3, 4, 5}
# b = {2, 3, 4, 5, 6}

# c = a.copy() # copy копирует уникальные элементы из одного множества в другое
# u = a.union(b) # union объединяет два множества (уникальные элементы)
# i = a.intersection(b) # intersection пересечения элементов
# dl = a.difference(b) # difference разность элементов
# dr = b.difference(a) # 
# q = a.union(b).difference(a.intersection(b)) # 

# a = {1, 2, 3}

# b = frozenset(a) # fronzenset Замораживает множество (нельзя никак изменять)

# print(b)



# List Comprehension ~ Генератор списка
# Можно создать список используя цикл for, а так же if-else

# Простая ситуация - список:
# list_1 = [exp for item in iterable]

# Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

# Допустим задача - создать список чисел от 1 до 100
# Обычным образом делали бы так:

# list_1 = []

# for i in range(1, 100):
#     list_1.append(i)

# print(list_1)


# А можно сделать так!


# list_1 = [i for i in range(1, 100)]

# Добавим условие, например только четные числа

# list_1 = [i for i in range(1, 100) if i % 2 == 0]

# Допустим, решили создать пары каждому из чисел(кортежи)

# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]

# Так же можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2

# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1)



# Лекция 3:

# Функции - фрагмент программы, испольщуемый многократно.

# def function_name(x):
    # body line 1
        # ...
    # body line n
    # optional return

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1): # первый аргумент начало, второй конец
#         summa += i
#     return summa # return завершит выполнение функции

# a = sum_numbers(5)
# print(a)



# def sum_str(*args): # * - неограниченное количество аргументов
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'e'))



# Модули - файл, в котором находятся различные функции, этот файл потом можно использовать - "import"

# Условно: создали файл modul1 с кодом:

# def max1(a, b):
#     if a > b:
#         return a
#     return b


# import modul1 # импортирует файл modul1
# print(modul1.max1(1, 2))

# from modul1 import max1 # берет из файла modul1 функцию max1

# print(max1(1, 2))

# from modul1 import * # * - использует все функции из файла modul1

# print(max1(1, 2))

# import modul1 as m1 # Импортирует файл modul1 и берет название m1 (локально только в этом коде)

# print(m1.max1(1, 2))



# Рекурсия - функция, которая вызывает саму себя

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# lst_1 = []

# for i in range(1, 10):
#     lst_1.append(fib(i))
# print(lst_1)



# Быстрая сортировка - разбитие чего-то большого, на несколько меленьких

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([1, 2, 3]))



# Сортировка слиянием - список постоянно делится пополам, пока не останется по одному элементу


# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# lst1 = [1, 2, 3, 4, 5, 69, 69, 123, 456, 123456]
# merge_sort(lst1)
# print(lst1)



# Лекция 4: 

# Функции: 

# def calk1(a):
#     return a+a

# def calk2(a):
#     return a*a

# def math(op, x):
#     print(op(x))

# math(calk1, 5)
# math(calk2, 5)



# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a, b: a + b

# math(calk1, 5, 45)

# math(lambda a, b: a + b, 5, 45)



# lst1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# print(lst1)

# for i in lst1:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)


# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# lst1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, lst1)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)



# lst1 = [x for x in range(1, 20)]
# print(lst1)

# lst1 = list(map(lambda x: x + 10, lst1))
# print(lst1)


# lst1 = "1 2 3 4 5 6 7 8 9 00"
# lst1 = list(map(int, lst1.split())) # map итератор, split преобразует в список, с помощью map мы наш список строк преоброзовали в int
# print(lst1)


# lst1 = [15, 2, 3, 445, 5, 66, 7, 8, 95, 00]
# res = list(filter(lambda x: x % 10 == 5, lst1))
# print(res)



# # Функция zip() пробегает по минимальному входящему набору:

# users = ['u1', 'u2', 'u3', 'u4', 'u5']
# id = [1, 2, 3, 4]
# salary = [111, 222, 333]

# data = list(zip(users, id, salary))
# print(data) # [('u1', 1, 111), ('u2', 2, 222), ('u3', 3, 333)]




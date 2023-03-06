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



# 
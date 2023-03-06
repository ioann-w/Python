# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монет: "))

e_sum, t_sum = 0, 0 # Сумма орлов и сумма решек

for i in range(n):
    count = int(input(f"Решка(1) или Орел(0)? # {i + 1}: "))
    if count == 0:
        e_sum += 1
    else:
        t_sum += 1

if t_sum > e_sum:
    print(f"Орлов {e_sum} из {n} монет")
else:
    print(f"Решек {t_sum} из {n} монет")



# n = int(input('Введите количество монет...'))
# count = 0
# i = 0

# while i < n:
#     type = int(input('орел или решка?\n:'))
#     if type !=1 and type != 0:
#         print("недопустимое значение") ### проверка на корректность ввода! ###
#         continue
#     elif type == 1:
#         count += 1
#         i += 1
#     else:
#         i +=1

# if n - count == 0 or count == 0: # выясняем необходимость переворачивать монеты
#     print('ничего переворачивать не нужно')
# elif count == n -count: # проверка на равность
#     print(f'одинаковое количество орлов и решек, по {count} шт.')
# elif count > n - count:
#     print(f'минимальное количество монеток {n - count}. Эти решки надо перевернуть и будет {n} орлов')
# else:
#     print(f'минимальное количество монеток {n - count}. Эти орлы надо перевернуть и будет {n} решек')



# n = int(input('введите кол... монет'))

# import random
# a = [random.randint(0, 1) for i in range(n)] # random
# print(a)

# sum_1 = 0
# sum_0 = 0

# for i in range(n):
#     if a[i] == 0:
#       sum_0 += 1
#     else:
#       sum_1 += 1

# if sum_0 < sum_1:
#   print(sum_0)
# else:
#   print(sum_1)



# from random import randit
# coins = [randint(0, 1) for _ in range(int(input()))] # "_" переменная, которая не будет использована
# print(coins)
# print(min(
#     coins.count(0),
#     coins.count(1)
# ))

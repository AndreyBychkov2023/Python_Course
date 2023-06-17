# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

N = abs(int(input('Введите натуральное число, обозначающее количество элементов в массиве: ')))
A_entered = input('Введите через пробел целые числа элементов массива: ').split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, к которому требуется найти самый близкий по величине элемент в массиве: '))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A_num[index]} в данном массиве наиболее близко по величине к числу {X}, их разница составляет {abs(X - A_num[index])}')
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [2, -5, 6, 9, 6, 0, 3, -3, 40, 0, 1, 5, 54, 10, 3, 0, -5, 3, 5, -3, 0, -5, -3, 5]

min = 5
max = 54

for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end =' ')
          
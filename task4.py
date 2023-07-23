# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# my_str = 'a a a b c a a d c d d'
# my_list = my_str.split()
# dict = {}
# for i in my_list:
#     if i in dict:
#         dict[i] += 1
#         print(f'{i}_{dict[i]}', end = ' ')
#     else: 
#         dict[i] = 0
#         print(i, end = ' ')
        
sequence = 'a a a b a c b b d'.split()
letters = {}
result = ''
for i in range(len(sequence)):
    if sequence[i] not in letters.keys():
        letters[sequence[i]] = 1
        result += f'{sequence[i]} '
    else:
        result += f'{sequence[i]}_{letters[sequence[i]]} '
        letters[sequence[i]] += 1
print(result)
        
# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

# def same_by(func, array):
#     if len(array) == 0:
#         return True
#     buf = list(map(func, array))
#     if len(list(filter(lambda x: x == buf[0], buf))) == len(buf):
#         return True
#     return False


# values = [0, 3, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
    
def same_by(characteristic, objects):
    new = list(filter(characteristic, objects))
    print(new)

    if new == objects:
        return True
    return False

def char(x):
    return x % 2 == 0

values = [2, 4, 5]
print(same_by(char, values))
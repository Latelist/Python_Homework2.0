#Реализуйте алгоритм перемешивания списка.

import random

try: 
    string = input('Enter list of numbers. Use space to split: ')
    list = string.split(' ')

    for i in range(len(list)):
        list[i] = int(list[i])

    print(list)

    for i in range(len(list)):
        new_index = random.randint(0, len(list) -1)
        temporary = list[new_index]
        list[new_index] = list[i]
        list[i] = temporary

    print(list)
except:
    print('Please, enter numbers next time. ')
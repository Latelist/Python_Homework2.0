# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

try: 
    N = int(input('Enter number: '))

    list = [1]
    for i in range(1, (N + 1)):
        list.append(list[i-1] * (i+1))

    print(list)
except: 
    print('Please, enter integer next time.')


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0


try: 
    N = int(input('Enter number: '))

    list = []
    for i in range(-N, N+1):
        list.append(i)
    print(list)

    indexes = input('Enter indexes to find product. Use space to split: ')
    indexes = indexes.split(' ')
    for i in range(len(indexes)):
        indexes[i] = int(indexes[i])


    product = 1
    for i in indexes:
        product *= list[i]

    print(product)

except:
    print('Please, enter integers next time.')

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

try: 
    N = float(input('Enter real number: '))

    while round((N - round(N)), 10) != 0:
        N *= 10

    sum = 0

    while N > 1:
        sum += N % 10
        N //= 10

    print(int(sum))
except:
    print('Please, enter integer next time.')

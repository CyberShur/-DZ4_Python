'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
'''

try:
    N = int(input('Введите натуральное число: '))
    multiplier = []
    counter = 2

    def SimpleMultiplier(a, mult, i):
        
        if a > 1:
            while i * i <= a:
                while a % i == 0:
                    mult.append(i)
                    a = a / i
                i = i + 1
            if a > 1:
                mult.append(a)
            return mult
        else:
            return print('у числа меньше 2 нет простых множителей')

    print(SimpleMultiplier(N, multiplier, counter))

except ValueError:
    print('Должно быть введено число')
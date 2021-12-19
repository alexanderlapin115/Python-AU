#!/usr/bin/env python3
a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))

def egcd(a, b, num1, num2):
    if a == 0:
        return (b, 0, 1)
    x = 0
    y = 0
    d, x, y = egcd(b % a, a, x, y)
    return (d, y - (b // a) * x, x)
d, num1, num2 = egcd(a, b, 0, 0)
print('Линейное представление двух чисел:', d, '=', a, '*', '(' , num1, ')', '+', b, '*', '(' , num2, ')')

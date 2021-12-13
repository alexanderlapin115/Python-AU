#!/usr/bin/env python3
x = int(input('Введите первое целое число: '))
y = int(input('Введите второе целое число: '))
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
print ('НОД двух чисел:', gcd(x, y))

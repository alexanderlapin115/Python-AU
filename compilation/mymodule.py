#!/usr/bin/env python3
def gcd(a, b):
    if a != 0 and b != 0:
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    if a == 0:
        return b
    if b == 0:
        return a
def sum(a, b):
    c = a + b
    return c
def subtraction(a, b):
    c = a - b
    return c
def multiplication(a, b):
    c = a * b
    return c
def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Ошибка, нельзя делить на ноль")

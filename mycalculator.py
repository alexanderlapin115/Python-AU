from mymodule import sum
from mymodule import gcd
from mymodule import division
from mymodule import subtraction
from mymodule import multiplication

a = int(input('Введите первое целое число: ')) #Нужны неотрицательные целые числа, так как для нахождения НОД используется алгоритм Евклида
b = int(input('Введите второе целое число: '))
print ("Сумма =", sum(a,b))
print ("НОД =", gcd(a,b))
print ("Частное =", division(a,b))
print ("Разность =", subtraction(a,b))
print ("Произведение =", multiplication(a,b))

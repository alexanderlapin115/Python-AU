#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')

ITERATIONS = 30
def my_cosh(x):
    sum = 1
    x += 0
    for n in range(1, ITERATIONS):
        sum += (x**(2*n)) / (math.factorial(2*n))

    return sum

A = float(input('Введите значение:'))
print("Рассчитанный гиперболический косинус: ", my_cosh(A))
print("Библиотечный гиперболический косинус: ", math.cosh(A))

vs = np.vectorize(my_cosh)

angles = np.r_[-5:5:0.01]
plt.plot(angles, vs(angles), linewidth=5, color = 'blue', alpha=0.25)
plt.plot(angles, np.cosh(angles), color='black', linewidth=1.5, linestyle='dashed')
plt.show(

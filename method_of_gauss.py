import numpy
from numpy import fabs
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

def gauss(a, b):
    a = a.copy()
    b = b.copy()
    m = len(a)

    def forward():
        for k in range (m-1):
            if fabs(a[k,k]) == 0:
                for i in range (k+1, m):
                    if fabs(a[i,k]) > fabs(a[k,k]):
                        a[k,i] = a[i,k]
            for i in range (k+1, m):
                if a[i,k] == 0:
                    continue
                s = a[k,k] / a[i,k]
                for n in range (k, m):
                    a[i,n] = a[k,n] - a[i,n] * s
                b[i] = b[k] - b [i] * s

    def backward():
        x = numpy.zeros(len(b), dtype=float)
        x [m-1] = b[m-1] / a[m-1,m-1]
        for i in range (m-2,-1,-1):
            sum = 0
            for n in range (i+1,m):
                sum += a[i,n] * x[n]
            x[i] = (b[i] - sum) / a[i,i]
        return x

    forward()
    x = backward()
    return x

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))

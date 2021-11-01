import numpy as np
from matplotlib import pyplot as pp

MODEL_G = 9.81
MODEL_DT = 0.01

class Body:
    def __init__(self, x, y, vx, vy):
        """
        Создать тело.
        
        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        vx: float
            горизонтальная скорость
        vy: float
            вертикальная скорость
        """

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
        self.trajectory_x = []
        self.trajectory_y = []
        
    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        
        if self.y < 0: # Это необходимо, чтобы тело остановилось после падения или приземления
            self.vx = 0
            self.vy = 0
        else:
            self.x += self.vx * MODEL_DT
            self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT

class Rocket(Body):
    def __init__(self, x, y, vx, vy, m, p, U):
        """
        Создать ракету.
        
        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        vx: float
            горизонтальная скорость
        vy: float
            вертикальная скорость
        m: float
            масса ракеты
        p: float
            расход топлива
        U: float
            скорость выброса топлива из сопла относительно ракеты
        """
        super().__init__(x, y, vx, vy) # Вызовем конструктор предка — тела, т.к. он для ракеты актуален

        self.m = m
        self.p = p
        self.U = U

    def advance(self):
        super().advance() # Вызовем метод предка — тела, т.к. и он для ракеты актуален

        if (self.m - self.p * MODEL_DT > 0): # Необходимо, чтобы тело ускорялось только пока есть топливо
            self.vx += 1
            self.vy += (self.U * self.p - self.m * MODEL_G) * (MODEL_DT **2)/(2 * self.m)
            self.x += self.vx * MODEL_DT
            self.y += self.vy * MODEL_DT

b = Body(0, 0, 9, 9)
r = Rocket(0, 0, 9, 9, 35, 2, 150)
bodies = [b, r]

for t in np.r_[0:2:MODEL_DT]: # для всех временных отрезков
    for b in bodies: # для всех тел
        b.advance() # выполним шаг

for b in bodies: # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y)
pp.show() # нарисуем их траектории

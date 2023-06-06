import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return 2 / (x**2 + 3 * y**2)

def rk4(f, a, b, y0, h):
    n = int((b - a) / h) + 1 #считаем количество шагов для области с шагом h
    x = np.linspace(a, b, n)
    y = np.zeros(n)
    y[0] = y0
    for i in range(n - 1):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + 1/6 * (k1 + 2*k2 + 2*k3 + k4) #обновляем значение
    return x, y

x, y = rk4(f, 3, 5, -1, 0.01)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Решение y\' = 2/(x^2 + 3y^2), y(3)=-1')
plt.show()
plt.savefig('rk4.png')
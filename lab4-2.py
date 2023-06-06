import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 + y**3

x0 = 0
y0 = 0.1

h = 0.01
n = int((1 - x0) / h)

x = np.zeros(n+1)
y = np.zeros(n+1)

x[0] = x0
y[0] = y0
x[1] = x0+0.001
y[1] = y0+0.001

f_vals = np.zeros(n+1)
for i in range(n+1):
    f_vals[i] = f(x[i], y[i])

y1 = y0 + h * f_vals[0]
y2 = y1 + h * f_vals[1]

for i in range(2, n+1):
    x[i] = x[i-1] + h
    y[i] = y[i-1] + (h/12) * (23*f_vals[i-1] - 16*f_vals[i-2] + 5*f_vals[i-3])

    f_vals[i] = f(x[i], y[i])

plt.plot(x, y, label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()




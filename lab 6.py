import numpy as np
import matplotlib.pyplot as plt

# константы
a = 0.65
b = 1.25
c = 1.05
f = -0.9
q = 1.96
h = 0.1
tau = 0.05
T = 0.5

# Параметры сетки
Nx = int(1 / h) + 1
Nt = int(T / tau) + 1

# Создание сетки
x_values = np.linspace(0, 1, Nx)
t_values = np.linspace(0, T, Nt)
U = np.zeros((Nt, Nx))

# начальные условия
U[0] = x_values**2 - x_values + f
dU_dt = f**2 + np.exp(q * x_values)

# решение смешанной задачи
for n in range(Nt - 1):
    for i in range(1, Nx - 1):
        U[n + 1, i] = (tau**2 * (U[n, i + 1] - 2 * U[n, i] + U[n, i - 1]) +
            tau**2 * (a * t_values[n] + b) / (1 + c**2 * x_values[i]**2) +
            2 * U[n, i] - U[n - 1, i] +
            h**2 * dU_dt[i]) / (1 + h * dU_dt[i])

# краевые условия
U[n + 1, 0] = f + np.sin(np.pi * t_values[n + 1])
U[n + 1, -1] = f + t_values[n + 1]**3

# построение графика при t=0.5 и t=0
plt.figure(figsize=(10, 5))
plt.plot(x_values, U[0], label='t = 0')
plt.plot(x_values, U[-1], label='t = 0.5')
plt.xlabel('x')
plt.ylabel('U(x, t)')
plt.title('Решение волнового уравнения')
plt.legend()
plt.grid(True)
plt.show()
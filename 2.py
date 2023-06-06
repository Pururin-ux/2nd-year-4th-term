import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Заданные точки
x_k = [-3.1, -3.0, -2.9, -2.8, -2.7, -2.6, -2.5]
f_x_k = [-3.6852, -3.7534, -3.9005, -4.1366, -4.4788, -4.9, -5.3]

# Точки интерполяции
x_interpolate = [-2.85, -2.73]

# Выполнение интерполяции кубическим сплайном
cs = CubicSpline(x_k, f_x_k)

# оценить значения функции в точках интерполяции
f_interpolate = cs(x_interpolate)

for x, f in zip(x_interpolate, f_interpolate):
    print(f"f({x}) = {f}")

#график
x_plot = np.linspace(min(x_k), max(x_k), 100)
f_plot = cs(x_plot)

plt.plot(x_plot, f_plot, label='Cubic Spline')
plt.scatter(x_k, f_x_k, color='red', label='Data Points')
plt.scatter(x_interpolate, f_interpolate, color='green', label='Interpolation Points')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Cubic Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()

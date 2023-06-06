import math
import numpy as np
import matplotlib.pyplot as plt

# Constants
accuracy = 0.00001

x = [2.70, 2.75, 2.80, 2.85, 2.9, 2.95, 3.0]
y = [4.3451, 4.4320, 4.5216, 4.6139, -4.7089, 4.8069, 4.9077]

#конечные разности
def whence_differences(y_array):
    return_array = []
    for i in range(0, len(y_array) - 1):
        return_array.append(y_array[i + 1] - y_array[i])
    return return_array


def witchcraft_start(y_array, h):
    part_y = [y_array[0]]
    y = y_array
    for i in range(0, len(y_array) - 1):
        y = whence_differences(y)
        part_y.append(y[0] / math.factorial(i + 1) / (h ** (i + 1)))

    return part_y


def tragic_magic(coefficients_y, point, x_array):
    value = coefficients_y[0]
    for i in range(1, len(coefficients_y)):
        q = 1
        for j in range(0, i):
            q *= (point - x_array[j])

        value += coefficients_y[i] * q
    return value

#строим точки
def build_points(x_array, y_array):
    for i in range(0, len(x_array)):
        plt.scatter(x_array[i], y_array[i])


def show_plot():
    plt.show()


def newton_there(x_array, y_array):
    x0 = x_array[0]
    h = x_array[1] - x_array[0]
    build_points(x_array, y_array)

    # возвращаем part_y = delta ^ n * y0 / (n! * h ^ n)
    part_y = witchcraft_start(y_array, h)

    print('Коэффициенты прямого полинома')
    print(part_y)

    x = np.linspace(x_array[0], x_array[len(x_array) - 1], 228)

    plt.plot(x, tragic_magic(part_y, x, x_array))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    show_plot()

#начинаем обратную интерполяцию
def witchcraft_continue(y_array, h):
    part_y = [y_array[len(y_array) - 1]]
    y = y_array
    for i in range(0, len(y_array) - 1):
        y = whence_differences(y)
        part_y.append(y[len(y) - 1] / math.factorial(i + 1) / (h ** (i + 1)))
    return part_y


def ecstatic_magic(coefficients_y, point, x_array):
    value = coefficients_y[0]
    for i in range(1, len(coefficients_y)):
        q = 1
        for j in range(0, i):
            q *= (point - x_array[len(x_array) - j - 1])

        value += coefficients_y[i] * q
    return value


def newton_here_the_boss(x_array, y_array):
    x0 = x_array[0]
    h = x_array[1] - x_array[0]
    build_points(x_array, y_array)

    # возвращаем part_y = delta ^ n * y_n / (n! * h ^ n)
    part_y = witchcraft_continue(y_array, h)

    print('Коэффициенты обратного полинома')
    print(part_y)

    x = np.linspace(x_array[0], x_array[len(x_array) - 1], 228)
    plt.plot(x, ecstatic_magic(part_y, x, x_array))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    show_plot()


if __name__ == "__main__":

    try:
        newton_there(x, y)
    except Exception as e:
        print(e)

    try:
        newton_here_the_boss(x, y)
    except Exception as e:
        print(e)
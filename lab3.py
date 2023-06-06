import random
import numpy as np
import matplotlib.pyplot as plt

#определяем функцию f(x,y)
def f(x,y):
    return x**2 + y
#устанавливаем границы интегрирования
a = 0
b = 1
c = 0
d = 1
#количество используемых случайных точек n=1000000.
n = 1000000
count = 0

points_x = []
points_y = []
#Затем мы создаем массив numpy из 100 равномерно расположенных точек между a и b, используя np.linspace() и вычисляем координаты y двух парабол y=x^2 и y^2=x. Ax.plot строит график
x = np.linspace(a, b, 100)
y1 = x**2
y2 = np.sqrt(x)
#Затем мы используем цикл for для генерации n случайных точек (x,y), равномерно распределенных в прямоугольной области D.
for i in range(n):
    x_val = random.uniform(a,b)
    y_val = random.uniform(c,d)
    #Мы подсчитываем количество точек, попадающих в область, заключенную двумя параболами y=x^2 и y^2= x и доб значение функции f (x, y) в каждой точке к подсчету промежуточной суммы.
    #Мы также сохраняем координаты x и y каждой точки в списках points_x и points_y соответственно.
    if y_val > x_val**2 and y_val**2 < x_val:
        count += f(x_val,y_val)
        points_x.append(x_val)
        points_y.append(y_val)
#Наконец, мы вычисляем площадь прямоугольника и используем ее для масштабирования значения count по количеству случайных точек n, чтобы получить приближение к двойному интегралу
area = (b-a)*(d-c)
integral = area*count/n

print("Приблизительное значение двойного интеграла:", integral)

fig, ax = plt.subplots()
ax.set_xlim([a,b])
ax.set_ylim([c,d])
ax.plot([a,b,b,a,a], [c,c,d,d,c], 'k-', lw=2)
ax.fill_between([a,b,b,a,a], [c,c,d,d,c], facecolor='gray', alpha=0.2)
ax.scatter(points_x, points_y, s=0.2, c='blue')
ax.plot(x, y1, 'r-', lw=2)
ax.plot(x, y2, 'r-', lw=2)
plt.show()

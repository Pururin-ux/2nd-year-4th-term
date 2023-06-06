import math

def f(x):
    return math.sin(x)**3 + math.cos(x)**3

a = 1   # нижний предел
b = 3   # верхний предел
e = 0.5*(10**(-3))  # точность

# определение правила Симпсона для одного подынтервала
def simpson_rule(a, b):
    h = (b - a) / 2  # step size
    fa = f(a)
    fb = f(b)
    fm = f(a + h)
    return (h / 3) * (fa + 4*fm + fb)

# используем правило Симпсона для аппроксимации интеграла по всему интервалу [a,b]
n = 1   # количество подынтервалов
approx = simpson_rule(a, b)
exact = 2.30254  # точное значение интеграла, для сравнения
while True:
    n *= 2
    h = (b - a) / n
    approx_new = 0
    for i in range(n):
        approx_new += simpson_rule(a + i*h, a + (i+1)*h)
    if abs(approx_new - approx) < e:
        break
    approx = approx_new

print("Приблизительное значение интеграла:", approx)
print("Точное значение интеграла:", exact)


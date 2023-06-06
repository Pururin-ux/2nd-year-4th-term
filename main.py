# Определение уравнений для решения
# в диагонально доминирующей форме
f1 = lambda x1, x2, x3, x4: (-77.9 - 5.5 * x4 + 0.3 * x2 - x1) / 9
f2 = lambda x1, x2, x3, x4: (-48.4 + 1.1 * x3 - 0.7 * x2 + 1.2 * x1) / 10
f3 = lambda x1, x2, x3, x4: (21.4 + 3.1 * x4 + 4.4 * x3 - 0.5 * x1) / 11
f4 = lambda x1, x2, x3, x4: (-5.5 - 2.3 * x4 - 4.8 * x3 + 2.4 * x2) / 10

# Начальная настройка
x01 = 0
x02 = 0
x03 = 0
x04 = 0
count = 1

# Точность
e = float(input('Enter eps: '))

# Реализация итерации Якоби
print('\nCount\tx1\tx2\tx3\tx4\n')

condition = True

while condition:
    x11 = f1(x01, x02, x03, x04)
    x22 = f2(x01, x02, x03, x04)
    x33 = f3(x01, x02, x03, x04)
    x44 = f4(x01, x02, x03, x04)
    print('%d\t%0.4f\t%0.4f\t%0.4f\t%0.4f\n' % (count, x11, x22, x33, x44))
    e1 = abs(x01 - x11)
    e2 = abs(x02 - x22)
    e3 = abs(x03 - x33)
    e4 = abs(x04 - x44)

    count += 1
    x01 = x11
    x02 = x22
    x03 = x33
    x04 = x44

    condition = e1 > e and e2 > e and e3 > e and e4 > e

print('\nSolution: x1=%0.3f, x2=%0.3f, x3 = %0.3f and x4 = %0.3f\n' % (x11, x22, x33, x44))
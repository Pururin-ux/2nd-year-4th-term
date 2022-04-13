def y(x):
    return ((x + .2) * x + .5) * x - 1.2


def dy(x):
    return (3 * x + .4) * x + .5


def newton(eps=.001):
    cnt = tmp = 0
    xo = 1
    while abs(xo - tmp) > eps:
        tmp = xo
        xo -= y(xo) / dy(xo)
        cnt += 1
    # для проверки
    print(round(y(xo), 6))

    return round(xo, 6), cnt


def fun_F(x):
    return (1.2 - (.2 * x + .5) * x) ** (1 / 3)


def iter_(eps=.001):
    xo = 1
    tmp = cnt = 0
    while abs(y(xo) - y(tmp)) > eps:
        tmp = xo
        xo = fun_F(xo)
        cnt += 1
    # для проверки
    print(round(y(xo), 6))

    return round(xo, 6), cnt


def secant(eps=.001):
    cnt = xo = 0
    xn = 1
    while abs(y(xn) - y(xo)) > eps:
        tmp = xn
        xn -= y(xn) * (xn - xo) / (y(xn) - y(xo))
        xo = tmp
        cnt += 1
    # для проверки
    print(round(y(xn), 6))

    return round(xn, 6), cnt


print('Метод Ньютона')
print(*newton(), '\n')
print('Метод итераций')
print(*iter_(), '\n')
print('Метод секущих')
print(*secant())
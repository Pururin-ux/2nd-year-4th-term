# подключение библиотеки tkinter
from tkinter import *
# импорт математической библиотеки
from math import *
# описание функции
def du (x,y):
    return 1/(cos(x))-y*tan(x)
def fx (x_0,y_0,x_k,n_1):
# шаг интегрирования
    h= (x_k-x_0) /n_1
#Метод Эйлера
    for i in range (0,n_1):
        y1=y_0+h*du (x_0,y_0)
        x1=x_0+h
        x_0=x1
        y_0=y1
    return y1
def rk (x_0,y_0,x_k,n_1):
    h= (x_k-x_0) /n_1
# метод рунге-кутта
    for i in range (0,n_1):
        k1=h*du (x_0,y_0)
        k2=h*du (x_0+h/2,y_0+k1/2)
        k3=h*du (x_0+h/2,y_0+k2/2)
        k4=h*du (x_0+h,y_0+k3)
        y1=y_0+ (k1+2*k2+2*k3+k4) /6
        x_0=x_0+h
        y_0=y1
    return y1
def calc_y1 ():
# начальные условия
    x0 = float (x0_entry. get ())
    y0 = float (y0_entry. get ())
# конечная точка
    xk = float (xk_entry. get ())
# число разбиений
    n = int (n_entry. get ())
# использование обработки исключений. Сначала выполняется ветвь try
    try:
        y1 = "%.3f" % fx (x0,y0,xk,n)
        y2 = "%.3f" % rk (x0,y0,xk,n)
# если во время выполнения try возникает исключение,
# то дальнейшее выполнение try прекращается и выполняется ветвь except
    except:
        y1 = "?"
        y2 = "?"
    y1_label. configure (text=y1)
    y2_label. configure (text=y2)
# создание экземпляра класса Tk, отвечающего за создание окон
root=Tk ()
# определение заголовка окна
root. title ("Задание 5")
frame = Frame (root)
frame. pack ()
t1_label = Label (frame, bg='tan', text="Численное решение дифференциального уравнения первого порядка", font='arial 12')
t1_label. grid (row=0, column=0, columnspan=5, padx=25,pady=5)
# создание окна ввода величины начального значения числа X
x0_entry = Entry (frame, width=10)
x0_entry. grid (row=1, column=2,pady=5)
x0_lebel = Label (frame, text="Начальное значение X: ")
x0_lebel. grid (row=1, column=1,pady=5)
# создание окна ввода величины начального значения числа Y
y0_entry = Entry (frame, width=10)
y0_entry. grid (row=2, column=2,pady=5)
y0_lebel = Label (frame, text="Начальное значение Y: ")
y0_lebel. grid (row=2, column=1,pady=5)
# оздание окна ввода величины конечной точки
xk_entry = Entry (frame, width=10)
xk_entry. grid (row=1, column=4,pady=5)
xk_lebel = Label (frame, text="Конечное значение Х: ")
xk_lebel. grid (row=1, column=3,pady=5)
# создание окна ввода величины точности интегрирования)
n_entry = Entry (frame, width=10)
n_entry. grid (row=2, column=4,pady=5)
n_lebel = Label (frame, text="Число разбиений: ")
n_lebel. grid (row=2, column=3,pady=5)
# создание поля вывода ответа (метод эйлера)
y1_label = Label (frame, text="?")
y1_label. grid (row=3, column=1,padx=5,pady=5)
y1_lebel = Label (frame, text="Метод Эйлера: ")
y1_lebel. grid (row=4, column=0,padx=5,pady=5)
# создание поля вывода ответа (метод рунге-кутта)
y2_label = Label (frame, text="?")
y2_label. grid (row=4, column=1,padx=5,pady=5)
y2_lebel = Label (frame, text="Метод Рунге-Кутта 4го порядка: ")
y2_lebel. grid (row=3, column=0,padx=5,pady=5)
# создание кнопки вычисления значения интеграла
eval_button = Button (frame,bg='coral', text="Вычислить", width=10,command=calc_y1)
eval_button. grid (row=4, column=3,padx=5,pady=5)
# создание кнопки закрытия приложения
exit_button = Button (frame, bg='coral', text="Выход", width=10,command=root. destroy)
exit_button. grid (row=4, column=4,padx=5,pady=5)
# непосредственное создание окна
root. mainloop ()
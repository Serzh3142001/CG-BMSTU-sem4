import random
from math import *
from tkinter import *
from tkinter import messagebox, ttk, colorchooser
import tkinter.messagebox as box
import matplotlib.pyplot as plt
import numpy as np
from time import *
import os
import sys

os.system(f'python3 ../../../gen_navigation.py {sys.argv[0][-5:-3]}')

window = Tk()

# var = IntVar()
# method = IntVar()
story = []
win_size = [700, 900]
c = Canvas(window, width=3840, height=2160, bg='white')

# ent1 = Entry(width=3)
# ent2 = Entry(width=3)
# ent3 = Entry(width=3)
# ent4 = Entry(width=3)
# ent5 = Entry(width=3)
# ent6 = Entry(width=3)
# ent8 = Entry(width=3)
# ent9 = Entry(width=3)
# ent10 = Entry(width=3)
# ent11 = Entry(width=3)
# ent12 = Entry(width=3)
# ent13 = Entry(width=3)
# ent14 = Entry(width=3)
# ent15 = Entry(width=3)
# ent16 = Entry(width=3)
# ent1.place(x=70, y=40)
# ent2.place(x=70, y=70)
# ent8.place(x=115, y=70)
# ent9.place(x=115, y=40)
# ent1.insert(0, 0)
# ent2.insert(0, 200)
# ent8.insert(0, 200)
# ent9.insert(0, 0)

# label1 = Label(text='Параметры окружности (эллипса):', fg='green', font='Arial 12')
# label2 = Label(text='Параметры пучка окружностей (эллипсов):', fg='green', font='Arial 13')
# label4 = Label(text='Центр:', font='Arial 15')
#
# label3 = Label(text='             Центр:', font='Arial 15')
# label5 = Label(text='Радиус:', font='Arial 15')
label6 = Label(text='  Цвет:', font='Arial 15')
# label7 = Label(text='    R (нач., кон.):', font='Arial 14')
# label11 = Label(text='Алгоритм:', fg='green', font='Arial 15')
# label14 = Label(text='°', font='Arial 17')
label18 = Label(text='⌘Z', font='Arial 11', fg='orange')
# label19 = Label(text='x:', font='Arial 11', fg='grey')
# label20 = Label(text='y:', font='Arial 11', fg='grey')
# label21 = Label(text='x:', font='Arial 11', fg='grey')
# label22 = Label(text='y:', font='Arial 11', fg='grey')
label23 = Label(text='Цвет фона:', font='Arial 15')
# label24 = Label(text='Полуоси:', font='Arial 14')
# label25 = Label(text='   Нач. полуоси:', font='Arial 14')
# label26 = Label(text='Шаг п-оси         ', font='Arial 14')
# label27 = Label(text='Кол-во эллипсов:', font='Arial 13')
# label28 = Label(text=':', font='Arial 14')


btn_col_line = Button(window, text='v', fg='green', command=lambda: line_col_choose())
btn_col_bg = Button(window, text='v', fg='green', command=lambda: bg_col_choose())
btn_hist = Button(window, text='Время', fg='green', command=lambda: fillWithDelay())
btn_back = Button(window, text='назад', fg='purple', command=lambda: back())
btn_cl_all = Button(window, text='🗑заново', fg='orange', command=lambda: start_state())
btn_draw_circle = Button(window, text='Закрасить', fg='red', command=lambda: fill())
btn_draw_ellipse = Button(window, text='Замкнуть', fg='blue', command=lambda: close())
# btn_draw_circle_bunch = Button(window, text='🎨○○', fg='blue', command=lambda: draw_circle_bunch(TAG))
# btn_draw_ellipse_bunch = Button(window, text='🎨⬯⬯', fg='blue', command=lambda: draw_ellipse_bunch(TAG))
btn_colorimeter = Button(window, text='🔍', fg='blue', command=lambda: os.system('open /System/Applications/Utilities/Digital\ Color\ Meter.app'))
btn_exit = Button(window, text=' выход ', fg='red', command=exit)

# set0 = Radiobutton(text="➚", fg='black', variable=var, value=0)
# set1 = Radiobutton(text="➚", fg='black', variable=var, value=1)

# set2 = Radiobutton(text="default", fg='black', variable=method, value=0)
# set3 = Radiobutton(text="Каноническое ур-е", fg='black', variable=method, value=1)
# set4 = Radiobutton(text="Параметрическое ур-е", fg='black', variable=method, value=2)
# set5 = Radiobutton(text="Брезенхем", fg='black', variable=method, value=3)
# set6 = Radiobutton(text="Средней точки", fg='black', variable=method, value=4)
# set7 = Radiobutton(text="ВУ", fg='black', variable=method, value=5)
# set1 = Radiobutton(text="➚", fg='black', variable=var, value=1)

# var.set(0)
# method.set(0)
# set0.place(x=157, y=42)
# set1.place(x=157, y=72)

# set2.place(x=220, y=42)
# set3.place(x=220, y=65)
# set4.place(x=220, y=88)
# set5.place(x=220, y=111)
# set6.place(x=220, y=134)
# set7.place(x=220, y=157)


# set10 = ttk.Combobox(window, state='readonly', values=["Шаг радиуса", "Кол-во окружностей"], width=12, font='Arial 12')
# set10.current(0)
# set11 = ttk.Combobox(window, state='readonly', values=["X", "Y"], width=1, font='Arial 12')
# set11.current(0)

ents = ''''''

lbls = '''label6.place(x=5, y=133)
label18.place(x=160, y=178)'''

btns = '''btn_col_line.place(x=135, y=133)
btn_back.place(x=116, y=175)
btn_hist.place(x=630, y=160)
btn_colorimeter.place(x=345, y=148)
btn_exit.place(x=630, y=840)
btn_draw_circle.place(x=220, y=148)
btn_draw_ellipse.place(x=220, y=175)
btn_cl_all.place(x=15, y=175)'''

rbtns = ''''''

TASK = '''
Реализовать различные алгоритмы построения одиночных отрезков. Отрезок задается координатой начала, координатой конца и цветом.

Сравнить визуальные характеристики отрезков, построенных разными алгоритмами, с помощью построения пучка отрезков, с заданным шагом.

Сравнение со стандартным алгоритмом. Задаются начальные и конечные координаты; рисуется отрезок разными методами. Отрисовка отрезка другим цветом и методом поверх первого, для проверки совпадения. Предоставить пользователю возможность выбора двух цветов – цвета фона и цвета рисования. Алгоритмы выбирать из выпадающего списка.

- ЦДА
- Брезенхем действительные числа
- Брезенхем целые числа
- Брезенхем с устранением ступенчатости
- ВУ

Построение гистограмм по количеству ступенек в зависимости от угла наклона.
'''
AUTHOR = '\n\nНиколаев Сергей ИУ7-44Б'
sz = 1
center = [365, 510]
dx = 0
dy = 0
color_coords = (98, 135), (98, 153), (149, 153), (149, 135)
resized_coords = [[89, 135], [89, 153], [139, 153], [139, 135]]
colorDraw = [(255, 0, 0), '#ff2600']

color_coords1 = (125, 844), (125, 862), (175, 862), (175, 844)
resized_coords1 = [[125, 844], [125, 862], [175, 862], [175, 844]]
colorBG = [(254.9921875, 255.99609375, 255.99609375), '#feffff']

c.create_polygon(color_coords, width=2, fill='black', tag='color')
lines = []
ellipses = []
circle_bunches = []
ellipse_bunches = []
old_dot = [0, 0]
old_angl = 0
cnt = -1
TAG = 0
TIME_FLAG = 0
DOTS = [[]]
PIXELCOLORS = [[colorBG[1] for _ in range(2560)] for _ in range(1354)]
PIXELOBJS = [[[] for _ in range(2560)] for _ in range(1354)]
DROWEDSTARTS = []
DICT = {}


# def measure_time():
#     global TAG, TIME_FLAG
#     TIME_FLAG = 1
#     radiuses = [r for r in range(100, 10002, 1000)]
#
#     standart_circle_times = []
#     canon_equation_circle_times = []
#     param_equation_circle_times = []
#     br_circle_times = []
#     middle_dot_circle_times = []
#
#     standart_ellipse_times = []
#     canon_equation_ellipse_times = []
#     param_equation_ellipse_times = []
#     br_ellipse_times = []
#     middle_dot_ellipse_times = []
#
#     tasks1 = '''standart_circle
#     canon_equation_circle
#     param_equation_circle
#     br_circle
#     middle_dot_circle'''
#
#     tasks2 = '''standart_ellipse
#     canon_equation_ellipse
#     param_equation_ellipse
#     br_ellipse
#     middle_dot_ellipse'''
#
#
#     n = 100
#     for radius in radiuses:
#         for task in tasks1.split('\n'):
#             summ1 = 0
#             for i in range(n):
#                 start = time()
#                 eval(f'{task}_draw([0, 0], {radius}, color[1], TAG)')
#                 stop = time()
#                 summ1 += stop-start
#                 # eval(f'{task}_times.append(stop-start)')
#                 if task == 'standart_circle':
#                     story.append(f'del_with_tag("t{TAG}")')
#                     back()
#                     TAG += 1
#             eval(f'{task}_times.append({summ1/n})')
#
#
#         for task in tasks2.split('\n'):
#             summ1 = 0
#             for i in range(n):
#                 start = time()
#                 eval(f'{task}_draw([0, 0], {[radius, 0.5*radius]}, color[1], TAG)')
#                 stop = time()
#                 summ1 += stop - start
#                 # eval(f'{task}_times.append(stop-start)')
#                 if task == 'standart_ellipse':
#                     story.append(f'del_with_tag("t{TAG}")')
#                     back()
#                     TAG += 1
#             eval(f'{task}_times.append({summ1 / n})')
#
#     plt.figure(figsize=(15, 6))
#
#     plt.subplot(1, 2, 1)
#     plt.title("Замеры для окружностей: ")
#     plt.plot(radiuses, standart_circle_times, label="Библиотечный\nспособ")
#     plt.plot(radiuses, canon_equation_circle_times, label="Каноническое\nуравнение")
#     plt.plot(radiuses, param_equation_circle_times, label="Параметрическое\nуравнение")
#     plt.plot(radiuses, br_circle_times, label="Брезенхем")
#     plt.plot(radiuses, middle_dot_circle_times, label="Алгоритм\nсредней точки")
#     plt.legend()
#     plt.ylabel("Время")
#     plt.xlabel("Величина радиуса")
#
#     plt.subplot(1, 2, 2)
#     plt.title("Замеры для эллипсов: ")
#     plt.plot(radiuses, standart_ellipse_times, label="Библиотечный\nспособ")
#     plt.plot(radiuses, canon_equation_ellipse_times, label="Каноническое\nуравнеие")
#     plt.plot(radiuses, param_equation_ellipse_times, label="Параметрическое\nуравнение")
#     plt.plot(radiuses, br_ellipse_times, label="Брезенхем")
#     plt.plot(radiuses, middle_dot_ellipse_times, label="Алгоритм\nсредней точки")
#     plt.legend()
#     plt.ylabel("Время")
#     plt.xlabel("Величина радиуса")
#
#     plt.show()
#
#     TIME_FLAG = 0

OLDTAG = 0
OLDY = 0
SAVEFLAG = 1

def draw_dot(x, y, colorr, tag, count_fl=False):
    global OLDTAG, OLDY, SAVEFLAG, PIXELOBJS
    # OLDTAG = tag
    if TIME_FLAG:
        c.update()
        # window.mainloop()

    if type(x) == list:
        y = x[1]
        x = x[0]

    if colorr == colorBG[1]:
        c.delete(PIXELOBJS[x][y][-1])
        PIXELOBJS[x][y].pop()
    else:
        d = 1
        #append...
        obj = c.create_polygon([x, y], [x, y + d], [x + d, y + d], [x + d, y], fill=colorr, tag=[f"t{tag}", x*y])
        PIXELOBJS[x][y].append(obj)
    # c.delete(obj)
    # OLDTAG = tag


def draw_dots_circle(dot_c, dot_dif, colorr, tag):
    x_c = dot_c[0]
    y_c = dot_c[1]

    x = dot_dif[0]
    y = dot_dif[1]

    draw_dot(net_to_canv(x_c + x, y_c + y), None, colorr, tag)
    draw_dot(net_to_canv(x_c - x, y_c + y), None, colorr, tag)
    draw_dot(net_to_canv(x_c + x, y_c - y), None, colorr, tag)
    draw_dot(net_to_canv(x_c - x, y_c - y), None, colorr, tag)

    draw_dot(net_to_canv(x_c + y, y_c + x), None, colorr, tag)
    draw_dot(net_to_canv(x_c - y, y_c + x), None, colorr, tag)
    draw_dot(net_to_canv(x_c + y, y_c - x), None, colorr, tag)
    draw_dot(net_to_canv(x_c - y, y_c - x), None, colorr, tag)


def draw_dots_ellipse(dot_c, dot_dif, colorr, tag):
    x_c = dot_c[0]
    y_c = dot_c[1]

    x = dot_dif[0]
    y = dot_dif[1]

    draw_dot(net_to_canv(x_c + x, y_c + y), None, colorr, tag)
    draw_dot(net_to_canv(x_c - x, y_c + y), None, colorr, tag)
    draw_dot(net_to_canv(x_c + x, y_c - y), None, colorr, tag)
    draw_dot(net_to_canv(x_c - x, y_c - y), None, colorr, tag)


def redraw_elems():
    del_with_tag('start')
    del_with_tag('stop')
    global TAG
    for i in range(TAG):
        del_with_tag(f't{i}')
    for line in lines:
        dda_draw(line[0], line[1], line[2], line[3])
    for ellipse in ellipses:
        draw_ellipse(ellipse[0], ellipse[1], ellipse[2], ellipse[3], ellipse[4], False, 0)
    for bunch in circle_bunches:
        draw_circle_bunch(bunch[0], bunch[1], bunch[2], bunch[3], bunch[4], bunch[5], 0)
    for bunch in ellipse_bunches:
        draw_ellipse_bunch(bunch[0], bunch[1], bunch[2], bunch[3], bunch[4], bunch[5], 0)


def line_col_choose():
    global colorDraw
    del_with_tag('color')
    colorDraw = colorchooser.askcolor()

    if not colorDraw:
        return

    c.create_polygon(resized_coords, width=2, fill=colorDraw[1], tag='color')


def bg_col_choose():
    global colorBG
    del_with_tag('color1')
    colorBG = colorchooser.askcolor()
    coordinate_field_creation()
    redraw_elems()

    if not colorBG[0]:
        return

    c.create_polygon(resized_coords1, width=2, fill=colorBG[1], tag='color1')


def net_to_canv(x, y=None):
    if y == None:
        t = x[0]
        y = x[1]
        x = t
    try:
        x, y = float(x), float(y)
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    global sz, center

    return [round(x / sz + center[0]), round(center[1] - y / sz)]


def canv_to_net(x, y=None):
    if y == None:
        t = x[0]
        y = x[1]
        x = t
    try:
        x, y = float(x), float(y)
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    global sz, center

    return [(x - center[0]) * sz, (center[1] - y) * sz]


def clean_all():
    pass
    # ent1.delete(0, END)
    # ent2.delete(0, END)
    # ent3.delete(0, END)
    # ent4.delete(0, END)
    # ent5.delete(0, END)
    # ent6.delete(0, END)
    # ent8.delete(0, END)
    # ent9.delete(0, END)
    # ent10.delete(0, END)
    # ent11.delete(0, END)
    # ent12.delete(0, END)
    # ent13.delete(0, END)
    # ent14.delete(0, END)
    # ent15.delete(0, END)
    # ent16.delete(0, END)

    # objs = c.find_withtag('rot')
    # objs += c.find_withtag('sz')
    # objs += c.find_withtag('fox')
    # for obj in objs:
    #     c.delete(obj)


def clean_coords():
    coords = c.find_withtag('coord')
    for cor in coords:
        c.delete(cor)

    net = c.find_withtag('net')
    for n in net:
        c.delete(n)


def del_with_tag(tag, pos=0):
    # if type(tag) == list:
    #     tag = tag[pos]
    for obj in c.find_withtag(tag):
        c.delete(obj)

    # if tag == 'sz':
    #     ent2.delete(0, END)
    #     ent2.insert(0, 200)


def dda_draw(start, stop, colorr, tag, count_fl=False):
    x1, y1 = start
    x2, y2 = stop
    x = [0] * 1000
    y = [0] * 1000
    xstart = round(x1)
    ystart = round(y1)
    xend = round(x2)
    yend = round(y2)
    L = max(abs(xend - xstart), abs(yend - ystart))
    dX = (x2 - x1) / L
    dY = (y2 - y1) / L
    i = 0
    x[i] = x1
    y[i] = y1
    i += 1
    while i < L:
        x[i] = x[i - 1] + dX
        y[i] = y[i - 1] + dY
        i += 1
    x[i] = x2
    y[i] = y2

    i = 0
    while i <= L:
        draw_dot(round(x[i]), round(y[i]), colorr, tag, count_fl)
        i += 1


def dda_draw_to_border(start, stop, tag, border, changeDirFlag):
    global PIXELCOLORS, DROWEDSTARTS

    x1, y1 = start
    x2, y2 = stop

    x = [0] * 1000
    y = [0] * 1000
    xstart = round(x1)
    ystart = round(y1)
    xend = round(x2)
    yend = round(y2)
    L = abs(yend - ystart)
    if not L:
        L = abs(xend - xstart)

    dX = (x2 - x1) / L
    dY = (y2 - y1) / L
    i = 0
    x[i] = x1
    y[i] = y1
    i += 1
    while i < L:
        x[i] = x[i - 1] + dX
        y[i] = y[i - 1] + dY
        i += 1

    x[i] = x2
    y[i] = y2

    i=0
    if changeDirFlag:
        i = 1

    while i < L:
        # draw_dot(round(x[i]), round(y[i]), colorr, tag, count_fl)
        # if round(y[i]) in DROWEDSTARTS:
        #     continue
        for xx in range(round(x[i]), border):
            if type(PIXELCOLORS[xx][round(y[i])]) != list:
                curColor = PIXELCOLORS[xx][round(y[i])]
                if curColor != colorBG[1] and curColor != colorDraw[1]:
                    PIXELCOLORS[xx][round(y[i])] = [PIXELCOLORS[xx][round(y[i])]]
                    curColor = colorDraw[1]
                else:
                    if curColor != colorDraw[1]:
                        curColor = colorDraw[1]
                    else:
                        curColor = colorBG[1]
                    PIXELCOLORS[xx][round(y[i])] = curColor

                # if PIXELCOLORS[xx][round(y[i])] != colorBG[1] and PIXELCOLORS[xx][round(y[i])] != colorDraw[1]:
                #     PIXELCOLORS[xx][round(y[i])] = [PIXELCOLORS[xx][round(y[i])]]
                # else:
                #     PIXELCOLORS[xx][round(y[i])] = curColor
            else:
                curColor = PIXELCOLORS[xx][round(y[i])][0]
                PIXELCOLORS[xx][round(y[i])] = PIXELCOLORS[xx][round(y[i])][0]
            draw_dot(xx, round(y[i]), curColor, tag)
        i += 1



    # DROWEDSTARTS += [y1, y2]


def printCorrectForm():
    global DICT

    for el in DICT:
        xx = []
        for ell in DICT[el]:
            x, y = canv_to_net(ell, el)
            xx.append(x)
        print(f'{y}: {xx}', end=', ')


def close():
    global TAG
    dda_draw(DOTS[-1][0], DOTS[-1][-1], 'black', TAG)
    lines.append([DOTS[-1][0], DOTS[-1][-1], 'black', TAG])
    story.append(f'del_with_tag("t{TAG}");lines.pop()')
    TAG += 1


# def pixelColor(x, y):
#     # x = window.winfo_pointerx()-window.winfo_x() # получаем координаты курсора относительно окна
#     # y = window.winfo_pointery()-window.winfo_y() #
#     # print(c.find_overlapping(x+0.5, y-0.5,x+0.5, y+0.5), x, y) # выводим, какую фигуру(-ы) накрывает квадрат 1х1 пиксель
#     return c.itemcget(c.find_overlapping(x+0.5, y-0.5, x+0.5, y+0.5)[-1], "fill" ) # выводим цвет самой верхней фигуры
    # print(colorDraw, colorBG)


# def fill(dictt=None, st=1):
#     global DICT, SAVEFLAG, TAG
#
#     if not dictt:
#         for y in DICT:
#             DICT[y] = sorted(DICT[y])
#
#         dictt = DICT
#
#     if st:
#         story.append(f'del_with_tag("t{TAG}");circles.pop()')
#
#     printCorrectForm()
#
#     SAVEFLAG = 0
#
#     for y in dictt:
#         print(y)
#         # try:
#         for i in range(0, len(dictt[y]), 2):
#             try:
#                 dda_draw([dictt[y][i], y], [dictt[y][i+1], y], color[1], TAG)
#             except:
#                 pass  # текущая полит. ситуация. Программа для преодоления трудностей
#
#     SAVEFLAG = 1
#     TAG += 1

def fillWithDelay():
    global TIME_FLAG
    TIME_FLAG = 1
    fill()
    TIME_FLAG = 0

def fill(st=1):
    global DOTS, TAG, colorDraw, story
    close()
    # DOTS = [(257, 619), (289, 418), (302, 469), (351, 438), (271, 386), (350, 356), (387, 458), (484, 574), (333, 675)]

    borderR = max([dot[0] for dot in DOTS[-1]])
    borderL = min([dot[0] for dot in DOTS[-1]])
    borderT = max([dot[1] for dot in DOTS[-1]])
    borderB = min([dot[1] for dot in DOTS[-1]])
    for i in range(len(DOTS[-1])):
        dir = 0
        # if i != 0:
        arr = sorted([DOTS[-1][i-1][1], DOTS[-1][i][1], DOTS[-1][(i+1)%len(DOTS[-1])][1]])
        if DOTS[-1][i][1] != arr[1]:
            dir = 1

        dda_draw_to_border(DOTS[-1][i], DOTS[-1][(i+1)%len(DOTS[-1])], TAG, borderR, dir)

    for i in range(borderL, borderR):
        for j in range(borderB, borderT):
            if type(PIXELCOLORS[i][j]) == list:
                PIXELCOLORS[i][j] = colorDraw[1]


    if st:
        story.append(f'del_with_tag("t{TAG}");DOTS.pop();resetPixels()')
        # story.append(f'DOTS.pop()')


    #RESET!!!

    TAG += 1
    DOTS.append([])
    # colorDraw[1] = ['blue', 'green', 'black', 'orange', 'pink', 'red'][TAG%6]

def resetPixels():
    global PIXELCOLORS
    PIXELCOLORS = [[colorBG[1] for _ in range(2560)] for _ in range(1354)]

def click(event):
    global TAG, DOTS
    # disable()
    # pixelColor(event.x, event.y)
    # dotts = c.find_withtag('dot')
    for dot in DOTS[-1]:
        if is_cursor_touch_dot(dot, event):
            DOTS[-1].append(dot)
            dda_draw(DOTS[-1][-2], DOTS[-1][-1], 'black', TAG)

            dotts = c.find_withtag('dot')
            story.append(f'c.delete({dotts[-1]});DOTS[-1].pop()')

            crds = event.x, event.y
            DOTS[-1].append(crds)
            if len(DOTS[-1]) > 1:
                dda_draw(DOTS[-1][-2], DOTS[-1][-1], 'black', TAG)
                lines.append([DOTS[-1][-2], DOTS[-1][-1], 'black', TAG])
                story[-1] += f';del_with_tag("t{TAG}");lines.pop()'

            TAG += 1
            # print(DICT)
            # enable()
            # tc = c.find_withtag('tc')
            # for tc1 in tc:
            #     c.delete(tc1)
            #
            # true_c = canv_to_net(c.coords(dot)[0], c.coords(dot)[1])
            # c.create_text(298, 842, text=f'{true_c[0] + 2:g}', tag='tc')
            # c.create_text(388, 842, text=f'{true_c[1] - 2:g}', tag='tc')
            # text1.configure(state=NORMAL)
            # text2.configure(state=NORMAL)
            # print(dot, c.coords(dot), event.x, event.y)
            # disable()
            return

    # triangls = c.find_withtag('triang')
    # for tri in triangls:
    #     if is_cursor_touch_triang(tri, event):
    #         tri_click(event, tri)
    #         return

    if event.x < 65 or event.x > 665 + dx or event.y < 210 or event.y > 810 + dy:
        return

    print(PIXELCOLORS[event.x][event.y])
    print_dot(event)

    dotts = c.find_withtag('dot')
    story.append(f'c.delete({dotts[-1]});DOTS[-1].pop()')

    crds = event.x, event.y
    DOTS[-1].append(crds)
    if len(DOTS[-1]) > 1:
        dda_draw(DOTS[-1][-2], DOTS[-1][-1], 'black', TAG)
        lines.append([DOTS[-1][-2], DOTS[-1][-1], 'black', TAG])
        story[-1] += f';del_with_tag("t{TAG}");lines.pop()'
        TAG += 1
    # print(DOTS)
    # print(DICT)
    # if var.get():
    #     flag2 += 1
    #     enable()
    #     text2.insert(END, f'({crds[0]:g}; {crds[1]:g})\n')
    #     disable()
    #     sett2 = text2.get(1.0, END).split('\n')[:-1]
    #     if not sett2[-1]:
    #         sett2 = sett2[:-1]
    #
    #     end = len(sett2)
    #     story[-1] += f'; text2.delete({end}.0, END)'
    #     story[-1] += '; text2.insert(END, "\\n")' if end > 1 else ''
    # else:
    #     flag1 += 1
        # enable()
        # text1.insert(END, f'({crds[0]:g}; {crds[1]:g})\n')
        # disable()
        #
        # sett1 = text1.get(1.0, END).split('\n')[:-1]
        # if not sett1[-1]:
        #     sett1 = sett1[:-1]

        # end = len(sett1)
        # story[-1] += f'; text1.delete({end}.0, END)'
        # story[-1] += '; text1.insert(END, "\\n")' if end > 1 else ''


def print_dot(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    # if var.get():
    #     c.create_oval(x1, y1, x2, y2, outline='blue', fill='blue', tag='dot', activeoutline='lightgreen', activefill='lightgreen')
    # else:
    c.create_oval(x1, y1, x2, y2, outline='black', fill='black', tag='dot', activeoutline='lightgreen', activefill='lightgreen')

def is_cursor_touch_dot(dot, event):
    # coo = c.coords(dot)
    coo = dot
    x, y = event.x, event.y

    if coo[0] - 2 <= x <= coo[0] + 2 and coo[1] - 2 <= y <= coo[1] + 2:
        return 1
    else:
        return 0


# def click(event):
#     global res_coords, rot_coords
#     if event.x < 65 or event.x > 665 + dx or event.y < 210 or event.y > 810 + dy:
#         return
#
#     global rotate_point, resize_point
#     if var.get() == 1:
#         rotate_point = canv_to_net(event.x, event.y)
#         reprint_dot(rotate_point)
#         ent3.delete(0, END)
#         ent4.delete(0, END)
#         ent3.insert(0, f'{canv_to_net(event.x, event.y)[0]:g}')
#         ent4.insert(0, f'{canv_to_net(event.x, event.y)[1]:g}')
#     elif var.get() == 0:
#         resize_point = canv_to_net(event.x, event.y)
#         reprint_dot(resize_point)
#     elif var.get() == 2:
#         ent3.delete(0, END)
#         ent4.delete(0, END)
#         ent3.insert(0, f'{canv_to_net(event.x, event.y)[0]:g}')
#         ent4.insert(0, f'{canv_to_net(event.x, event.y)[1]:g}')


def reprint_dot(coords, fl=0):
    global sz
    try:
        coords[0], coords[1] = float(coords[0]), float(coords[1])
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    buf = net_to_canv(coords[0], coords[1])

    x1, y1 = (buf[0] - 2), (buf[1] - 2)
    x2, y2 = (buf[0] + 2), (buf[1] + 2)

    if (fl == 1 or not var.get()) and fl != 2:
        del_with_tag('start')
        ent1.delete(0, END)
        ent9.delete(0, END)
        ent1.insert(END, f'{coords[0]:g}')
        ent9.insert(END, f'{coords[1]:g}')
        c.create_oval(x1, y1, x2, y2, outline='blue', fill='blue', tag='start', activeoutline='lightgreen',
                      activefill='lightgreen')
    elif fl == 2 or var.get():
        del_with_tag('stop')
        ent2.delete(0, END)
        # ent8.delete(0, END)
        ent2.insert(END, f'{coords[0]:g}')
        # ent8.insert(END, f'{coords[1]:g}')
        c.create_oval(x1, y1, x2, y2, outline='red', fill='red', tag='stop', activeoutline='lightgreen',
                      activefill='lightgreen')


def back():
    if not len(story):
        return

    command = story[-1]
    commands = []
    if ';' in command:
        commands = command.split(';')
    else:
        commands.append(command)

    for com in commands:
        if not com:
            continue
        print(com)
        eval(com)

    del story[-1]


def scale(x, y):
    global sz
    prev_sz = sz
    while x < (150 + dx / 4) * sz and y < (150 + dy / 4) * sz:
        sz /= 2

    while x > (300 + dx / 2) * sz or y > (300 + dy / 2) * sz:
        sz *= 2

    if sz != prev_sz:
        redraw_net_coords()


def redraw_net_coords():
    global sz

    coords = c.find_withtag('coord')
    for cor in coords:
        c.delete(cor)

    max_len = 0
    for i in range(65, 665 + dx, 50):
        if len(f'{round((i - 365) * sz, 3):g}') > max_len:
            max_len = len(f'{round((i - 365) * sz, 3):g}')

    for i in range(round(center[0] + 50), 665 + dx, 50):
        c.create_text(i, 530 + dy / 2, fill='grey', text=f'{round((i - center[0]) * sz, 3):g}', tag='coord',
                      font='Verdana 8' if max_len > 6 else 'Verdana 12')

    for i in range(round(center[0] - 50), 65, -50):
        c.create_text(i, 530 + dy / 2, fill='grey', text=f'{round((i - center[0]) * sz, 3):g}', tag='coord',
                      font='Verdana 8' if max_len > 6 else 'Verdana 12')

    for i in range(round(center[1] + 50), 810 + dy, 50):
        c.create_text(345 + dx / 2, i + 10, fill='grey', text=f'{round(-(i - center[1]) * sz, 3):g}', tag='coord')

    for i in range(round(center[1] - 50), 210, -50):
        c.create_text(345 + dx / 2, i + 10, fill='grey', text=f'{round(-(i - center[1]) * sz, 3):g}', tag='coord')


def buttons_creation():
    btn_cl_all.place(x=25, y=170)
    btn_back.place(x=25, y=140)
    btn_exit.place(x=630, y=840)


def coordinate_field_creation():
    global center, colorBG
    del_with_tag('bg')

    if not colorBG[1]:
        colorBG = ['', 'white']

    c.create_polygon([[65, 210], [65, 811 + dy], [666 + dx, 811 + dy], [666 + dx, 210]], width=2, fill=colorBG[1],
                     tag='bg')
    center[0] = round(365 + dx / 2)
    center[1] = round(510 + dy / 2)
    clean_coords()
    c.create_line(33, 510 + dy / 2, 695 + dx, 510 + dy / 2, fill='grey',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6", tag='net')
    c.create_line(365 + dx / 2, 835 + dy, 365 + dx / 2, 185, fill='grey',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6", tag='net')
    c.create_line(665 + dx, 210, 665 + dx, 810 + dy, fill='black',
                  width=1, dash=(5, 9), tag='net')
    c.create_line(65, 810 + dy, 665 + dx, 810 + dy, fill='black',
                  width=1, dash=(5, 9), tag='net')
    c.create_line(65, 210, 665 + dx, 210, fill='black',
                  width=1, dash=(5, 9), tag='net')
    c.create_line(65, 210, 65, 810 + dy, fill='black',
                  width=1, dash=(5, 9), tag='net')

    # c.create_line(225 + dx / 4, 5, 225 + dx / 4, 180, fill='black',
    #               width=1, dash=(5, 9), tag='net')
    #
    # c.create_line(440 + dx / 1.8, 5, 440 + dx / 1.8, 180, fill='black',
    #               width=1, dash=(5, 9), tag='net')
    #
    # c.create_line(5, 27, 700 + dx, 27, fill='grey',
    #               width=1, dash=(5, 9), tag='net')

    for i in range(round(center[0] + 50), 665 + dx, 50):
        c.create_line(i, 503 + dy / 2, i, 520 + dy / 2, fill='grey', width=2, tag='net')
        c.create_line(i, 210, i, 810 + dy, fill='grey', width=1, dash=(1, 9), tag='net')

    for i in range(round(center[0] - 50), 65, -50):
        c.create_line(i, 503 + dy / 2, i, 520 + dy / 2, fill='grey', width=2, tag='net')
        c.create_line(i, 210, i, 810 + dy, fill='grey', width=1, dash=(1, 9), tag='net')

    for i in range(round(center[1] + 50), 810 + dy, 50):
        c.create_line(358 + dx / 2, i, 372 + dx / 2, i, fill='grey', width=2, tag='net')
        c.create_line(65, i, 665 + dx, i, fill='grey', width=1, dash=(1, 9), tag='net')

    for i in range(round(center[1] - 50), 210, -50):
        c.create_line(358 + dx / 2, i, 372 + dx / 2, i, fill='grey', width=2, tag='net')
        c.create_line(65, i, 665 + dx, i, fill='grey', width=1, dash=(1, 9), tag='net')

    c.create_text(688 + dx, 493 + dy / 2, text='X', font='Verdana 20', fill='green', tag='net')
    c.create_text(380 + dx / 2, 195, text='Y', font='Verdana 20', fill='green', tag='net')
    redraw_net_coords()


def start_state():
    global story, rot_coords, res_coords, circles, circle_bunches, TAG, ellipses, circle_bunches, ellipse_bunches
    scale(290, 290)
    story = []
    circles = []
    ellipses = []
    circle_bunches = []
    ellipse_bunches = []

    circle_bunches = []
    clean_all()
    for i in range(TAG):
        del_with_tag(f't{i}')
    del_with_tag('start')
    del_with_tag('stop')
    TAG = 0
    # ent1.insert(0, 0)
    # ent2.insert(0, 200)
    # ent3.insert(0, 50)
    # ent4.insert(0, -150)
    # ent5.insert(0, 10)
    # ent6.insert(0, 100)
    # ent8.insert(0, 100)
    # ent9.insert(0, 0)
    # ent10.insert(0, 200)
    # ent11.insert(0, 10)
    # ent12.insert(0, 15)
    # ent13.insert(0, 5)
    # ent14.insert(0, 10)
    # ent15.insert(0, 0)
    # ent16.insert(0, 20)


old_dx, old_dy = dx, dy


def config(event):
    global dx, dy, old_dx, old_dy, rotate_point, resize_point, resized_coords, resized_coords1
    if event.widget == window:
        kx = window.winfo_width() / win_size[0]
        ky = window.winfo_height() / win_size[1]

        if kx < 0.9 or ky < 0.85:
            return

        max_elems = 30
        ent_places = [0] * max_elems
        lbl_places = [0] * max_elems
        btn_places = [0] * max_elems
        radiobtn_places = [0] * max_elems

        if 'ent' in ents:
            for ent in ents.split('\n'):
                ind = int(ent.split('ent')[1].split('.')[0])
                ent_places[ind] = [int(ent.split('x=')[1].split(',')[0]), int(ent.split('y=')[1].split(')')[0])]

        for lbl in lbls.split('\n'):
            ind = int(lbl.split('label')[1].split('.')[0])
            lbl_places[ind] = [int(lbl.split('x=')[1].split(',')[0]), int(lbl.split('y=')[1].split(')')[0])]

        k = 0
        for btn in btns.split('\n'):
            name = btn.split('.')[0]
            btn_places[k] = [name, int(btn.split('x=')[1].split(',')[0]), int(btn.split('y=')[1].split(')')[0])]
            k += 1

        if 'set' in ents:
            for rbtn in rbtns.split('\n'):
                rbtn, koef = rbtn.split(':')
                ind = int(rbtn.split('set')[1].split('.')[0])
                radiobtn_places[ind] = [int(rbtn.split('x=')[1].split(',')[0]), int(rbtn.split('y=')[1].split(')')[0]), float(koef)]

        # try:
        for i in range(max_elems):
            if lbl_places[i]:
                eval(f'label{i}.place(x={lbl_places[i][0]} * kx, y={lbl_places[i][1]} * 1)')
            if ent_places[i]:
                eval(f'ent{i}.place(x={ent_places[i][0]} * kx, y={ent_places[i][1]} * 1)')
            if btn_places[i]:
                eval(f'{btn_places[i][0]}.place(x={btn_places[i][1]} * kx, y={btn_places[i][2]} * 1)')
            if radiobtn_places[i]:
                eval(f'set{i}.place(x={radiobtn_places[i][0]} * kx * {radiobtn_places[i][2]}, y={radiobtn_places[i][1]} * 1)')
        # except:
        #     pass
        btn_exit.place(x=window.winfo_width() - 70, y=window.winfo_height() - 60)
        btn_col_bg.place(x=170, y=window.winfo_height() - 60)

        del_with_tag('color')
        del_with_tag('color1')

        resized_coords = []
        resized_coords1 = []
        for i in range(len(color_coords)):
            resized_coords.append([color_coords[i][0], color_coords[i][1]])
            resized_coords[i][0] *= kx/1.1
            resized_coords1.append([color_coords1[i][0], color_coords1[i][1]])
            resized_coords1[i][1] *= ky
        c.create_polygon(resized_coords, width=2, fill=colorDraw[1], tag='color')
        c.create_polygon(resized_coords1, width=2, fill=colorBG[1], tag='color1')
        label23.place(x=20, y=window.winfo_height() - 60)

        old_dx, old_dy = dx, dy
        dx = window.winfo_width() - win_size[0]
        dy = window.winfo_height() - win_size[1]
        coordinate_field_creation()
        redraw_elems()
        c.place(x=-15, y=0)


c.bind('<1>', click)
window.bind("<Command-z>", lambda event: back())
window.bind("<Configure>", config)
window.bind("<Button-2>", fill)


buttons_creation()
coordinate_field_creation()
start_state()

mmenu = Menu(window)
add_menu = Menu(mmenu)
add_menu.add_command(label='О программе и авторе',
                     command=lambda: messagebox.showinfo('О программе и авторе', TASK + AUTHOR))
add_menu.add_command(label='Выход', command=exit)
mmenu.add_cascade(label='About', menu=add_menu)
window.config(menu=mmenu)

window.geometry('700x900')
c.pack()
window.mainloop()

from math import *
from tkinter import *
from tkinter import messagebox, ttk, colorchooser
import tkinter.messagebox as box
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

os.system(f'python3 ../../../gen_navigation.py {sys.argv[0][-5:-3]}')

window = Tk()

var = IntVar()
method = IntVar()
story = []
win_size = [700, 900]
c = Canvas(window, width=3840, height=2160, bg='white')

ent1 = Entry(width=3)
ent2 = Entry(width=3)
ent3 = Entry(width=3)
ent4 = Entry(width=3)
ent5 = Entry(width=3)
ent6 = Entry(width=3)
ent8 = Entry(width=3)
ent9 = Entry(width=3)
ent10 = Entry(width=3)
ent11 = Entry(width=3)
ent12 = Entry(width=3)
ent13 = Entry(width=3)
ent14 = Entry(width=3)
# ent15 = Entry(width=3)
ent16 = Entry(width=3)
ent1.place(x=70, y=40)
ent2.place(x=70, y=70)
# ent8.place(x=115, y=70)
ent9.place(x=115, y=40)
ent1.insert(0, 0)
ent2.insert(0, 200)
# ent8.insert(0, 200)
ent9.insert(0, 0)

label1 = Label(text='Параметры окружности (эллипса):', fg='green', font='Arial 12')
label2 = Label(text='Параметры пучка окружностей (эллипсов):', fg='green', font='Arial 13')
label4 = Label(text='Центр:', font='Arial 15')

label3 = Label(text='             Центр:', font='Arial 15')
label5 = Label(text='Радиус:', font='Arial 15')
label6 = Label(text='  Цвет:', font='Arial 15')
label7 = Label(text='    R (нач., кон.):', font='Arial 14')
label11 = Label(text='Алгоритм:', fg='green', font='Arial 15')
# label14 = Label(text='°', font='Arial 17')
label18 = Label(text='⌘Z', font='Arial 11', fg='orange')
label19 = Label(text='x:', font='Arial 11', fg='grey')
label20 = Label(text='y:', font='Arial 11', fg='grey')
label21 = Label(text='x:', font='Arial 11', fg='grey')
label22 = Label(text='y:', font='Arial 11', fg='grey')
label23 = Label(text='Цвет фона:', font='Arial 15')
label24 = Label(text='Полуоси:', font='Arial 14')
label25 = Label(text='   Нач. полуоси:', font='Arial 14')
label26 = Label(text='Шаг п-оси         ', font='Arial 14')
label27 = Label(text='Кол-во эллипсов:', font='Arial 13')
label28 = Label(text=':', font='Arial 14')


btn_col_line = Button(window, text='v', fg='green', command=lambda: line_col_choose())
btn_col_bg = Button(window, text='v', fg='green', command=lambda: bg_col_choose())
btn_hist = Button(window, text='Время', fg='green', command=lambda: count_steps())
btn_back = Button(window, text='назад', fg='purple', command=lambda: back())
btn_cl_all = Button(window, text='🗑заново', fg='orange', command=lambda: start_state())
btn_draw_circle = Button(window, text='Нарисовать ○', fg='blue', command=lambda: draw_circle(TAG))
btn_draw_ellipse = Button(window, text='Нарисовать ⬯', fg='blue', command=lambda: draw_ellipse(TAG))
btn_draw_circle_bunch = Button(window, text='🎨○○', fg='blue', command=lambda: draw_circle_bunch(TAG))
btn_draw_ellipse_bunch = Button(window, text='🎨⬯⬯', fg='blue', command=lambda: draw_ellipse_bunch(TAG))
btn_colorimeter = Button(window, text='🔍', fg='blue', command=lambda: os.system('open /System/Applications/Utilities/Digital\ Color\ Meter.app'))
btn_exit = Button(window, text=' выход ', fg='red', command=exit)

set0 = Radiobutton(text="➚", fg='black', variable=var, value=0)
# set1 = Radiobutton(text="➚", fg='black', variable=var, value=1)

set2 = Radiobutton(text="default", fg='black', variable=method, value=0)
set3 = Radiobutton(text="Каноническое ур-е", fg='black', variable=method, value=1)
set4 = Radiobutton(text="Параметрическое ур-е", fg='black', variable=method, value=2)
set5 = Radiobutton(text="Брезенхем", fg='black', variable=method, value=3)
set6 = Radiobutton(text="Средней точки", fg='black', variable=method, value=4)
# set7 = Radiobutton(text="ВУ", fg='black', variable=method, value=5)
set1 = Radiobutton(text="➚", fg='black', variable=var, value=1)

var.set(0)
method.set(0)
set0.place(x=157, y=42)
# set1.place(x=157, y=72)

set2.place(x=220, y=42)
set3.place(x=220, y=65)
set4.place(x=220, y=88)
set5.place(x=220, y=111)
set6.place(x=220, y=134)
# set7.place(x=220, y=157)

set10 = ttk.Combobox(window, state='readonly', values=["Шаг радиуса", "Кол-во окружностей"], width=12, font='Arial 12')
set10.current(0)
set11 = ttk.Combobox(window, state='readonly', values=["X", "Y"], width=1, font='Arial 12')
set11.current(0)

ents = '''ent1.place(x=72, y=40)
ent2.place(x=72, y=70)
ent3.place(x=540, y=40)
ent4.place(x=579, y=40)
ent5.place(x=540, y=66)
ent6.place(x=579, y=66)
ent8.place(x=72, y=103)
ent9.place(x=115, y=40)
ent10.place(x=115, y=103)
ent11.place(x=540, y=92)
ent12.place(x=540, y=118)
ent13.place(x=579, y=118)
ent14.place(x=540, y=144)
ent16.place(x=540, y=170)'''

lbls = '''label1.place(x=5, y=4)
label2.place(x=428, y=4)
label3.place(x=428, y=43)
label4.place(x=5, y=43)
label5.place(x=5, y=73)
label6.place(x=5, y=133)
label7.place(x=428, y=72)
label11.place(x=215, y=2)
label18.place(x=160, y=178)
label19.place(x=72, y=25)
label20.place(x=117, y=25)
label21.place(x=538, y=25)
label22.place(x=578, y=25)
label24.place(x=4, y=105)
label25.place(x=428, y=121)
label26.place(x=428, y=149)
label27.place(x=426, y=177)
label28.place(x=526, y=149)'''

btns = '''btn_col_line.place(x=135, y=133)
btn_back.place(x=116, y=175)
btn_hist.place(x=630, y=160)
btn_colorimeter.place(x=345, y=148)
btn_exit.place(x=630, y=840)
btn_draw_circle.place(x=220, y=148)
btn_draw_ellipse.place(x=220, y=175)
btn_draw_circle_bunch.place(x=630, y=70)
btn_draw_ellipse_bunch.place(x=630, y=130)
btn_cl_all.place(x=15, y=175)'''

rbtns = '''set0.place(x=157, y=42):1
set2.place(x=220, y=32):1
set3.place(x=220, y=55):1
set4.place(x=220, y=78):1
set5.place(x=220, y=101):1
set6.place(x=220, y=124):1
set1.place(x=619, y=42):1
set10.place(x=430, y=93):1
set11.place(x=498, y=148):1'''

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
color = [(255, 0, 0), '#ff0000']

color_coords1 = (125, 844), (125, 862), (175, 862), (175, 844)
resized_coords1 = [[125, 844], [125, 862], [175, 862], [175, 844]]
color1 = [(254.9921875, 255.99609375, 255.99609375), '#feffff']

c.create_polygon(color_coords, width=2, fill='black', tag='color')
circles = []
ellipses = []
circle_bunches = []
ellipse_bunches = []
old_dot = [0, 0]
old_angl = 0
cnt = -1
TAG = 0


def rgb_to_hex(rgb):
    rgb = tuple(map(int, rgb))
    return '#%02x%02x%02x' % rgb


def draw_dot(x, y, colorr, tag, count_fl=False):
    if type(x) == list:
        y = x[1]
        x = x[0]

    global old_dot, old_angl, cnt

    if not count_fl:
        d = 1
        c.create_polygon([x, y], [x, y + d], [x + d, y + d], [x + d, y], fill=colorr, tag=f"t{tag}")
        # print(tag)
    else:
        if x - old_dot[0]:
            new_angl = abs(y - old_dot[1])/abs(x - old_dot[0])
        else:
            new_angl = abs(x - old_dot[0]) / abs(y - old_dot[1])

        if new_angl != old_angl:
            cnt += 1

        old_angl = new_angl
        old_dot = [x, y]


def count_steps():
    global cnt, old_dot, old_angl
    hist1 = []
    hist2 = []
    hist3 = []
    hist4 = []
    hist5 = []

    try:
        center = [float(ent3.get()), float(ent4.get())]
        radius = float(ent5.get())
        step = int(ent6.get())
    except:
        box.showinfo('Error', 'Некорректные координаты!')
        return

    colorr = color
    for met in range(1, 6):
        for alpha in range(0, 91, step):
            start = center
            stop = [start[0] + radius * sin(radians(alpha)), start[1] + radius * cos(radians(alpha))]
            draw_ellipse(0, start, stop, colorr, met, True, 0)
            for i in range(cnt//2):
                eval(f'hist{met}.append(alpha)')
            cnt = -1
            old_dot = [0, 0]
            old_angl = 0

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 3, 1)
    plt.hist(hist1, 90)
    plt.ylabel('Кол-во ступенек')
    plt.title('ЦДА')
    plt.subplot(2, 3, 2)
    plt.hist(hist2, 90)
    plt.title('Брезенхейм (float)')
    plt.subplot(2, 3, 3)
    plt.hist(hist3, 90)
    plt.title('Брезенхейм (int)')
    plt.subplot(2, 3, 4)
    plt.hist(hist4, 90)
    plt.xlabel('Угол')
    plt.title('Брезенхейм (устр. ступ)')
    plt.subplot(2, 3, 5)
    plt.hist(hist5, 90)
    plt.title('ВУ')

    plt.show()


def redraw_elems():
    del_with_tag('start')
    del_with_tag('stop')
    global TAG
    for i in range(TAG):
        del_with_tag(f't{i}')
    for circle in circles:
        draw_circle(circle[0], circle[1], circle[2], circle[3], circle[4], False, 0)
    for ellipse in ellipses:
        draw_ellipse(ellipse[0], ellipse[1], ellipse[2], ellipse[3], ellipse[4], False, 0)
    for bunch in circle_bunches:
        draw_circle_bunch(bunch[0], bunch[1], bunch[2], bunch[3], bunch[4], bunch[5], 0)
    for bunch in ellipse_bunches:
        draw_ellipse_bunch(bunch[0], bunch[1], bunch[2], bunch[3], bunch[4], bunch[5], 0)


def draw_circle(tag, center=None, radius=None, colorr=None, met=None, count_fl=False, st=1):
    global TAG
    if not center:
        try:
            center, radius = [[float(ent1.get()), float(ent9.get())], float(ent2.get())]
            met = method.get()
            colorr = color
            circles.append([tag, center, radius, color, met])
        except:
            box.showinfo('Error', 'Некорректные данные!')
            return


    redraw_flag = 0
    max_stop_x = abs(int(center[0])) + radius
    max_stop_y = abs(int(center[1])) + radius
    if max_stop_x > (300 + dx / 2) * sz or max_stop_y > (300 + dy / 2) * sz:
        scale(max_stop_x, max_stop_y)
        redraw_flag = 1

    if st:
        story.append(f'del_with_tag("t{tag}");circles.pop()')

    if met == 0:
        standart_circle_draw(center, radius, colorr[1], tag)
    elif met == 1:
        canon_equation_circle_draw(center, radius, colorr[1], tag, count_fl)
    elif met == 2:
        param_equation_circle_draw(center, radius, colorr[1], tag, count_fl)
    elif met == 3:
        br_circle_draw(center, radius, colorr[1], tag, count_fl)
    elif met == 4:
        middle_dot_circle_draw(center, radius, colorr, tag, count_fl)

    if redraw_flag:
        redraw_elems()

    if st:
        TAG += 1


def draw_ellipse(tag, center=None, axcises=None, colorr=None, met=None, count_fl=False, st=1):
    global TAG
    if not center:
        try:
            center, axcises = [[float(ent1.get()), float(ent9.get())], [float(ent8.get()), float(ent10.get())]]
            if axcises[0] < 0 or axcises[1] < 0:
                raise
            met = method.get()
            colorr = color
            ellipses.append([tag, center, axcises, color, met])
        except:
            box.showinfo('Error', 'Некорректные данные!')
            return


    redraw_flag = 0
    max_stop_x = abs(int(center[0])) + axcises[0]
    max_stop_y = abs(int(center[1])) + axcises[1]
    if max_stop_x > (300 + dx / 2) * sz or max_stop_y > (300 + dy / 2) * sz:
        scale(max_stop_x, max_stop_y)
        redraw_flag = 1

    if st:
        story.append(f'del_with_tag("t{tag}");ellipses.pop()')

    if met == 0:
        standart_ellipse_draw(center, axcises, colorr[1], tag)
    elif met == 1:
        canon_equation_ellipse_draw(center, axcises, colorr[1], tag, count_fl)
    elif met == 2:
        param_equation_ellipse_draw(center, axcises, colorr[1], tag, count_fl)
    elif met == 3:
        br_ellipse_draw(center, axcises, colorr[1], tag, count_fl)
    elif met == 4:
        middle_dot_ellipse_draw(center, axcises, colorr, tag, count_fl)

    if redraw_flag:
        redraw_elems()

    if st:
        TAG += 1


def draw_circle_bunch(tag, center=None, colorr=None, met=None, radiuses=None, step_or_count=None, st=1):
    global TAG
    if not center:
        try:
            center = [float(ent3.get()), float(ent4.get())]
            radiuses = [float(ent5.get()), float(ent6.get())]
            if radiuses[0] > radiuses[1]:
                box.showinfo('Error', 'Начальный радиус больше конечного!')
                return
            if set10.get():
                step_or_count = int(ent11.get())
                step_or_count = [step_or_count, 'count']
            else:
                step_or_count = float(ent11.get())
                step_or_count = [step_or_count, 'step']
            if step_or_count[0] <= 0:
                raise

        except:
            box.showinfo('Error', 'Некорректные данные!')
            return

        met = method.get()
        colorr = color
        circle_bunches.append([tag, center, colorr, met, radiuses, step_or_count])

    max_stop_x = abs(center[0]) + radiuses[1]
    max_stop_y = abs(center[1]) + radiuses[1]
    # print(max_stop_x, max_stop_y)

    redraw_flag = 0
    if max_stop_x > (300 + dx/2)*sz or max_stop_y > (300 + dy/2)*sz:
        scale(max_stop_x, max_stop_y)
        redraw_flag = 1

    if st:
        story.append(f'del_with_tag("t{tag}");circle_bunches.pop()')

    if step_or_count[1] == 'step':
        step = step_or_count[0]
    else:
        step = (radiuses[1] - radiuses[0])/step_or_count[0]

    for radius in np.arange(radiuses[0], radiuses[1], step):
        if met == 0:
            standart_circle_draw(center, radius, colorr[1], tag)
        elif met == 1:
            canon_equation_circle_draw(center, radius, colorr[1], tag)
        elif met == 2:
            param_equation_circle_draw(center, radius, colorr[1], tag)
        elif met == 3:
            br_circle_draw(center, radius, colorr[1], tag)
        elif met == 4:
            middle_dot_circle_draw(center, radius, colorr, tag)

    if redraw_flag:
        redraw_elems()

    if st:
        TAG += 1


def draw_ellipse_bunch(tag, center=None, colorr=None, met=None, axcises=None, step_and_count=None, st=1):
    global TAG
    if not center:
        try:
            center = [float(ent3.get()), float(ent4.get())]
            axcises = [float(ent12.get()), float(ent13.get())]
            if axcises[0] < 0 or axcises[1] < 0:
                raise

            step_and_count = [float(ent14.get()), int(ent16.get())]
            if set11.get():
                step_and_count.append('x')
            else:
                step_and_count.append('y')
            if step_and_count[0] <= 0 or step_and_count[1] <= 0:
                raise

        except:
            box.showinfo('Error', 'Некорректные данные!')
            return

        met = method.get()
        colorr = color
        ellipse_bunches.append([tag, center, colorr, met, axcises, step_and_count])

    max_stop_x = abs(center[0]) + axcises[0] + step_and_count[0]*step_and_count[1]
    max_stop_y = abs(center[1]) + axcises[1] + step_and_count[0]*step_and_count[1]
    # print(max_stop_x, max_stop_y)

    redraw_flag = 0
    if max_stop_x > (300 + dx/2)*sz or max_stop_y > (300 + dy/2)*sz:
        scale(max_stop_x, max_stop_y)
        redraw_flag = 1

    if st:
        story.append(f'del_with_tag("t{tag}");ellipse_bunches.pop()')

    ######
    change_index = 0
    if step_and_count[2] == 'x':
        change_index = 0
    else:
        change_index = 1

    for i in range(step_and_count[1]):

        if met == 0:
            standart_ellipse_draw(center, axcises, colorr[1], tag)
        elif met == 1:
            canon_equation_ellipse_draw(center, axcises, colorr[1], tag)
        elif met == 2:
            param_equation_ellipse_draw(center, axcises, colorr[1], tag)
        elif met == 3:
            br_ellipse_draw(center, axcises, colorr[1], tag)
        elif met == 4:
            middle_dot_ellipse_draw(center, axcises, colorr, tag)
        axcises[change_index] += step_and_count[0]

    # if redraw_flag:
    #     redraw_elems()

    if st:
        TAG += 1


def standart_circle_draw(center, radius, colorr, tag):
    # global TAG
    x1, y1 = list(map(round, net_to_canv(center[0]-radius, center[1]+radius)))
    x2, y2 = list(map(round, net_to_canv(center[0] + radius, center[1] - radius)))

    c.create_oval(x1, y1, x2, y2, width=1, outline=colorr, tag=f't{tag}')


def canon_equation_circle_draw(center, radius, colorr, tag, count_fl=False):
    pass


def param_equation_circle_draw(center, radius, colorr, tag, count_fl=False):
    pass


def br_circle_draw(center, radius, colorr, tag, count_fl=False):
    pass


def middle_dot_circle_draw(center, radius, colorr, tag, count_fl=False):
    pass


def standart_ellipse_draw(center, axcises, colorr, tag):
    # global TAG
    x1, y1 = list(map(round, net_to_canv(center[0]-axcises[0], center[1]+axcises[1])))
    x2, y2 = list(map(round, net_to_canv(center[0] + axcises[0], center[1] - axcises[1])))

    c.create_oval(x1, y1, x2, y2, width=1, outline=colorr, tag=f't{tag}')


def canon_equation_ellipse_draw(center, radius, colorr, tag, count_fl=False):
    pass


def param_equation_ellipse_draw(center, radius, colorr, tag, count_fl=False):
    pass


def br_ellipse_draw(center, radius, colorr, tag, count_fl=False):
    pass


def middle_dot_ellipse_draw(center, radius, colorr, tag, count_fl=False):
    pass


def change_brightness(col, k):
    col = col[0]
    col = list(col)
    for i in range(3):
        col[i] += (255 - col[i]) * (1 - k)

    return rgb_to_hex(col)


def sign(diff):
    if diff < 0:
        return -1
    elif diff == 0:
        return 0
    else:
        return 1


def fpart(x):
    return abs(x - int(x))


def line_col_choose():
    global color
    del_with_tag('color')
    color = colorchooser.askcolor()

    if not color:
        return

    c.create_polygon(resized_coords, width=2, fill=color[1], tag='color')


def bg_col_choose():
    global color1
    del_with_tag('color1')
    color1 = colorchooser.askcolor()
    coordinate_field_creation()
    redraw_elems()

    if not color1[0]:
        return

    c.create_polygon(resized_coords1, width=2, fill=color1[1], tag='color1')


def cart_sum(a, b):
    return a[0] + b[0], a[1] + b[1]


def cart_dif(a, b):
    return a[0] - b[0], a[1] - b[1]


def rotate(a, alpha, center):
    a = cart_dif(a, center)
    res = (cos(alpha) * a[0] - sin(alpha) * a[1],
           sin(alpha) * a[0] + cos(alpha) * a[1])
    res = cart_sum(res, center)
    return res


def resize(a, k, center):
    k1 = k[0]
    k2 = k[1]
    a = cart_dif(a, center)
    res = (a[0] * k1, a[1] * k2)
    res = cart_sum(res, center)
    return res


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
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent8.delete(0, END)
    ent9.delete(0, END)
    ent10.delete(0, END)

    objs = c.find_withtag('rot')
    objs += c.find_withtag('sz')
    objs += c.find_withtag('fox')
    for obj in objs:
        c.delete(obj)


def clean_coords():
    coords = c.find_withtag('coord')
    for cor in coords:
        c.delete(cor)

    net = c.find_withtag('net')
    for n in net:
        c.delete(n)


def del_with_tag(tag):
    for obj in c.find_withtag(tag):
        c.delete(obj)

    if tag == 'sz':
        ent2.delete(0, END)
        ent2.insert(0, 200)


def click(event):
    global res_coords, rot_coords
    if event.x < 65 or event.x > 665 + dx or event.y < 210 or event.y > 810 + dy:
        return

    global rotate_point, resize_point
    if var.get() == 1:
        rotate_point = canv_to_net(event.x, event.y)
        reprint_dot(rotate_point)
        ent3.delete(0, END)
        ent4.delete(0, END)
        ent3.insert(0, f'{canv_to_net(event.x, event.y)[0]:g}')
        ent4.insert(0, f'{canv_to_net(event.x, event.y)[1]:g}')
    elif var.get() == 0:
        resize_point = canv_to_net(event.x, event.y)
        reprint_dot(resize_point)
    elif var.get() == 2:
        ent3.delete(0, END)
        ent4.delete(0, END)
        ent3.insert(0, f'{canv_to_net(event.x, event.y)[0]:g}')
        ent4.insert(0, f'{canv_to_net(event.x, event.y)[1]:g}')


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
    global center, color1
    del_with_tag('bg')

    if not color1[1]:
        color1 = ['', 'white']

    c.create_polygon([[65, 210], [65, 810 + dy], [665 + dx, 810 + dy], [665 + dx, 210]], width=2, fill=color1[1],
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

    c.create_line(225 + dx / 4, 5, 225 + dx / 4, 180, fill='black',
                  width=1, dash=(5, 9), tag='net')

    c.create_line(440 + dx / 1.8, 5, 440 + dx / 1.8, 180, fill='black',
                  width=1, dash=(5, 9), tag='net')

    c.create_line(5, 27, 700 + dx, 27, fill='grey',
                  width=1, dash=(5, 9), tag='net')

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
    global story, rot_coords, res_coords, circles, circle_bunches, TAG
    scale(290, 290)
    story = []
    circles = []
    circle_bunches = []
    clean_all()
    for i in range(TAG):
        del_with_tag(f't{i}')
    del_with_tag('start')
    del_with_tag('stop')
    TAG = 0
    ent1.insert(0, 0)
    ent2.insert(0, 200)
    ent3.insert(0, 150)
    ent4.insert(0, -150)
    ent5.insert(0, 10)
    ent6.insert(0, 100)
    ent8.insert(0, 100)
    ent9.insert(0, 0)
    ent10.insert(0, 200)
    ent11.insert(0, 10)
    ent12.insert(0, 10)
    ent13.insert(0, 15)
    ent14.insert(0, 10)
    # ent15.insert(0, 0)
    ent16.insert(0, 10)


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

        for rbtn in rbtns.split('\n'):
            rbtn, koef = rbtn.split(':')
            ind = int(rbtn.split('set')[1].split('.')[0])
            radiobtn_places[ind] = [int(rbtn.split('x=')[1].split(',')[0]), int(rbtn.split('y=')[1].split(')')[0]), float(koef)]

        for i in range(max_elems):
            if lbl_places[i]:
                eval(f'label{i}.place(x={lbl_places[i][0]} * kx, y={lbl_places[i][1]} * 1)')
            if ent_places[i]:
                eval(f'ent{i}.place(x={ent_places[i][0]} * kx, y={ent_places[i][1]} * 1)')
            if btn_places[i]:
                eval(f'{btn_places[i][0]}.place(x={btn_places[i][1]} * kx, y={btn_places[i][2]} * 1)')
            if radiobtn_places[i]:
                eval(f'set{i}.place(x={radiobtn_places[i][0]} * kx * {radiobtn_places[i][2]}, y={radiobtn_places[i][1]} * 1)')
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
        c.create_polygon(resized_coords, width=2, fill=color[1], tag='color')
        c.create_polygon(resized_coords1, width=2, fill=color1[1], tag='color1')
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

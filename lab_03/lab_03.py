from math import *
from tkinter import *
import tkinter.messagebox as box
from tkinter import messagebox
from tkinter import colorchooser
import matplotlib.pyplot as plt


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
ent1.place(x=70, y=40)
ent2.place(x=70, y=70)
ent8.place(x=115, y=70)
ent9.place(x=115, y=40)
ent1.insert(0, 0)
ent2.insert(0, 200)
ent8.insert(0, 200)
ent9.insert(0, 0)

label1 = Label(text='Координаты отрезка:', font='Arial 15')
label1.place(x=60, y=5)
label2 = Label(text='Пучок отрезков:', font='Arial 15')
label3 = Label(text='Центр:', font='Arial 15')

label4 = Label(text='Начало:', font='Arial 15')
label5 = Label(text='Конец:', font='Arial 15')
label6 = Label(text='Цвет:', font='Arial 15')
label7 = Label(text='Радиус, шаг:', font='Arial 13')
label11 = Label(text='Способ:', font='Arial 15')
label14 = Label(text='°', font='Arial 17')
label18 = Label(text='⌘Z', font='Arial 11', fg='orange')
label19 = Label(text='x:', font='Arial 11', fg='grey')
label20 = Label(text='y:', font='Arial 11', fg='grey')
label21 = Label(text='x:', font='Arial 11', fg='grey')
label22 = Label(text='y:', font='Arial 11', fg='grey')
label23 = Label(text='Цвет фона:', font='Arial 15')

label1.place(x=5, y=5)
label4.place(x=5, y=43)
label5.place(x=15, y=73)
label6.place(x=22, y=103)
label11.place(x=535, y=43)
label18.place(x=20, y=120)
label19.place(x=70, y=25)
label20.place(x=115, y=25)
label23.place(x=20, y=830)


btn_col_line = Button(window, text='v', fg='green', command=lambda: line_col_choose())
btn_col_bg = Button(window, text='v', fg='green', command=lambda: bg_col_choose())
btn_hist = Button(window, text='📊Гистограммы', fg='green', command=lambda: count_steps())
btn_back = Button(window, text='назад', fg='purple', command=lambda: back())
btn_cl_all = Button(window, text='🗑заново', fg='orange', command=lambda: start_state())
btn_draw = Button(window, text='Нарисовать отрез.', fg='blue', command=lambda: draw_line(TAG))
btn_draw_bunch = Button(window, text='Нарисовать пучок', fg='blue', command=lambda: draw_bunch(TAG))
btn_exit = Button(window, text=' выход ', fg='red', command=exit)

set0 = Radiobutton(text="➚", fg='black', variable=var, value=0)
set1 = Radiobutton(text="➚", fg='black', variable=var, value=1)

set2 = Radiobutton(text="default", fg='black', variable=method, value=0)
set3 = Radiobutton(text="ЦДА", fg='black', variable=method, value=1)
set4 = Radiobutton(text="Брезенхейм (float)", fg='black', variable=method, value=2)
set5 = Radiobutton(text="Брезенхейм (int)", fg='black', variable=method, value=3)
set6 = Radiobutton(text="Брезенхейм (устр. ступен.)", fg='black', variable=method, value=4)
set7 = Radiobutton(text="ВУ", fg='black', variable=method, value=5)
set8 = Radiobutton(text="➚", fg='black', variable=var, value=2)

var.set(1)
method.set(0)
set0.place(x=157, y=42)
set1.place(x=157, y=72)

set2.place(x=220, y=42)
set3.place(x=220, y=65)
set4.place(x=220, y=88)
set5.place(x=220, y=111)
set6.place(x=220, y=134)
set7.place(x=220, y=157)

ents = '''ent1.place(x=70, y=40)
ent2.place(x=70, y=70)
ent3.place(x=525, y=40)
ent4.place(x=570, y=40)
ent5.place(x=525, y=70)
ent6.place(x=570, y=70)
ent8.place(x=115, y=70)
ent9.place(x=115, y=40)'''

lbls = '''label1.place(x=5, y=5)
label2.place(x=435, y=5)
label3.place(x=465, y=43)
label4.place(x=5, y=43)
label5.place(x=15, y=73)
label6.place(x=22, y=103)
label7.place(x=437, y=75)
label11.place(x=220, y=5)
label14.place(x=608, y=70)
label18.place(x=80, y=143)
label19.place(x=70, y=25)
label20.place(x=115, y=25)
label21.place(x=525, y=25)
label22.place(x=570, y=25)'''

btns = '''btn_col_line.place(x=135, y=103)
btn_back.place(x=25, y=140)
btn_hist.place(x=437, y=140)
btn_exit.place(x=630, y=840)
btn_draw.place(x=220, y=175)
btn_draw_bunch.place(x=437, y=105)'''

rbtns = '''set0.place(x=157, y=42)
set1.place(x=157, y=72)
set2.place(x=220, y=32)
set3.place(x=220, y=55)
set4.place(x=220, y=78)
set5.place(x=220, y=101)
set6.place(x=220, y=124)
set7.place(x=220, y=147)
set8.place(x=610, y=42)'''

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
color_coords = (87, 105), (87, 123), (137, 123), (137, 105)
resized_coords = [[87, 105], [87, 123], [137, 123], [137, 105]]
color = [(0.0, 0.0, 0.0), '#000000']

color_coords1 = (125, 844), (125, 862), (175, 862), (175, 844)
resized_coords1 = [[125, 844], [125, 862], [175, 862], [175, 844]]
color1 = [(254.9921875, 255.99609375, 255.99609375), '#feffff']

c.create_polygon(color_coords, width=2, fill='black', tag='color')
lines = []
bunches = []
old_dot = [0, 0]
old_angl = 0
cnt = -1
TAG = 0


def rgb_to_hex(rgb):
    rgb = tuple(map(int, rgb))
    return '#%02x%02x%02x' % rgb


def draw_dot(x, y, colorr, tag, count_fl=False):
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
            draw_line(0, start, stop, colorr, met, True, 0)
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
    global TAG
    for i in range(TAG):
        del_with_tag(f't{i}')
    for line in lines:
        draw_line(line[0], line[1], line[2], line[3], line[4], False, 0)
    for bunch in bunches:
        draw_bunch(bunch[0], bunch[1], bunch[2], bunch[3], bunch[4], bunch[5], 0)


def draw_line(tag, start=None, stop=None, colorr=None, met=None, count_fl=False, st=1):
    global TAG
    if not start:
        start, stop = [ent1.get(), ent9.get()], [ent2.get(), ent8.get()]
        met = method.get()
        colorr = color
        lines.append([tag, start, stop, color, met])

    if max(abs(int(start[0])), abs(int(stop[0]))) > 300 + dx/2 or max(abs(int(start[1])), abs(int(stop[1]))) > 300 + dy/2:
        box.showinfo('Error', f'Выход за границы:\nx: ({-(300 + dx//2)}...{300 + dx//2})\ny: ({-(300 + dy//2)}...{300 + dy//2})')
        lines.pop()
        return

    if st:
        story.append(f'del_with_tag("t{tag}");lines.pop()')

    if met == 0:
        standart_draw(start, stop, colorr[1], tag)
    elif met == 1:
        dda_draw(start, stop, colorr[1], tag, count_fl)
    elif met == 2:
        br_float_draw(start, stop, colorr[1], tag, count_fl)
    elif met == 3:
        br_int_draw(start, stop, colorr[1], tag, count_fl)
    elif met == 4:
        br_smooth_draw(start, stop, colorr, tag, count_fl)
    elif met == 5:
        vu_draw(start, stop, colorr, tag, count_fl)

    if st:
        TAG += 1


def draw_bunch(tag, center=None, colorr=None, met=None, radius=None, step=None, st=1):
    global TAG
    if not center:
        try:
            center = [float(ent3.get()), float(ent4.get())]
            radius = float(ent5.get())
            step = int(ent6.get())
        except:
            box.showinfo('Error', 'Некорректные координаты!')
            return

        met = method.get()
        colorr = color
        bunches.append([tag, center, colorr, met, radius, step])

    max_stop = max(list(map(abs, center))) + radius
    if max(abs(int(center[0])), abs(int(max_stop))) > 300 + dx/2 or max(abs(int(center[1])), abs(int(max_stop))) > 300 + dy/2:
        box.showinfo('Error', f'Выход за границы:\nx: ({-(300 + dx//2)}...{300 + dx//2})\ny: ({-(300 + dy//2)}...{300 + dy//2})')
        bunches.pop()
        return

    if st:
        story.append(f'del_with_tag("t{tag}");bunches.pop()')

    for alpha in range(0, 360, step):
        start = center
        stop = [start[0] + radius * sin(radians(alpha)), start[1] + radius * cos(radians(alpha))]
        if met == 0:
            standart_draw(start, stop, colorr[1], tag)
        elif met == 1:
            dda_draw(start, stop, colorr[1], tag)
        elif met == 2:
            br_float_draw(start, stop, colorr[1], tag)
        elif met == 3:
            br_int_draw(start, stop, colorr[1], tag)
        elif met == 4:
            br_smooth_draw(start, stop, colorr, tag)
        elif met == 5:
            vu_draw(start, stop, colorr, tag)

    if st:
        TAG += 1


def standart_draw(start, stop, colorr, tag):
    # global TAG
    c.create_line([net_to_canv(start), net_to_canv(stop)], width=1, fill=colorr, tag=f't{tag}')


def dda_draw(start, stop, colorr, tag, count_fl=False):
    x1, y1 = net_to_canv(start)
    x2, y2 = net_to_canv(stop)
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


def br_float_draw(start, stop, colorr, tag, count_fl=False):
    x0, y0 = list(map(int, start))
    x1, y1 = list(map(int, stop))
    dx = x1 - x0
    dy = y1 - y0

    if dx <= 0 and dy >= 0 and abs(dx) >= abs(dy) or dx <= 0 and dy <= 0 or dx >= 0 and dy <= 0 and abs(dy) > abs(dx):
        x0, y0, x1, y1 = x1, y1, x0, y0

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    error = 0
    deltaerr = (dy + 1) / (dx + 1)
    y = y0
    x = x0
    diry = y1 - y0
    if diry > 0:
        diry = 1
    if diry < 0:
        diry = -1

    dirx = x1 - x0
    if dirx > 0:
        dirx = 1
    if dirx < 0:
        dirx = -1

    if deltaerr <= 1:
        for x in range(x0, x1):
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, tag, count_fl)
            error += deltaerr
            if error >= 1.0:
                y += diry
                error -= 1.0
    else:
        deltaerr = 1/deltaerr
        for y in range(y0, y1):
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, tag, count_fl)
            error += deltaerr
            if error >= 1.0:
                x += dirx
                error -= 1.0


def br_int_draw(start, stop, colorr, tag, count_fl=False):
    x0, y0 = list(map(int, start))
    x1, y1 = list(map(int, stop))
    dx = x1 - x0
    dy = y1 - y0

    if dx <= 0 and dy >= 0 and abs(dx) >= abs(dy) or dx <= 0 and dy <= 0 or dx >= 0 and dy <= 0 and abs(dy) > abs(dx):
        x0, y0, x1, y1 = x1, y1, x0, y0

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    error = 0
    deltaerr = (dy + 1)
    deltaerr1 = (dx + 1)
    y = y0
    x = x0
    diry = y1 - y0
    if diry > 0:
        diry = 1
    if diry < 0:
        diry = -1

    dirx = x1 - x0
    if dirx > 0:
        dirx = 1
    if dirx < 0:
        dirx = -1

    if dx >= dy:
        for x in range(x0, x1):
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, tag, count_fl)
            error += deltaerr
            if error >= dx + 1:
                y += diry
                error -= (dx + 1)
    else:
        for y in range(y0, y1):
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, tag, count_fl)
            error += deltaerr1
            if error >= dy + 1:
                x += dirx
                error -= (dy + 1)


def change_brightness(col, k):
    col = col[0]
    col = list(col)
    for i in range(3):
        col[i] += (255-col[i])*(1-k)

    return rgb_to_hex(col)

def br_smooth_draw(start, stop, colorr, tag, count_fl=False):
    x0, y0 = list(map(round, (list(map(float, start)))))
    x1, y1 = list(map(round, list(map(float, stop))))
    dx = x1 - x0
    dy = y1 - y0

    if dx <= 0 and dy >= 0 and abs(dx) >= abs(dy) or dx <= 0 and dy <= 0 or dx >= 0 and dy <= 0 and abs(dy) > abs(dx):
        x0, y0, x1, y1 = x1, y1, x0, y0

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    I = 1
    dxx = abs(x1 - x0 + 1)
    dyy = abs(y1 - y0 + 1)
    m = min(dxx, dyy)/max(dxx, dyy)  # max?
    if not x1-x0 or not y1-y0:
        m = 1
    w = I - m
    e = 1 / 2
    y = y0
    x = x0
    diry = y1 - y0
    if diry > 0:
        diry = 1
    if diry < 0:
        diry = -1

    dirx = x1 - x0
    if dirx > 0:
        dirx = 1
    if dirx < 0:
        dirx = -1

    draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), change_brightness(colorr, m / 2), tag, count_fl)
    if dx >= dy:
        while x < x1:
            if e < w:
                x += 1
                e += m
            else:
                x += 1
                y += diry
                e -= w
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), change_brightness(colorr, e), tag, count_fl)
    else:
        while y < y1:
            if e < w:
                y += 1
                e += m
            else:
                y += 1
                x += dirx
                e -= w
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), change_brightness(colorr, e), tag, count_fl)


    # c.create_polygon(list(map(net_to_canv, [[0, 0], [0, 100], [100, 100], [100, 0]])), fill=change_brightness(colorr, k1))
    #
    # c.create_polygon(list(map(net_to_canv, [[102, 0], [102, 100], [202, 100], [202, 0]])), fill=change_brightness(colorr, 1-k1))


def fpart(x):
    return abs(x - int(x))


def vu_draw(start, stop, colorr, tag, count_fl=False):
    x0, y0 = list(map(round, list(map(float, start))))
    x1, y1 = list(map(round, list(map(float, stop))))

    dx = x1 - x0
    dy = y1 - y0

    if dx <= 0 and dy >= 0 and abs(dx) >= abs(dy) or dx <= 0 and dy <= 0 or dx >= 0 and dy <= 0 and abs(dy) > abs(dx):
        x0, y0, x1, y1 = x1, y1, x0, y0

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    gradient = min(dx, dy)/max(dx, dy)

    diry = y1 - y0
    if diry > 0:
        diry = 1
    if diry < 0:
        diry = -1

    dirx = x1 - x0
    if dirx > 0:
        dirx = 1
    if dirx < 0:
        dirx = -1

    # обработать начальную точку
    xend = round(x0)
    yend = y0 + gradient * (xend - x0)
    xgap = 1 - fpart(x0 + 0.5)
    xpxl1 = xend  # будет использоваться в основном цикле
    ypxl1 = int(yend)
    draw_dot(round(net_to_canv(xpxl1, ypxl1)[0]), round(net_to_canv(xpxl1, ypxl1)[1]),
             change_brightness(colorr, (1 - fpart(yend)) * xgap), tag, count_fl)
    draw_dot(round(net_to_canv(xpxl1, ypxl1+1)[0]), round(net_to_canv(xpxl1, ypxl1+1)[1]),
             change_brightness(colorr, fpart(yend) * xgap), tag, count_fl)
    intery = yend + gradient  # первое y - пересечение для цикла
    interx = xend + gradient

    # обработать конечную точку
    xend = round(x1)
    yend = y1 + gradient * (xend - x1)
    xgap = fpart(x1 + 0.5)
    xpxl2 = xend  # будет использоваться в основном цикле
    ypxl2 = int(yend)
    draw_dot(round(net_to_canv(xpxl2, ypxl2)[0]), round(net_to_canv(xpxl2, ypxl2)[1]),
             change_brightness(colorr, (1 - fpart(yend)) * xgap), tag, count_fl)
    draw_dot(round(net_to_canv(xpxl2, ypxl2 + 1)[0]), round(net_to_canv(xpxl2, ypxl2 + 1)[1]),
             change_brightness(colorr, fpart(yend) * xgap), tag, count_fl)

    # основной цикл
    if abs(dx) >= abs(dy):
        for x in range(xpxl1, xpxl2):
            if intery >= 0:
                draw_dot(round(net_to_canv(x, int(intery))[0]), round(net_to_canv(x, int(intery))[1]),
                         change_brightness(colorr, 1 - fpart(intery)), tag, count_fl)
                if not count_fl:
                    draw_dot(round(net_to_canv(x, int(intery)+1)[0]), round(net_to_canv(x, int(intery)+1)[1]),
                             change_brightness(colorr, fpart(intery)), tag)
            else:
                draw_dot(round(net_to_canv(x, int(intery))[0]), round(net_to_canv(x, int(intery))[1]),
                         change_brightness(colorr, fpart(intery)), tag, count_fl)
                if not count_fl:
                    draw_dot(round(net_to_canv(x, int(intery) - 1)[0]), round(net_to_canv(x, int(intery) + 1)[1]),
                             change_brightness(colorr, 1 - fpart(intery)), tag)
            intery += gradient*diry
    else:
        for y in range(ypxl1, ypxl2):
            if interx >= 0:
                draw_dot(round(net_to_canv(int(interx), y)[0]), round(net_to_canv(int(interx), y)[1]),
                         change_brightness(colorr, 1 - fpart(interx)), tag, count_fl)
                if not count_fl:
                    draw_dot(round(net_to_canv(int(interx)+1, y)[0]), round(net_to_canv(int(interx)+1, y)[1]),
                             change_brightness(colorr, fpart(interx)), tag)
            else:
                draw_dot(round(net_to_canv(int(interx), y)[0]), round(net_to_canv(int(interx), y)[1]),
                         change_brightness(colorr, fpart(interx)), tag, count_fl)
                if not count_fl:
                    draw_dot(round(net_to_canv(int(interx) + 1, y)[0]), round(net_to_canv(int(interx) - 1, y)[1]),
                             change_brightness(colorr, 1 - fpart(interx)), tag)
            interx += gradient*dirx


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
        dotts = c.find_withtag('start')
        for dot in dotts:
            c.delete(dot)
        ent1.delete(0, END)
        ent9.delete(0, END)
        ent1.insert(END, f'{coords[0]:g}')
        ent9.insert(END, f'{coords[1]:g}')
        c.create_oval(x1, y1, x2, y2, outline='blue', fill='blue', tag='start', activeoutline='lightgreen',
                      activefill='lightgreen')
    elif fl == 2 or var.get():
        dotts = c.find_withtag('stop')
        for dot in dotts:
            c.delete(dot)
        ent2.delete(0, END)
        ent8.delete(0, END)
        ent2.insert(END, f'{coords[0]:g}')
        ent8.insert(END, f'{coords[1]:g}')
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
        redraw()


def redraw():
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

    c.create_line(440 + dx / 2, 5, 440 + dx / 2, 180, fill='black',
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
    redraw()


def start_state():
    global story, rot_coords, res_coords, lines, bunches, TAG
    scale(200, 200)
    story = []
    lines = []
    bunches = []
    clean_all()
    for i in range(TAG):
        del_with_tag(f't{i}')
    TAG = 0
    ent1.insert(0, 0)
    ent2.insert(0, 200)
    ent3.insert(0, 150)
    ent4.insert(0, -150)
    ent5.insert(0, 100)
    ent6.insert(0, 5)
    ent8.insert(0, 200)
    ent9.insert(0, 0)


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
            ind = int(rbtn.split('set')[1].split('.')[0])
            radiobtn_places[ind] = [int(rbtn.split('x=')[1].split(',')[0]), int(rbtn.split('y=')[1].split(')')[0])]

        for i in range(max_elems):
            if ent_places[i]:
                eval(f'ent{i}.place(x={ent_places[i][0]} * kx, y={ent_places[i][1]} * 1)')
            if lbl_places[i]:
                eval(f'label{i}.place(x={lbl_places[i][0]} * kx, y={lbl_places[i][1]} * 1)')
            if btn_places[i]:
                eval(f'{btn_places[i][0]}.place(x={btn_places[i][1]} * kx, y={btn_places[i][2]} * 1)')
            if radiobtn_places[i]:
                eval(f'set{i}.place(x={radiobtn_places[i][0]} * kx, y={radiobtn_places[i][1]} * 1)')
        btn_exit.place(x=window.winfo_width() - 70, y=window.winfo_height() - 60)
        btn_col_bg.place(x=170, y=window.winfo_height() - 60)

        del_with_tag('color')
        del_with_tag('color1')

        resized_coords = []
        resized_coords1 = []
        for i in range(len(color_coords)):
            resized_coords.append([color_coords[i][0], color_coords[i][1]])
            resized_coords[i][0] *= kx
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

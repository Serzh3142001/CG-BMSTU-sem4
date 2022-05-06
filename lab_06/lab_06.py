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

var = IntVar()
# method = IntVar()
story = []
win_size = [700, 900]
c = Canvas(window, width=3840, height=2160, bg='white')

ent1 = Entry(width=7)
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
# btn_hist = Button(window, text='Время', fg='green', command=lambda: fillWithDelay())
btn_back = Button(window, text='назад', fg='purple', command=lambda: back())
btn_cl_all = Button(window, text='🗑заново', fg='orange', command=lambda: start_state())
btn_draw_circle = Button(window, text='Закрасить', fg='green', command=lambda: fillTriger())
btn_draw_ellipse = Button(window, text='Замкнуть', fg='blue', command=lambda: close())
btn_delay = Button(window, text='>>', fg='green', command=lambda: unDelay())
# btn_draw_ellipse_bunch = Button(window, text='🎨⬯⬯', fg='blue', command=lambda: draw_ellipse_bunch(TAG))
btn_colorimeter = Button(window, text='🔍', fg='blue', command=lambda: os.system('open /System/Applications/Utilities/Digital\ Color\ Meter.app'))
btn_exit = Button(window, text=' выход ', fg='red', command=exit)

set0 = Radiobutton(text="Мгновенно", fg='black', variable=var, value=0)
set1 = Radiobutton(text="С задержкой", fg='black', variable=var, value=1)

# set2 = Radiobutton(text="default", fg='black', variable=method, value=0)
# set3 = Radiobutton(text="Каноническое ур-е", fg='black', variable=method, value=1)
# set4 = Radiobutton(text="Параметрическое ур-е", fg='black', variable=method, value=2)
# set5 = Radiobutton(text="Брезенхем", fg='black', variable=method, value=3)
# set6 = Radiobutton(text="Средней точки", fg='black', variable=method, value=4)
# set7 = Radiobutton(text="ВУ", fg='black', variable=method, value=5)
# set1 = Radiobutton(text="➚", fg='black', variable=var, value=1)

var.set(0)
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

ents = '''ent1.place(x=250, y=30)'''

lbls = '''label6.place(x=5, y=133)
label18.place(x=160, y=178)'''

btns = '''btn_col_line.place(x=135, y=133)
btn_back.place(x=116, y=175)
btn_colorimeter.place(x=100, y=80)
btn_exit.place(x=630, y=840)
btn_draw_circle.place(x=15, y=20)
btn_draw_ellipse.place(x=15, y=80)
btn_cl_all.place(x=15, y=175)'''

rbtns = '''set0.place(x=100, y=20):1
set1.place(x=100, y=50):1'''

TASK = '''
Необходимо обеспечить ввод произвольной многоугольной области, содержащей произвольное количество отверстий. Ввод (вершин многоугольника) производить с помощью мыши, при этом для удобства пользователя должны отображаться ребра, соединяющие вводимые вершины. Предусмотреть ввод горизонтальных и вертикальных ребер. Должен быть предусмотрен ввод затравочной точки. Пользователь должен иметь возможность задания цвета заполнения.
Работа программы должна предусматривать два режима – с задержкой и без задержки.
Режим с задержкой должен позволить проследить выполняемую последовательность действий.
(Задержку целесообразно выполнять после обработки очередной строки).
Обеспечить замер времени выполнения алгоритма (без задержки, с выводом на экран только окончательного результата).
'''
AUTHOR = '\n\nНиколаев Сергей ИУ7-44Б'
sz = 1
center = [365, 510]
dx = 0
dy = 0
color_coords = (98, 135), (98, 153), (149, 153), (149, 135)
resized_coords = [[89, 135], [89, 153], [139, 153], [139, 135]]
colorDraw = [(255, 0, 0), '#0000ff']

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
TIME_LINE_FLAG = 0
DOTS = [[]]
PIXELCOLORS = []
PIXELOBJS = []
# bufPIXELOBJS = [[[] for _ in range(2560)] for _ in range(1354)]
DROWEDSTARTS = []
DICT = {}
BORDERCOLOR = 'black'


OLDTAG = 0
OLDY = 0
SAVEFLAG = 1
FILLFLAG = 0


def draw_dot(x, y, colorr, tag, lineFl=False):
    global OLDTAG, OLDY, SAVEFLAG, PIXELOBJS
    # OLDTAG = tag
    if TIME_FLAG and TIME_LINE_FLAG:
        c.update()
        # window.mainloop()

    if type(x) == list:
        y = x[1]
        x = x[0]

    # if colorr == colorBG[1] and len(PIXELOBJS[x][y]):
    #     c.delete(PIXELOBJS[x][y][-1])
    #     PIXELOBJS[x][y].pop()
    # else:
    d = 1
    obj = c.create_polygon([x, y], [x, y + d], [x + d, y + d], [x + d, y], fill=colorr, tag=f"t{tag}")
        # if not lineFl:
        #     PIXELOBJS[x][y].append(obj)
        # print(c.coords(obj))
    return obj


def redraw_elems():
    return
    global PIXELOBJS, PIXELCOLORS
    sleep(1)

    for i in range(len(PIXELOBJS)):
        for j in range(len(PIXELOBJS[0])):
            # c.delete(PIXELOBJS[i][j])
            if PIXELOBJS[i][j]:
                c.itemconfigure(PIXELOBJS[i][j], state='hidden')
                ii, jj = net_to_canv(canv_to_net(i, j))
                PIXELCOLORS[i][j], PIXELCOLORS[ii][jj] = PIXELCOLORS[ii][jj], PIXELCOLORS[i][j]
                PIXELOBJS[i][j] = []
                PIXELOBJS[ii][jj] = draw_dot(ii,  jj)
                c.itemconfigure(PIXELOBJS[i][j], state='normal')
            # if PIXELOBJS[i][j] and PIXELOBJS[i][j][0] == tag:
            #     PIXELCOLORS[i][j] = colorBG[1]
            #     PIXELOBJS[i][j] = []

    # del_with_tag('start')
    # del_with_tag('stop')
    # global TAG
    # for i in range(TAG):
    #     del_with_tag(f't{i}')
    # for line in lines:
    #     br_int_draw(line[0], line[1], line[2], line[3])
    # for ellipse in ellipses:
    #     draw_ellipse(ellipse[0], ellipse[1], ellipse[2], ellipse[3], ellipse[4], False, 0)
    # for bunch in circle_bunches:
    #     draw_circle_bunch(bunch[0], bunch[1], bunch[2], bunch[3], bunch[4], bunch[5], 0)
    # for bunch in ellipse_bunches:
    #     draw_ellipse_bunch(bunch[0], bunch[1], bunch[2], bunch[3], bunch[4], bunch[5], 0)


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


def unDelay():
    global TIME_FLAG, TIME_LINE_FLAG
    if not TIME_FLAG:
        TIME_LINE_FLAG = 0
        btn_delay.place(x=-100, y=80)
        var.set(0)

    TIME_FLAG = 0



def br_int_draw(start, stop, colorr, tag, count_fl=False):
    global PIXELOBJS
    x0, y0 = list(map(round, start))
    x1, y1 = list(map(round, stop))
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
            PIXELCOLORS[x][y] = BORDERCOLOR
            PIXELOBJS[x][y] = [tag, draw_dot(x, y, colorr, tag, count_fl)]
            error += deltaerr
            if error >= dx + 1:
                y += diry
                error -= (dx + 1)
    else:
        for y in range(y0, y1):
            PIXELCOLORS[x][y] = BORDERCOLOR
            PIXELOBJS[x][y] = [tag, draw_dot(x, y, colorr, tag, count_fl)]
            error += deltaerr1
            if error >= dy + 1:
                x += dirx
                error -= (dy + 1)


def close(event=None):
    global TAG, DOTS
    br_int_draw(DOTS[-1][0], DOTS[-1][-1], BORDERCOLOR, TAG)
    lines.append([DOTS[-1][0], DOTS[-1][-1], BORDERCOLOR, TAG])
    story.append(f'del_with_tag("t{TAG}");DOTS.pop();delObjs({TAG})')
    TAG += 1
    DOTS.append([])


def fillTriger():
    global FILLFLAG
    FILLFLAG = 1

def fillProcess(start, st=1, dir=2):
    global DOTS, TAG, colorDraw, story, PIXELCOLORS, TIME_FLAG, FILLFLAG, TIME_LINE_FLAG, PIXELOBJS
    startTime = time()
    FILLFLAG = 0

    if st:
        if var.get():
            btn_delay.place(x=65, y=50)
            TIME_FLAG = 1
            TIME_LINE_FLAG = 1
        else:
            TIME_FLAG = 0
            TIME_LINE_FLAG = 0

    xl = xr = start[0]
    y = start[1]
    while PIXELCOLORS[xl][y] != BORDERCOLOR or PIXELCOLORS[xr][y] != BORDERCOLOR:
        if xl < 65 or xr > 665 + dx:
            box.showinfo('Error', 'Затравка вне замкнутой области!')
            DOTS.append([])
            return
        if PIXELCOLORS[xl][y] != BORDERCOLOR:
            PIXELOBJS[xl][y] = [TAG, draw_dot(xl, y, colorDraw[1], TAG)]
            PIXELCOLORS[xl][y] = colorDraw[1]
            xl -= 1
        if PIXELCOLORS[xr][y] != BORDERCOLOR:
            PIXELOBJS[xr][y] = [TAG, draw_dot(xr, y, colorDraw[1], TAG)]
            PIXELCOLORS[xr][y] = colorDraw[1]
            xr += 1
    if TIME_LINE_FLAG:
        c.update()
    xl += 1

    # if dir == 1 or dir == 2:
    for x in range(xl, xr):
        if (x == xr-1 or x != xl and PIXELCOLORS[x][y-1] == BORDERCOLOR and PIXELCOLORS[x-1][y-1] != BORDERCOLOR) and PIXELCOLORS[x-1][y-1] != colorDraw[1] and xr-xl != 1:
            fillProcess([x-1, y-1], 0, 1)

    # if dir == 0 or dir == 2:
    for x in range(xl, xr):
        if (x == xr-1 or x != xl and PIXELCOLORS[x][y+1] == BORDERCOLOR and PIXELCOLORS[x-1][y+1] != BORDERCOLOR) and PIXELCOLORS[x-1][y+1] != colorDraw[1] and xr-xl != 1:
            fillProcess([x-1, y+1], 0, 0)


    # PIXELCOLORS = [[colorBG[1] for _ in range(2560)] for _ in range(1354)]

    if st:
        story[-1] += f';del_with_tag("t{TAG}");DOTS.pop();delObjs({TAG})'
        TAG += 1
        DOTS.append([])
        stop = time()
        ent1.delete(0, END)
        ent1.insert(0, f't = {round(stop - startTime, 2)}"')
        btn_delay.place(x=-100, y=50)


def resetPixels():
    global PIXELCOLORS
    PIXELCOLORS = [[colorBG[1] for _ in range(1354)] for _ in range(2560)]


def delObjs(tag):
    global PIXELOBJS, PIXELCOLORS
    for i in range(len(PIXELOBJS)):
        for j in range(len(PIXELOBJS[0])):
            if PIXELOBJS[i][j] and PIXELOBJS[i][j][0] == tag:
                PIXELCOLORS[i][j] = colorBG[1]
                PIXELOBJS[i][j] = []


def click(event):
    global TAG, DOTS, TIME_FLAG, FILLFLAG

    bufTimeFl = TIME_FLAG
    TIME_FLAG = 0

    if FILLFLAG:
        event.y -= 10
        print_dot(event)
        fillProcess([event.x, event.y])
        return

    # for dot in DOTS[-1]:
    #     if is_cursor_touch_dot(dot, event):
    #         DOTS[-1].append(dot)
    #         br_int_draw(DOTS[-1][-2], DOTS[-1][-1], BORDERCOLOR, TAG)
    #
    #         dotts = c.find_withtag('dot')
    #         story.append(f'c.delete({dotts[-1]});DOTS[-1].pop()')
    #
    #         crds = event.x, event.y
    #         DOTS[-1].append(crds)
    #         if len(DOTS[-1]) > 1:
    #             br_int_draw(DOTS[-1][-2], DOTS[-1][-1], BORDERCOLOR, TAG)
    #             lines.append([DOTS[-1][-2], DOTS[-1][-1], BORDERCOLOR, TAG])
    #             story[-1] += f';del_with_tag("t{TAG}");lines.pop();delObjs({TAG})'
    #
    #         TAG += 1
    #         return

    if event.x < 65 or event.x > 665 + dx or event.y < 210 or event.y > 810 + dy:
        return

    # print(PIXELCOLORS[event.x][event.y])
    print(event.x, event.y)
    for i in range(event.x-1, event.x+2):
        for j in range(event.y - 1, event.y + 2):
            PIXELCOLORS[i][j] = BORDERCOLOR
    print_dot(event)

    dotts = c.find_withtag('dot')
    story.append(f'c.delete({dotts[-1]});DOTS[-1].pop();delDotPixels({[event.x, event.y]})')

    crds = event.x, event.y
    DOTS[-1].append(crds)
    if len(DOTS[-1]) > 1:
        br_int_draw(DOTS[-1][-2], DOTS[-1][-1], BORDERCOLOR, TAG)
        lines.append([DOTS[-1][-2], DOTS[-1][-1], BORDERCOLOR, TAG])
        story[-1] += f';del_with_tag("t{TAG}");lines.pop();delObjs({TAG})'
        TAG += 1

    TIME_FLAG = bufTimeFl

def delDotPixels(coords):
    x, y = coords
    for i in range(x-1, x+2):
        for j in range(y - 1, y + 2):
            PIXELCOLORS[i][j] = colorBG

def motion(event):
    x, y = event.x, event.y
    if x < 65 or x > 665 + dx or y < 210 or y > 810 + dy:
        return

    del_with_tag('pointer')

    if FILLFLAG:
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        # if var.get():
        #     c.create_oval(x1, y1, x2, y2, outline='blue', fill='blue', tag='dot', activeoutline='lightgreen', activefill='lightgreen')
        # else:
        c.create_oval(x1, y1-10, x2, y2-10, outline='red', fill='red', tag='pointer', activeoutline='lightgreen',
                      activefill='lightgreen')
        c.create_line(x-10, y-10, x-5, y-10, fill='green', width=1, tag='pointer')
        c.create_line(x + 5, y-10, x + 10, y-10, fill='green', width=1, tag='pointer')
        c.create_line(x, y - 20, x, y - 15, fill='green', width=1, tag='pointer')
        c.create_line(x, y, x, y - 5, fill='green', width=1, tag='pointer')
        # c.create_polygon([x, y-10], [x, y + 1-10], [x + 1, y + 1-10], [x + 1, y-10], fill=colorDraw[1], tag='pointer')



def print_dot(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    # if var.get():
    #     c.create_oval(x1, y1, x2, y2, outline='blue', fill='blue', tag='dot', activeoutline='lightgreen', activefill='lightgreen')
    # else:
    if FILLFLAG:
        dot = c.create_oval(x1, y1, x2, y2, outline='red', fill='red', tag='dot', activeoutline='lightgreen',
                      activefill='lightgreen')
        story.append(f'c.delete({dot})')
        return
    c.create_oval(x1, y1, x2, y2, outline=BORDERCOLOR, fill=BORDERCOLOR, tag='dot', activeoutline='lightgreen', activefill='lightgreen')

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
    global PIXELCOLORS
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
    global story, rot_coords, res_coords, lines, circles, circle_bunches, TAG, ellipses, circle_bunches, ellipse_bunches, DOTS, PIXELOBJS, PIXELCOLORS, colorBG
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
    del_with_tag('dot')
    TAG = 0
    # TIME_FLAG = 0
    DOTS = [[]]
    lines = []
    PIXELCOLORS = [[colorBG[1] for _ in range(1354)] for _ in range(2560)]
    PIXELOBJS = [[[] for _ in range(1354)] for _ in range(2650)]
    colorBG = [(254.9921875, 255.99609375, 255.99609375), '#feffff']
    coordinate_field_creation()

    # bufPIXELOBJS = [[[] for _ in range(2560)] for _ in range(1354)]
    ent1.delete(0, END)
    ent1.insert(0, 't = ')
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

        # if 'set' in ents:
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
window.bind("<Button-2>", close)
window.bind("<Motion>", motion)


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

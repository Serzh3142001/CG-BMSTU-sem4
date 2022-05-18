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
story = []
win_size = [700, 900]
c = Canvas(window, width=3840, height=2160, bg='white')

ent1 = Entry(width=3)
ent2 = Entry(width=3)
ent3 = Entry(width=3)
ent4 = Entry(width=3)
ent5 = Entry(width=3)
ent6 = Entry(width=3)
ent7 = Entry(width=3)
ent8 = Entry(width=3)
ent1.insert(0, -160)
ent2.insert(0, 100)
ent3.insert(0, -200)
ent4.insert(0, 150)
ent5.insert(0, 150)
ent6.insert(0, -200)
ent7.insert(0, 250)
ent8.insert(0, -250)

label6 = Label(text='  Цвет:', font='Arial 15')
label18 = Label(text='⌘Z', font='Arial 11', fg='orange')
label19 = Label(text='x:', font='Arial 11', fg='grey')
label20 = Label(text='y:', font='Arial 11', fg='grey')
label23 = Label(text='Цвет фона:', font='Arial 15')


btn_col_line = Button(window, text='v', fg='green', command=lambda: line_col_choose())
btn_col_bg = Button(window, text='v', fg='green', command=lambda: bg_col_choose())
btn_back = Button(window, text='назад', fg='purple', command=lambda: back())
btn_cl_all = Button(window, text='🗑заново', fg='orange', command=lambda: start_state())
btn_draw_ellipse = Button(window, text='замкнуть', fg='blue', command=lambda: close())
btn_colorimeter = Button(window, text='🔍', fg='blue', command=lambda: os.system('open /System/Applications/Utilities/Digital\ Color\ Meter.app'))
btn_exit = Button(window, text=' выход ', fg='red', command=exit)

set0 = Radiobutton(text="Мгновенно", fg='black', variable=var, value=0)
set1 = Radiobutton(text="С задержкой", fg='black', variable=var, value=1)

var.set(0)

ents = ''''''

lbls = '''label6.place(x=5, y=133)
label18.place(x=160, y=178)'''

btns = '''btn_col_line.place(x=135, y=133)
btn_back.place(x=116, y=175)
btn_colorimeter.place(x=100, y=80)
btn_exit.place(x=630, y=840)
btn_draw_ellipse.place(x=15, y=80)
btn_cl_all.place(x=15, y=175)'''

rbtns = ''''''

TASK = '''
Реализовать отсечение отрезков выпуклым многоугольным отсекателем.
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
DOTS = []
PIXELCOLORS = []
PIXELOBJS = []
# bufPIXELOBJS = [[[] for _ in range(2560)] for _ in range(1354)]
DROWEDSTARTS = []
DICT = {}
BORDERCOLOR = 'black'


OLDTAG = 0
OLDY = 0
SAVEFLAG = 1
CUTTERFLAG = 2
LINEFLAG = 0
redrawCommands = []


def redraw_elems():
    start_state()


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


def clean_coords():
    coords = c.find_withtag('coord')
    for cor in coords:
        c.delete(cor)

    net = c.find_withtag('net')
    for n in net:
        c.delete(n)


def del_with_tag(tag, pos=0):
    for obj in c.find_withtag(tag):
        c.delete(obj)


CUTTERENDEDITING = 0
def close(event=None):
    global TAG, DOTS, CUTTERENDEDITING
    if not isCutterConvex(DOTS):
        box.showinfo('Error', 'Отсекатель невыпуклый!')
        start_state()
        return

    del_with_tag('lineHelper')

    print('DOOOTS:', DOTS[0], DOTS[1])
    c.create_line(DOTS[0], DOTS[-1], fill='red', width=2, tag=f'line{TAG}')
    redrawCommands.append(
        f'c.create_line(net_to_canv({canv_to_net(DOTS[0])}), net_to_canv({canv_to_net(DOTS[-1])}), fill=\'red\', width=2, tag=f\'line{TAG}\')')
    story.append(f'del_with_tag("line{TAG}")')
    TAG += 1
    CUTTERENDEDITING = 1


def get_vect(dot_start, dot_end):
    return [dot_end[0] - dot_start[0], dot_end[1] - dot_start[1]]


def get_vect_mul(fvector, svector):
    return fvector[0] * svector[1] - fvector[1] * svector[0]


def get_scalar_mul(fvector, svector):
    return fvector[0] * svector[0] + fvector[1] * svector[1]


def get_normal(dot_start, dot_end, dot_check):
    vect = get_vect(dot_start, dot_end)
    normal = None

    if vect[0] == 0:
        normal = [1, 0]
    else:
        normal = [-vect[1] / vect[0], 1]

    if get_scalar_mul(get_vect(dot_end, dot_check), normal) < 0:
        for i in range(len(normal)):
            normal[i] = -normal[i]

    return normal


def get_normals(cut):
    normals = []
    cutlen = len(cut)

    for i in range(cutlen):
        normals.append(get_normal(cut[i], cut[(i + 1) % cutlen], cut[(i + 2) % cutlen]))

    return normals


def cyrusbeck(cut, line, normals):
    t_start = 0
    t_end = 1

    vect = get_vect(line[0], line[1])
    cutlen = len(cut)

    for i in range(cutlen):
        w_vect = get_vect(cut[(i + 1) % cutlen], line[0])
        if cut[i] != line[0]:
            w_vect = get_vect(cut[i], line[0])

        vect_scal = get_scalar_mul(vect, normals[i])
        w_vect_scal = get_scalar_mul(w_vect, normals[i])

        if vect_scal == 0:
            if w_vect_scal < 0:
                return
            continue

        t = -w_vect_scal / vect_scal
        if vect_scal > 0:
            if t > t_start:
                t_start = t
        else:
            if t < t_end:
                t_end = t

        if t_start > t_end:
            break

    if t_start < t_end:
        dot_start = [round(line[0][0] + vect[0] * t_start),
                     round(line[0][1] + vect[1] * t_start)]
        dot_end = [round(line[0][0] + vect[0] * t_end),
                   round(line[0][1] + vect[1] * t_end)]
        c.create_line(dot_start, dot_end, fill=colorDraw[1], width=3, tag=f'line{TAG}')
        print(f'DB: cyrus tag = {TAG}')


def isCutterConvex(cutter):
    PosAngle = False
    NegAngle = False
    for i in range(len(cutter)):
        x1 = cutter[i][0]
        y1 = cutter[i][1]
        x2 = cutter[(i + 1)%len(cutter)][0]
        y2 = cutter[(i + 1) % len(cutter)][1]
        x3 = cutter[(i + 2) % len(cutter)][0]
        y3 = cutter[(i + 2) % len(cutter)][1]
        d = (x2-x1)*(y3-y2)-(y2-y1)*(x3-x2)
        if d > 0:
            PosAngle = True
        elif d < 0:
            NegAngle = True

    if PosAngle and NegAngle:
        return False
    else:
        return True


CUTTER_END = []
def click(event):
    global defCoords, SHIFTFLAG, TAG, DOTS, TIME_FLAG, FILLFLAG, CUTTERFLAG, CUTTER_START, LINEFLAG, LINE_START, CUTTER_END

    if event.x < 65 or event.x > 665 + dx or event.y < 210 or event.y > 810 + dy:
        return

    if not CUTTERENDEDITING:
        DOTS.append([event.x, event.y-10])
        del_with_tag('lineHelper')

        if SHIFTFLAG:
            if abs(DOTS[-2][0] - event.x) < abs(DOTS[-2][1] - event.y + 10):
                DOTS[-1][0] = DOTS[-2][0]
            else:
                DOTS[-1][1] = DOTS[-2][1]

        if len(DOTS) > 1:
            c.create_line(DOTS[-2], DOTS[-1], fill='red', width=2, tag=f'line{TAG}')
            story.append(f'DOTS.pop();del_with_tag("line{TAG}")')
            TAG += 1
    else:
        LINEFLAG += 1
        if LINEFLAG % 2:
            LINE_START = [event.x, event.y - 10]
        elif LINEFLAG > 1:
            del_with_tag('lineHelper')
            LINE_END = [event.x, event.y - 10]

            if SHIFTFLAG:
                if abs(LINE_START[0] - event.x) < abs(LINE_START[1] - event.y + 10):
                    LINE_END = [LINE_START[0], event.y - 10]
                else:
                    LINE_END[1] = LINE_START[1]

            obj = c.create_line(LINE_START, LINE_END, fill='black', width=1, dash=(7, 9), tag=f'line{TAG}')
            print(f'DB: line tag = {TAG}')
            cyrusbeck(DOTS, [LINE_START, LINE_END], get_normals(DOTS))
            story.append(f'del_with_tag("line{TAG}")')

            TAG += 1

    print(event.x, event.y)
    SHIFTFLAG = 0


CUTTER_START = []
LINE_START = []
SHIFTFLAG = 0
def motion(event, fl=0):
    global SHIFTFLAG
    SHIFTFLAG = fl
    x, y = event.x, event.y
    if x < 65 or x > 665 + dx or y < 210 or y > 810 + dy:
        return

    del_with_tag('lineHelper')
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    c.create_oval(x1, y1 - 10, x2, y2 - 10, outline='red', fill='red', tag='lineHelper',
                  activeoutline='lightgreen',
                  activefill='lightgreen')
    c.create_line(x - 10, y - 10, x - 5, y - 10, fill='green', width=1, tag='lineHelper')
    c.create_line(x + 5, y - 10, x + 10, y - 10, fill='green', width=1, tag='lineHelper')
    c.create_line(x, y - 20, x, y - 15, fill='green', width=1, tag='lineHelper')
    c.create_line(x, y, x, y - 5, fill='green', width=1, tag='lineHelper')

    if not CUTTERENDEDITING and len(DOTS):
        if not fl:
            c.create_line(DOTS[-1], x, y-10, fill='black', width=1, dash=(7, 9), tag='lineHelper')
        else:
            if abs(DOTS[-1][0] - x) < abs(DOTS[-1][1] - y + 10):
                x = DOTS[-1][0]
                y -= 10
            else:
                y = DOTS[-1][1]
            c.create_line(DOTS[-1], x, y, fill='black', width=1, dash=(7, 9), tag='lineHelper')

    elif LINEFLAG:
        if LINEFLAG % 2:
            if not fl:
                c.create_line(LINE_START, x, y-10, fill='black', width=1, dash=(7, 9), tag='lineHelper')
            else:
                if abs(LINE_START[0] - x) < abs(LINE_START[1] - y + 10):
                    x = LINE_START[0]
                    y -= 10
                else:
                    y = LINE_START[1]
                c.create_line(LINE_START, x, y, fill='black', width=1, dash=(7, 9), tag='lineHelper')


def motionWithShift(event):
    motion(event, 1)


def back():
    global LINEFLAG, CUTTERFLAG, redrawCommands
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
    global DOTS, CUTTERENDEDITING, redrawCommands, LINEFLAG, CUTTERFLAG, story, rot_coords, res_coords, lines, circles, circle_bunches, TAG, ellipses, circle_bunches, ellipse_bunches, DOTS, PIXELOBJS, PIXELCOLORS, colorBG
    scale(290, 290)
    CUTTERENDEDITING = 0

    story = ['start_state()']
    DOTS = []
    redrawCommands = []
    clean_all()
    CUTTERFLAG = 2

    LINEFLAG = 0
    coordinate_field_creation()


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
        if rbtns:
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
window.bind("<Command-r>", exit)
window.bind("<Configure>", config)
window.bind("<Button-2>", close)
window.bind("<Motion>", motion)
window.bind("<Shift-Motion>", motionWithShift)


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

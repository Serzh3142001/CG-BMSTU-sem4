from math import *
from tkinter import *
import tkinter.messagebox as box
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()

var = IntVar()
story = []
win_size = [700, 900]
c = Canvas(window, width=win_size[0], height=win_size[1], bg='white')
res_coords = []
rot_coords = []
cnt_res_clc = 0
cnt_rot_clc = 0

ent1 = Entry(width=8)
ent2 = Entry(width=8)
ent3 = Entry(width=8)
ent4 = Entry(width=8)
ent5 = Entry(width=8)
ent6 = Entry(width=8)
ent7 = Entry(width=8)
ent1.place(x=70, y=40)
ent2.place(x=320, y=40)
ent3.place(x=320, y=80)
ent4.place(x=570, y=40)
ent5.place(x=570, y=80)
ent6.place(x=320, y=110)
ent7.place(x=570, y=110)
ent1.insert(0, 15)
ent2.insert(0, 5)
ent3.insert(0, 0)
ent4.insert(0, 5)
ent5.insert(0, 0)
ent6.insert(0, 0)
ent7.insert(0, 0)

label1 = Label(text='Смещение:', font='Arial 15')
label1.place(x=60, y=5)
label2 = Label(text='Масштабирование:', font='Arial 15')
label2.place(x=280, y=5)
label3 = Label(text='Поворот:', font='Arial 15')
label3.place(x=535, y=5)

label4 = Label(text='На:', font='Arial 15')
label5 = Label(text='На:', font='Arial 15')
label6 = Label(text='X:', font='Arial 15')
label7 = Label(text='Y:', font='Arial 15')
label8 = Label(text='X:', font='Arial 15')
label9 = Label(text='Y:', font='Arial 15')
label10 = Label(text='Относ.\nточки:', font='Arial 13')
label11 = Label(text='На:', font='Arial 15')
label12 = Label(text='Относ.\nточки:', font='Arial 13')
label13 = Label(text='%', font='Arial 15')
label14 = Label(text='°', font='Arial 17')

btn_rot_r = Button(window, text='↻', fg='green', command=lambda: rotate_fox(fox_coords, ent4.get(),
                                                                                net_to_canv(ent5.get(),
                                                                                            ent7.get())))
btn_rot_l = Button(window, text='↺', fg='green', command=lambda: rotate_fox(fox_coords, '-'+ent4.get(),
                                                                            net_to_canv(ent5.get(),
                                                                                        ent7.get())))
btn_res_r = Button(window, text='▲', fg='green', command=lambda: resize_fox(fox_coords, ent2.get(),
                                                                           net_to_canv(ent3.get(),
                                                                                       ent6.get())))
btn_res_l = Button(window, text='▼', fg='green', command=lambda: resize_fox(fox_coords, '-' + ent2.get(),
                                                                           net_to_canv(ent3.get(),
                                                                                       ent6.get())))
btn_mv_r = Button(window, text='▶', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'right'))
btn_mv_l = Button(window, text='◀', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'left'))
btn_mv_u = Button(window, text='▲', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'up'))
btn_mv_d = Button(window, text='▼', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'down'))
btn_back = Button(window, text='назад', fg='purple', command=lambda: back())
btn_cl_all = Button(window, text='🗑заново', fg='orange', command=lambda: start_state())
btn_exit = Button(window, text=' выход ', fg='red', command=exit)

set0 = Radiobutton(text="➚", fg='black', variable=var, value=0)
set1 = Radiobutton(text="➚", fg='black', variable=var, value=1)

ents = '''ent1.place(x=70, y=40)
ent2.place(x=320, y=40)
ent3.place(x=320, y=80)
ent4.place(x=570, y=40)
ent5.place(x=570, y=80)
ent6.place(x=320, y=110)
ent7.place(x=570, y=110)'''

lbls = '''label1.place(x=60, y=5)
label2.place(x=280, y=5)
label3.place(x=535, y=5)
label4.place(x=35, y=43)
label5.place(x=285, y=43)
label6.place(x=295, y=82)
label7.place(x=295, y=112)
label8.place(x=545, y=82)
label9.place(x=545, y=112)
label10.place(x=491, y=90)
label11.place(x=535, y=43)
label12.place(x=241, y=90)
label13.place(x=403, y=42)
label14.place(x=653, y=42)'''

btns = '''btn_res_l.place(x=330, y=150)
btn_res_r.place(x=360, y=150)
btn_mv_r.place(x=125, y=110)
btn_mv_l.place(x=85, y=110)
btn_mv_u.place(x=105, y=90)
btn_mv_d.place(x=105, y=130)
btn_cl_all.place(x=25, y=170)
btn_rot_r.place(x=620, y=150)
btn_rot_l.place(x=590, y=150)
btn_back.place(x=25, y=140)
btn_exit.place(x=630, y=840)'''

rbtns = '''set0.place(x=405, y=97)
set1.place(x=655, y=97)'''




TASK = 'Вариант 13:\nНарисовать исходный рисунок, затем его переместить, промасштабировать, повернуть'
AUTHOR = '\n\nНиколаев Сергей ИУ7-44Б'
sz = 1
resize_point = [0, 0]
rotate_point = [0, 0]

def cart_sum(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cart_dif(a, b):
    return (a[0] - b[0], a[1] - b[1])


def rotate(a, alpha, center):
    a = cart_dif(a, center)
    res = (cos(alpha) * a[0] - sin(alpha) * a[1],
           sin(alpha) * a[0] + cos(alpha) * a[1])
    res = cart_sum(res, center)
    return res

def resize(a, k, center):
    a = cart_dif(a, center)
    res = (a[0]*k, a[1]*k)
    res = cart_sum(res, center)
    return res


def clean_tri():
    triangls = c.find_withtag('triang')
    for tri in triangls:
        c.delete(tri)

def rotate_fox(dots, alpha, center, st=1):
    try:
        alpha = radians(float(alpha))
    except:
        box.showinfo('Error', 'Некорректное значение угла поворота!')
        return

    try:
        x, y = float(ent5.get()), float(ent7.get())
    except:
        box.showinfo('Error', 'Некорректные координаты!')
        return

    if st:
        story.append(f'rotate_fox(fox_coords, {-degrees(alpha)}, {center}, 0)')

    global fox_coords, rotate_point

    reprint_dot([x, y], 2)
    rotate_point = [x, y]

    rotated_dots = []
    for dot in dots:
        rotated_dots.append(rotate(dot, alpha, center))

    fox = c.find_withtag('fox')
    for elem in fox:
        c.delete(elem)

    fox_coords = rotated_dots
    analyze_and_redraw()
    draw_fox(fox_coords)

def resize_fox(dots, k, center, st=1):
    try:
        k = float(k)/100 + 1
    except:
        box.showinfo('Error', 'Некорректное значение процента масштабирования!')
        return

    try:
        x, y = float(ent3.get()), float(ent6.get())
    except:
        box.showinfo('Error', 'Некорректные координаты!')
        return

    if st:
        story.append(f'resize_fox(fox_coords, {-(k - 1)*100}, {center}, 0)')

    global fox_coords, resize_point

    reprint_dot([x, y], 1)
    resize_point = [x, y]

    resized_dots = []
    for dot in dots:
        resized_dots.append(resize(dot, k, center))

    fox = c.find_withtag('fox')
    for elem in fox:
        c.delete(elem)

    fox_coords = resized_dots
    analyze_and_redraw()
    draw_fox(fox_coords)


def move_fox(dots, delta, dir, st=1):
    global sz
    try:
        delta = float(delta)/sz
    except:
        box.showinfo('Error', 'Некорректное значение процента масштабирования!')
        return

    if st:
        story.append(f'move_fox(fox_coords, {-delta*sz}, "{dir}", 0)')

    global fox_coords
    moved_dots = []
    for dot in dots:
        if dir == 'up':
            moved_dots.append([dot[0], dot[1] - delta])
        elif dir == 'down':
            moved_dots.append([dot[0], dot[1] + delta])
        elif dir == 'left':
            moved_dots.append([dot[0] - delta, dot[1]])
        elif dir == 'right':
            moved_dots.append([dot[0] + delta, dot[1]])

    fox = c.find_withtag('fox')
    for elem in fox:
        c.delete(elem)

    fox_coords = moved_dots
    analyze_and_redraw()
    draw_fox(fox_coords)


def resize_dots(dots, k, center):
    global fox_coords

    resized_dots = []
    for dot in dots:
        resized_dots.append(resize(dot, k, center))

    fox_coords = resized_dots

def analyze_and_redraw():
    global fox_coords, sz
    max_coord = 0

    for dot in fox_coords:
        dot = canv_to_net(dot[0], dot[1])
        if max(abs(dot[0]), abs(dot[1])) > max_coord:
            max_coord = max(abs(dot[0]), abs(dot[1]))

    try:
        max_coord = max(max_coord, abs(float(ent3.get())), abs(float(ent5.get())),
                        abs(float(ent6.get())), abs(float(ent7.get())))
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    if 150 * sz <= max_coord <= 300 * sz:
        return

    old = sz
    scale(max_coord, max_coord)
    new = sz
    resize_dots(fox_coords, old/new, net_to_canv(0, 0))
    reprint_dot([float(ent3.get()), float(ent6.get())], 1)
    reprint_dot([float(ent5.get()), float(ent7.get())], 2)


def clean_all():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)

    objs = c.find_withtag('rot')
    objs += c.find_withtag('sz')
    objs += c.find_withtag('fox')
    for obj in objs:
        c.delete(obj)


def clean_coords():
    coords = c.find_withtag('coord')
    for cor in coords:
        c.delete(cor)


def click(event):
    global res_coords, cnt_res_clc, cnt_rot_clc

    if event.x < 65 or event.x > 665 or event.y < 210 or event.y > 810:
        return

    if var.get():
        cnt_rot_clc += 1
        rot_coords.append(canv_to_net(event.x, event.y) + [var.get() + 1])
        if len(rot_coords) > 1:
            story.append(f'reprint_dot({rot_coords[-2][:-1]}, {rot_coords[-2][-1]});rot_coords.pop()')
    else:
        cnt_res_clc += 1
        res_coords.append(canv_to_net(event.x, event.y) + [var.get() + 1])
        if len(res_coords) > 1:
            story.append(f'reprint_dot({res_coords[-2][:-1]}, {res_coords[-2][-1]});res_coords.pop()')

    global rotate_point, resize_point
    if var.get():
        rotate_point = canv_to_net(event.x, event.y)
        reprint_dot(rotate_point)
    else:
        resize_point = canv_to_net(event.x, event.y)
        reprint_dot(resize_point)


def reprint_dot(coords, fl=0):
    global sz
    buf = net_to_canv(coords[0], coords[1])

    x1, y1 = (buf[0] - 2), (buf[1] - 2)
    x2, y2 = (buf[0] + 2), (buf[1] + 2)

    if (fl == 1 or not var.get()) and fl != 2:
        dotts = c.find_withtag('sz')
        for dot in dotts:
            c.delete(dot)
        ent3.delete(0, END)
        ent6.delete(0, END)
        ent3.insert(END, f'{coords[0]:g}')
        ent6.insert(END, f'{coords[1]:g}')
        c.create_oval(x1, y1, x2, y2, outline='red', fill='red', tag='sz', activeoutline='lightgreen', activefill='lightgreen')
        c.create_text(x1-5, y1 - 9, text='⇖', fill='green', tag='sz', font='Arial 20')
        c.create_text(x1 + 10, y1 - 9, text='⇗', fill='green', tag='sz', font='Arial 20')
        c.create_text(x1 - 5, y1 + 7, text='⇙', fill='green', tag='sz', font='Arial 20')
        c.create_text(x1 + 10, y1 + 7, text='⇘', fill='green', tag='sz', font='Arial 20')
    elif fl == 2 or var.get():
        dotts = c.find_withtag('rot')
        for dot in dotts:
            c.delete(dot)
        ent5.delete(0, END)
        ent7.delete(0, END)
        ent5.insert(END, f'{coords[0]:g}')
        ent7.insert(END, f'{coords[1]:g}')
        c.create_oval(x1, y1, x2, y2, outline='red', fill='red', tag='rot', activeoutline='lightgreen', activefill='lightgreen')
        c.create_text(x1 + 2, y1 - 2, text='↻', fill='green', tag='rot', font='Helvetica 40')


def net_to_canv(x, y):
    try:
        x, y = float(x), float(y)
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    global sz
    center = (365, 510)

    return [round(x/sz + center[0]), round(center[1] - y/sz)]


def canv_to_net(x, y):
    try:
        x, y = float(x), float(y)
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    global sz
    center = (365, 510)

    return [round((x - center[0])*sz, 3), round((center[1] - y)*sz, 3)]


def back():
    global res_coords, rot_coords
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
        eval(com)

    # analyze_and_redraw()
    del story[-1]


def scale(x, y):
    global sz
    prev_sz = sz
    while x > -150 * sz and x < 150 * sz and y > -150 * sz and y < 150 * sz:
        sz /= 2

    while x < -300 * sz or x > 300 * sz or y < -300 * sz or y > 300 * sz:
        sz *= 2

    if sz != prev_sz:
        redraw()


def redraw():
    global sz
    clean_coords()
    max_len = 0
    for i in range(65, 670, 50):
        if len(f'{round((i - 365)*sz, 3):g}') > max_len:
            max_len = len(f'{round((i - 365)*sz, 3):g}')

    for i in range(65, 670, 50):
        c.create_text(i, 530, fill='grey', text=f'{round((i - 365)*sz, 3):g}' if i - 365 else '', tag='coord',
                      font='Verdana 8' if max_len > 6 else 'Verdana 12')

    for i in range(210, 820, 50):
        c.create_text(345, i + 10, fill='grey', text=f'{round(-(i - 510)*sz, 3):g}' if i - 510 else '', tag='coord')


def text_and_labels_creation():
    label1.place(x=60, y=5)
    label2.place(x=280, y=5)
    label3.place(x=535, y=5)
    label4.place(x=35, y=43)
    label5.place(x=285, y=43)
    label6.place(x=295, y=82)
    label7.place(x=295, y=112)
    label8.place(x=545, y=82)
    label9.place(x=545, y=112)
    label10.place(x=491, y=90)
    label11.place(x=535, y=43)
    label12.place(x=241, y=90)
    label13.place(x=403, y=42)
    label14.place(x=653, y=42)


def buttons_creation():
    btn_res_l.place(x=330, y=150)
    btn_res_r.place(x=360, y=150)
    btn_mv_r.place(x=125, y=110)
    btn_mv_l.place(x=85, y=110)
    btn_mv_u.place(x=105, y=90)
    btn_mv_d.place(x=105, y=130)
    btn_cl_all.place(x=25, y=170)
    btn_rot_r.place(x=620, y=150)
    btn_rot_l.place(x=590, y=150)
    btn_back.place(x=25, y=140)
    btn_exit.place(x=630, y=840)


def coordinate_field_creation():
    c.create_line(33, 510, 690, 510, fill='grey',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6")
    c.create_line(365, 820, 365, 185, fill='grey',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6")
    c.create_line(665, 210, 665, 810, fill='black',
                  width=1, dash=(5, 9))
    c.create_line(65, 810, 665, 810, fill='black',
                  width=1, dash=(5, 9))
    c.create_line(65, 210, 665, 210, fill='black',
                  width=1, dash=(5, 9))
    c.create_line(65, 210, 65, 810, fill='black',
                  width=1, dash=(5, 9))
    c.create_text(355, 520, text='0')

    for i in range(65, 750, 50):
        c.create_line(i, 503, i, 520, fill='grey', width=2)
        c.create_line(i, 210, i, 810, fill='grey', width=1, dash=(1, 9))
        c.create_text(i, 530, text=f'{i - 365}' if i - 365 else '', fill='grey', tag='coord')

    for i in range(210, 820, 50):
        c.create_line(358, i, 372, i, fill='grey', width=2)
        c.create_line(65, i, 665, i, fill='grey', width=1, dash=(1, 9))
        c.create_text(345, i+10, text=f'{-(i - 510)}' if i - 510 else '', fill='grey', tag='coord')

    c.create_text(688, 498, text='X', font='Verdana 20', fill='green')
    c.create_text(380, 195, text='Y', font='Verdana 20', fill='green')


def radiobutton_creation():
    var.set(0)
    set0.place(x=405, y=97)
    set1.place(x=655, y=97)


def load_and_transf_coords(file):
    coords = []
    with open(file) as f:
        line = f.readline()
        while line:
            loc = list(map(float, line.strip('\n').strip(')').strip('(').split('; ')))
            loc = net_to_canv(loc[0], loc[1])
            coords.append(loc)
            line = f.readline()

    pol1 = [[-157, -116], [-206, -111], [-187, -157]]
    pol2 = [[177, -65], [182, -50], [188, -38], [205, -35]]
    for i in range(len(pol1)):
        pol1[i] = net_to_canv(pol1[i][0], pol1[i][1])
        coords.append(pol1[i])

    for i in range(len(pol2)):
        pol2[i] = net_to_canv(pol2[i][0], pol2[i][1])
        coords.append(pol2[i])

    return coords


def draw_fox(coords):
    c.create_line(coords[:-7], width=2, activefill='lightgreen', tag='fox')
    c.create_polygon(coords[-4:], width=2, activefill='lightgreen', tag='fox', fill='black')
    c.create_polygon(coords[-7:-4], width=2, activefill='lightgreen', tag='fox', fill='black')


def start_state():
    global story
    scale(200, 200)
    story = []
    clean_all()
    ent1.insert(0, 15)
    ent2.insert(0, 5)
    ent3.insert(0, 0)
    ent4.insert(0, 5)
    ent5.insert(0, 0)
    ent6.insert(0, 0)
    ent7.insert(0, 0)
    draw_fox(default_fox_coords)

def config(event):
    if event.widget == window:
        kx=window.winfo_width()/win_size[0]
        ky=window.winfo_height()/win_size[1]

        if kx < 0.9 or ky < 0.85:
            return

        max_elems = 20
        ent_places = [0]*max_elems
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
                eval(f'ent{i}.place(x={ent_places[i][0]} * kx, y={ent_places[i][1]} * ky)')
            if lbl_places[i]:
                eval(f'label{i}.place(x={lbl_places[i][0]} * kx, y={lbl_places[i][1]} * ky)')
            if btn_places[i]:
                eval(f'{btn_places[i][0]}.place(x={btn_places[i][1]} * kx, y={btn_places[i][2]} * ky)')
            if radiobtn_places[i]:
                eval(f'set{i}.place(x={radiobtn_places[i][0]} * kx, y={radiobtn_places[i][1]} * ky)')
        btn_exit.place(x=window.winfo_width()-70, y=window.winfo_height()-60)
        c.place(x=355*kx-365, y=210*ky-210)


c.bind('<1>', click)
window.bind("<Command-r>", lambda event: rotate_fox(fox_coords, ent4.get(), net_to_canv(ent5.get(), ent7.get())))
window.bind("<Shift-Command-r>", lambda event: rotate_fox(fox_coords, '-'+ent4.get(), net_to_canv(ent5.get(), ent7.get())))
window.bind("<Command-Up>", lambda event: resize_fox(fox_coords, ent2.get(), net_to_canv(ent3.get(), ent6.get())))
window.bind("<Command-Down>", lambda event: resize_fox(fox_coords, '-' + ent2.get(), net_to_canv(ent3.get(), ent6.get())))
window.bind("<Up>", lambda event: move_fox(fox_coords, ent1.get(), 'up'))
window.bind("<Down>", lambda event: move_fox(fox_coords, ent1.get(), 'down'))
window.bind("<Right>", lambda event: move_fox(fox_coords, ent1.get(), 'right'))
window.bind("<Left>", lambda event: move_fox(fox_coords, ent1.get(), 'left'))
window.bind("<Command-z>", lambda event: back())
window.bind("<Configure>", config)


btn_rot_r = Button(window, text='↻', fg='green', command=lambda: rotate_fox(fox_coords, ent4.get(),
                                                                                net_to_canv(ent5.get(),
                                                                                            ent7.get())))
btn_rot_l = Button(window, text='↺', fg='green', command=lambda: rotate_fox(fox_coords, '-'+ent4.get(),
                                                                            net_to_canv(ent5.get(),
                                                                                        ent7.get())))
btn_res_r = Button(window, text='▲', fg='green', command=lambda: resize_fox(fox_coords, ent2.get(),
                                                                           net_to_canv(ent3.get(),
                                                                                       ent6.get())))
btn_res_l = Button(window, text='▼', fg='green', command=lambda: resize_fox(fox_coords, '-' + ent2.get(),
                                                                           net_to_canv(ent3.get(),
                                                                                       ent6.get())))
btn_mv_r = Button(window, text='▶', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'right'))
btn_mv_l = Button(window, text='◀', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'left'))
btn_mv_u = Button(window, text='▲', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'up'))
btn_mv_d = Button(window, text='▼', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'down'))
btn_back = Button(window, text='назад', fg='purple', command=lambda: back())
btn_cl_all = Button(window, text='🗑заново', fg='orange', command=lambda: start_state())
btn_exit = Button(window, text=' выход ', fg='red', command=exit)



text_and_labels_creation()
buttons_creation()
coordinate_field_creation()
radiobutton_creation()
default_fox_coords = load_and_transf_coords('data.txt')
fox_coords = load_and_transf_coords('data.txt')
draw_fox(default_fox_coords)

mmenu = Menu(window)
add_menu = Menu(mmenu)
add_menu.add_command(label='О программе и авторе',
                     command=lambda: messagebox.showinfo('О программе и авторе', TASK + AUTHOR))
add_menu.add_command(label='Выход', command=exit)
mmenu.add_cascade(label='About', menu=add_menu)
window.config(menu=mmenu)

c.pack()
window.mainloop()

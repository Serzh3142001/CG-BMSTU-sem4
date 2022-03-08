from math import *
from tkinter import *
import tkinter.messagebox as box
from tkinter import messagebox


class Fox:
    def __init__(self, coords):
        self.coords = coords

    def upd_coords(self, d1, d2):
        for i in range(len(self.coords)):
            self.coords[i] = [self.coords[i][0] + d1, self.coords[i][1] + d2]
            # self.coords[i] = canv_to_net(self.coords[i])

    def draw(self):
        # self.upd_coords()
        for elem in c.find_withtag('fox'):
            c.delete(elem)
        c.create_line(self.coords[:-7], width=2, activefill='lightgreen', tag='fox')
        c.create_polygon(self.coords[-4:], width=2, activefill='lightgreen', tag='fox', fill='black')
        c.create_polygon(self.coords[-7:-4], width=2, activefill='lightgreen', tag='fox', fill='black')

    def rotate(self, alpha, center, st=1):
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

        global rotate_point

        reprint_dot([x, y], 2)
        if st and [x, y] != rotate_point:
            rot_coords.append([x, y] + [2])
            if len(rot_coords) > 1:
                story.append(f'reprint_dot({rot_coords[-2][:-1]}, {rot_coords[-2][-1]});rot_coords.pop()')
            else:
                story.append(f'del_with_tag("rot")' + ';rot_coords.pop()' if len(rot_coords) else '')

        rotate_point = [x, y]

        rotated_dots = []
        for dot in self.coords:
            rotated_dots.append(rotate(dot, alpha, center))

        foxx = c.find_withtag('fox')
        for elem in foxx:
            c.delete(elem)

        self.coords = rotated_dots
        self.analyze_and_redraw()

        if st:
            story.append(f'fox.rotate({-degrees(alpha)}, {net_to_canv(ent5.get(), ent7.get())}, 0)')

        self.draw()

    def resize(self, sign, k, k1, center, st=1):
        try:
            if sign == 1:
                k = float(k)
                k1 = float(k1)
            else:
                k = 1 / float(k)
                k1 = 1 / float(k1)
        except:
            box.showinfo('Error', 'Некорректное значение процента масштабирования!')
            return

        try:
            x, y = float(ent3.get()), float(ent6.get())
        except:
            box.showinfo('Error', 'Некорректные координаты!')
            return

        global resize_point, sz

        reprint_dot([x, y], 1)
        if st and [x, y] != resize_point:
            res_coords.append([x, y] + [1])
            if len(res_coords) > 1:
                story.append(f'reprint_dot({res_coords[-2][:-1]}, {res_coords[-2][-1]});res_coords.pop()')
            else:
                story.append(f'del_with_tag("sz")' + ';res_coords.pop()' if len(res_coords) else '')

        resize_point = [x, y]

        resized_dots = []
        for dot in self.coords:
            resized_dots.append(resize(dot, [k, k1], center))

        foxx = c.find_withtag('fox')
        for elem in foxx:
            c.delete(elem)

        self.coords = resized_dots
        self.analyze_and_redraw()

        if st:
            story.append(
                f'fox.resize({sign * (-1 if sign == -1 else 1)}, {1 / k}, {1 / k1}, '
                f'{net_to_canv(ent3.get(), ent6.get())}, 0)')

        self.draw()

    def move(self, delta, dir, st=1):
        global sz
        try:
            if type(delta) == list:
                delta[0] = float(delta[0]) / sz
                delta[1] = float(delta[1]) / sz
            else:
                delta = float(delta) / sz
        except:
            box.showinfo('Error', 'Некорректное значение процента масштабирования!')
            return

        if st:
            if type(delta) == list:
                story.append(f'fox.move({[-delta[0] * sz, -delta[1] * sz]}, "{dir}", 0)')
            else:
                story.append(f'fox.move({-delta * sz}, "{dir}", 0)')

        moved_dots = []
        for dot in self.coords:
            if dir == 'up':
                moved_dots.append([dot[0], dot[1] - delta])
            elif dir == 'down':
                moved_dots.append([dot[0], dot[1] + delta])
            elif dir == 'left':
                moved_dots.append([dot[0] - delta, dot[1]])
            elif dir == 'right':
                moved_dots.append([dot[0] + delta, dot[1]])
            elif dir == 'w':
                moved_dots.append([dot[0] + delta[0], dot[1] - delta[1]])

        foxx = c.find_withtag('fox')
        for elem in foxx:
            c.delete(elem)

        self.coords = moved_dots
        self.analyze_and_redraw()
        self.draw()

    def analyze_and_redraw(self):
        global sz
        max_coord_x = 0
        max_coord_y = 0

        for dot in self.coords:
            dot = canv_to_net(dot[0], dot[1])
            if abs(dot[0]) > max_coord_x:
                max_coord_x = abs(dot[0])
            if abs(dot[1]) > max_coord_y:
                max_coord_y = abs(dot[1])

        try:
            max_coord_x = max(max_coord_x, abs(float(ent3.get())), abs(float(ent5.get())))
            max_coord_y = max(max_coord_y, abs(float(ent6.get())), abs(float(ent7.get())))
        except:
            box.showinfo('Error', 'Некорректные координаты!')

        if (150 + dx) * sz <= max_coord_x <= (300 + dx) * sz and (150 + dy) * sz <= max_coord_y <= (300 + dy) * sz:
            return

        old = sz
        scale(max_coord_x, max_coord_y)
        new = sz
        self.resize_dots(old / new, net_to_canv(0, 0))
        reprint_dot([float(ent3.get()), float(ent6.get())], 1)
        reprint_dot([float(ent5.get()), float(ent7.get())], 2)

    def resize_dots(self, k, center):
        resized_dots = []
        for dot in self.coords:
            resized_dots.append(resize(dot, [k, k], center))

        self.coords = resized_dots


window = Tk()

var = IntVar()
story = []
win_size = [700, 900]
c = Canvas(window, width=3840, height=2160, bg='white')

ent1 = Entry(width=3)
ent2 = Entry(width=3)
ent3 = Entry(width=8)
ent4 = Entry(width=8)
ent5 = Entry(width=8)
ent6 = Entry(width=8)
ent7 = Entry(width=8)
ent8 = Entry(width=3)
ent9 = Entry(width=3)
ent10 = Entry(width=2)
ent1.place(x=70, y=40)
ent2.place(x=320, y=40)
ent3.place(x=320, y=80)
ent4.place(x=570, y=40)
ent5.place(x=570, y=80)
ent6.place(x=320, y=110)
ent7.place(x=570, y=110)
ent8.place(x=365, y=40)
ent9.place(x=115, y=40)
ent10.place(x=104, y=97)
ent1.insert(0, 15)
ent2.insert(0, 1.1)
ent3.insert(0, 0)
ent4.insert(0, 5)
ent5.insert(0, 0)
ent6.insert(0, 0)
ent7.insert(0, 0)
ent8.insert(0, 1.3)
ent9.insert(0, 5)
ent10.insert(0, 15)

label1 = Label(text='Смещение:', font='Arial 15')
label1.place(x=60, y=5)
label2 = Label(text='Масштабирование:', font='Arial 15')
label2.place(x=280, y=5)
label3 = Label(text='Поворот:', font='Arial 15')
label3.place(x=535, y=5)

label4 = Label(text='На:', font='Arial 15')
label5 = Label(text='В:', font='Arial 15')
label6 = Label(text='X:', font='Arial 15')
label7 = Label(text='Y:', font='Arial 15')
label8 = Label(text='X:', font='Arial 15')
label9 = Label(text='Y:', font='Arial 15')
label10 = Label(text='Относ.\nточки:', font='Arial 13')
label11 = Label(text='На:', font='Arial 15')
label12 = Label(text='Относ.\nточки:', font='Arial 13')
label13 = Label(text='раз', font='Arial 15')
label14 = Label(text='°', font='Arial 17')
label15 = Label(text='◀ ▶ ▲ ▼', font='Arial 13', fg='orange')
label16 = Label(text='⌘ ▲ ▼', font='Arial 13', fg='orange')
label17 = Label(text='⌘[⇧]R', font='Arial 13', fg='orange')
label18 = Label(text='⌘Z', font='Arial 13', fg='orange')
label19 = Label(text='x:', font='Arial 11', fg='grey')
label20 = Label(text='y:', font='Arial 11', fg='grey')
label21 = Label(text='x:', font='Arial 11', fg='grey')
label22 = Label(text='y:', font='Arial 11', fg='grey')

btn_rot_r = Button(window, text='↻', fg='green', command=lambda: fox.rotate(ent4.get(), net_to_canv(ent5.get(),
                                                                                                    ent7.get())))
btn_rot_l = Button(window, text='↺', fg='green', command=lambda: fox.rotate('-' + ent4.get(), net_to_canv(ent5.get(),
                                                                                                          ent7.get())))
btn_res_r = Button(window, text='▲', fg='green', command=lambda: fox.resize(1, ent2.get(), ent8.get(),
                                                                            net_to_canv(ent3.get(),
                                                                                        ent6.get())))
btn_res_l = Button(window, text='▼', fg='green', command=lambda: fox.resize(-1, ent2.get(), ent8.get(),
                                                                            net_to_canv(ent3.get(),
                                                                                        ent6.get())))
btn_mv = Button(window, text='move', fg='green', command=lambda: fox.move([ent1.get(), ent9.get()], 'w'))
btn_mv_r = Button(window, text='▶', fg='green', command=lambda: fox.move(ent10.get(), 'right'))
btn_mv_l = Button(window, text='◀', fg='green', command=lambda: fox.move(ent10.get(), 'left'))
btn_mv_u = Button(window, text='▲', fg='green', command=lambda: fox.move(ent10.get(), 'up'))
btn_mv_d = Button(window, text='▼', fg='green', command=lambda: fox.move(ent10.get(), 'down'))
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
ent7.place(x=570, y=110)
ent8.place(x=365, y=40)
ent9.place(x=115, y=40)
ent10.place(x=104, y=97)'''

lbls = '''label1.place(x=60, y=5)
label2.place(x=280, y=5)
label3.place(x=535, y=5)
label4.place(x=35, y=43)
label5.place(x=290, y=43)
label6.place(x=295, y=82)
label7.place(x=295, y=112)
label8.place(x=545, y=82)
label9.place(x=545, y=112)
label10.place(x=491, y=90)
label11.place(x=535, y=43)
label12.place(x=241, y=90)
label13.place(x=403, y=42)
label14.place(x=653, y=42)
label15.place(x=150, y=7)
label16.place(x=425, y=7)
label17.place(x=613, y=7)
label18.place(x=20, y=120)
label19.place(x=70, y=25)
label20.place(x=115, y=25)
label21.place(x=320, y=25)
label22.place(x=365, y=25)'''

btns = '''btn_res_l.place(x=330, y=150)
btn_res_r.place(x=360, y=150)
btn_mv_r.place(x=128, y=100)
btn_mv_l.place(x=85, y=100)
btn_mv_u.place(x=106, y=75)
btn_mv_d.place(x=106, y=125)
btn_mv.place(x=165, y=43)
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
res_coords = []
rot_coords = []
center = [365, 510]
dx = 0
dy = 0


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


def clean_all():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)
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
        ent3.delete(0, END)
        ent6.delete(0, END)
        ent2.insert(0, 5)
        ent3.insert(0, 0)
        ent6.insert(0, 0)

    if tag == 'rot':
        ent4.delete(0, END)
        ent5.delete(0, END)
        ent7.delete(0, END)
        ent4.insert(0, 5)
        ent5.insert(0, 0)
        ent7.insert(0, 0)


def click(event):
    global res_coords, rot_coords

    if event.x < 65 or event.x > 665+dx or event.y < 210 or event.y > 810+dy:
        return

    if var.get():
        rot_coords.append(canv_to_net(event.x, event.y) + [var.get() + 1])
        if len(rot_coords) > 1:
            story.append(f'reprint_dot({rot_coords[-2][:-1]}, {rot_coords[-2][-1]});rot_coords.pop()')
        else:
            story.append(f'del_with_tag("rot")' + ';rot_coords.pop()' if len(rot_coords) else '')
    else:
        res_coords.append(canv_to_net(event.x, event.y) + [var.get() + 1])
        if len(res_coords) > 1:
            story.append(f'reprint_dot({res_coords[-2][:-1]}, {res_coords[-2][-1]});res_coords.pop()')
        else:
            story.append(f'del_with_tag("sz")' + ';res_coords.pop()' if len(res_coords) else '')

    global rotate_point, resize_point
    if var.get():
        rotate_point = canv_to_net(event.x, event.y)
        reprint_dot(rotate_point)
    else:
        resize_point = canv_to_net(event.x, event.y)
        reprint_dot(resize_point)


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
        dotts = c.find_withtag('sz')
        for dot in dotts:
            c.delete(dot)
        ent3.delete(0, END)
        ent6.delete(0, END)
        ent3.insert(END, f'{coords[0]:g}')
        ent6.insert(END, f'{coords[1]:g}')
        c.create_oval(x1, y1, x2, y2, outline='red', fill='red', tag='sz', activeoutline='lightgreen',
                      activefill='lightgreen')
        c.create_text(x1 - 5, y1 - 9, text='⇖', fill='green', tag='sz', font='Arial 20')
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
        c.create_oval(x1, y1, x2, y2, outline='red', fill='red', tag='rot', activeoutline='lightgreen',
                      activefill='lightgreen')
        c.create_text(x1 + 2, y1 - 2, text='↻', fill='green', tag='rot', font='Helvetica 40')


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

    foxx = c.find_withtag('fox')
    for elem in foxx:
        c.delete(elem)
    fox.analyze_and_redraw()
    fox.draw()

    del story[-1]


def scale(x, y):
    global sz
    prev_sz = sz
    while x < (150 + dx/4) * sz and y < (150 + dy/4) * sz:
        sz /= 2

    while x > (300 + dx/2) * sz or y > (300 + dy/2) * sz:
        sz *= 2

    if sz != prev_sz:
        redraw()


def redraw():
    global sz

    coords = c.find_withtag('coord')
    for cor in coords:
        c.delete(cor)

    max_len = 0
    for i in range(65, 665+dx, 50):
        if len(f'{round((i - 365) * sz, 3):g}') > max_len:
            max_len = len(f'{round((i - 365) * sz, 3):g}')

    for i in range(65, 665+dx, 50):
        c.create_text(i, 530+dy/2, fill='grey', text=f'{round((i - center[0]) * sz, 3):g}', tag='coord',
                      font='Verdana 8' if max_len > 6 else 'Verdana 12')

    for i in range(210, 810+dy, 50):
        c.create_text(345+dx/2, i + 10, fill='grey', text=f'{round(-(i - center[1]) * sz, 3):g}', tag='coord')


def text_and_labels_creation():
    label1.place(x=60, y=5)
    label2.place(x=280, y=5)
    label3.place(x=535, y=5)
    label4.place(x=35, y=43)
    label5.place(x=290, y=43)
    label6.place(x=295, y=82)
    label7.place(x=295, y=112)
    label8.place(x=545, y=82)
    label9.place(x=545, y=112)
    label10.place(x=491, y=90)
    label11.place(x=535, y=43)
    label12.place(x=241, y=90)
    label13.place(x=403, y=42)
    label14.place(x=653, y=42)
    label15.place(x=150, y=7)
    label16.place(x=425, y=7)
    label17.place(x=613, y=7)
    label18.place(x=20, y=120)
    label19.place(x=70, y=25)
    label20.place(x=115, y=25)
    label21.place(x=320, y=25)
    label22.place(x=365, y=25)


def buttons_creation():
    btn_res_l.place(x=330, y=150)
    btn_res_r.place(x=360, y=150)
    btn_mv_r.place(x=128, y=100)
    btn_mv.place(x=165, y=43)
    btn_mv_l.place(x=85, y=100)
    btn_mv_u.place(x=106, y=75)
    btn_mv_d.place(x=106, y=125)
    btn_cl_all.place(x=25, y=170)
    btn_rot_r.place(x=620, y=150)
    btn_rot_l.place(x=590, y=150)
    btn_back.place(x=25, y=140)
    btn_exit.place(x=630, y=840)


def coordinate_field_creation():
    global center
    center[0] = 365 + dx/2
    center[1] = 510 + dy/2
    clean_coords()
    c.create_line(33, 510+dy/2, 690+dx, 510+dy/2, fill='grey',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6", tag='net')
    c.create_line(365+dx/2, 820+dy, 365+dx/2, 185, fill='grey',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6", tag='net')
    c.create_line(665+dx, 210, 665+dx, 810+dy, fill='black',
                  width=1, dash=(5, 9), tag='net')
    c.create_line(65, 810+dy, 665+dx, 810+dy, fill='black',
                  width=1, dash=(5, 9), tag='net')
    c.create_line(65, 210, 665+dx, 210, fill='black',
                  width=1, dash=(5, 9), tag='net')
    c.create_line(65, 210, 65, 810+dy, fill='black',
                  width=1, dash=(5, 9), tag='net')
    # c.create_text(355+dx/2, 520+dy/2, text='0', tag='coord')

    for i in range(65, 665+dx, 50):
        c.create_line(i, 503+dy/2, i, 520+dy/2, fill='grey', width=2, tag='net')
        c.create_line(i, 210, i, 810+dy, fill='grey', width=1, dash=(1, 9), tag='net')
        # c.create_text(i, 530+dy/2, text=f'{i - center[0]}', fill='grey', tag='coord')

    for i in range(210, 810+dy, 50):
        c.create_line(358+dx/2, i, 372+dx/2, i, fill='grey', width=2, tag='net')
        c.create_line(65, i, 665+dx, i, fill='grey', width=1, dash=(1, 9), tag='net')
        # c.create_text(345+dx/2, i + 10, text=f'{-(i - center[1])}', fill='grey', tag='coord')

    c.create_text(688+dx, 498+dy/2, text='X', font='Verdana 20', fill='green', tag='net')
    c.create_text(380+dx/2, 195, text='Y', font='Verdana 20', fill='green', tag='net')
    redraw()


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


def start_state():
    global story, rot_coords, res_coords, fox
    scale(200, 200)
    story = []
    res_coords = []
    rot_coords = []
    clean_all()
    ent1.insert(0, 15)
    ent2.insert(0, 1.1)
    ent3.insert(0, 0)
    ent4.insert(0, 5)
    ent5.insert(0, 0)
    ent6.insert(0, 0)
    ent7.insert(0, 0)
    ent8.insert(0, 1.3)
    ent9.insert(0, 5)
    ent10.insert(0, 15)
    fox = Fox(load_and_transf_coords('data.txt'))
    fox.draw()


old_dx, old_dy = dx, dy
def config(event):
    global dx, dy, old_dx, old_dy, rotate_point, resize_point
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

        old_dx, old_dy = dx, dy
        dx = window.winfo_width() - win_size[0]
        dy = window.winfo_height() - win_size[1]
        coordinate_field_creation()
        fox.upd_coords((dx-old_dx)/2, (dy-old_dy)/2)
        # r_point_canv = net_to_canv(rotate_point)

        # rotate_point = [rotate_point[0] + (dx-old_dx)/2, rotate_point[1] + (dy-old_dy)/2]
        # rotate_point = canv_to_net(r_point_canv[0] + (dx-old_dx)/2, r_point_canv[1] + (dy-old_dy)/2)
        # reprint_dot(rotate_point, 2)
        reprint_dot([ent3.get(), ent6.get()], 1)
        reprint_dot([ent5.get(), ent7.get()], 2)
        fox.analyze_and_redraw()
        fox.draw()

        print(fox.coords)
        print(center)
        c.place(x=0, y=0)


fox = Fox(load_and_transf_coords('data.txt'))

c.bind('<1>', click)
window.bind("<Command-r>", lambda event: fox.rotate(ent4.get(), net_to_canv(ent5.get(), ent7.get())))
window.bind("<Shift-Command-r>", lambda event: fox.rotate('-' + ent4.get(), net_to_canv(ent5.get(), ent7.get())))
window.bind("<Command-Up>", lambda event: fox.resize(1, ent2.get(), ent8.get(), net_to_canv(ent3.get(), ent6.get())))
window.bind("<Command-Down>", lambda event: fox.resize(-1, ent2.get(), ent8.get(), net_to_canv(ent3.get(), ent6.get())))
window.bind("<Up>", lambda event: fox.move(ent10.get(), 'up'))
window.bind("<Down>", lambda event: fox.move(ent10.get(), 'down'))
window.bind("<Right>", lambda event: fox.move(ent10.get(), 'right'))
window.bind("<Left>", lambda event: fox.move(ent10.get(), 'left'))
window.bind("<Command-z>", lambda event: back())
window.bind("<Configure>", config)

text_and_labels_creation()
buttons_creation()
coordinate_field_creation()
radiobutton_creation()
default_fox_coords = load_and_transf_coords('data.txt')
# coords = load_and_transf_coords('data.txt')
fox.draw()

mmenu = Menu(window)
add_menu = Menu(mmenu)
add_menu.add_command(label='О программе и авторе',
                     command=lambda: messagebox.showinfo('О программе и авторе', TASK + AUTHOR))
add_menu.add_command(label='Выход', command=exit)
mmenu.add_cascade(label='About', menu=add_menu)
window.config(menu=mmenu)

c.pack()
window.mainloop()

from tkinter import *
import tkinter.messagebox as box

root = Tk()
var = IntVar()
c = Canvas(root, width=700, height=900, bg='white')
c.create_rectangle(4, 32, 266, 172, outline='black', width=2)
c.create_rectangle(429, 32, 691, 172, outline='black', width=2)
text1 = Text(width=36, height=10)
text2 = Text(width=36, height=10)
ent1 = Entry(width=8)
ent2 = Entry(width=8)
ent1.place(x=32, y=177)
ent2.place(x=132, y=177)
ent3 = Entry(width=8)
ent4 = Entry(width=8)
ent3.place(x=460, y=177)
ent4.place(x=560, y=177)
sz = 1
flag1 = 0
flag2 = 0

def clean_tri():
    triangls = c.find_withtag('triang')
    for tri in triangls:
        c.delete(tri)

def clean_all():
    global flag1, flag2
    flag1, flag2 = 0, 0
    clean_tri()
    dotts = c.find_withtag('dot')
    for dot in dotts:
        c.delete(dot)
    text1.delete(1.0, END)
    text2.delete(1.0, END)

def clean_coords():
    coords = c.find_withtag('coord')
    for cor in coords:
        c.delete(cor)

def tri_click(event, tag):
    triangls = list(c.find_withtag('triang'))
    triangls.remove(tag)
    for tri in triangls:
        c.delete(tri)

def add_dot(num):
    if num == 1:
        d1 = ent1.get()
        d2 = ent2.get()
    else:
        d1 = ent3.get()
        d2 = ent4.get()

    try:
        d1 = float(d1)
        d2 = float(d2)

        if num == 1:
            text1.insert(END, f'({d1:g}; {d2:g})\n')
        else:
            text2.insert(END, f'({d1:g}; {d2:g})\n')
        dots_update()
    except:
        box.showinfo('Error', 'Некорректные координаты!1')

def is_cursor_touch_triang(tri, event):
    coo = c.coords(tri)[:-2]

    x0, y0 = event.x, event.y
    x1, y1 = int(coo[0]), int(coo[1])
    x2, y2 = int(coo[2]), int(coo[3])
    x3, y3 = int(coo[4]), int(coo[5])

    d1 = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
    d2 = ((x0 - x2) ** 2 + (y0 - y2) ** 2) ** 0.5
    d3 = ((x0 - x3) ** 2 + (y0 - y3) ** 2) ** 0.5

    a1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    a2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    a3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

    cos1 = (d1 ** 2 + d2 ** 2 - a1 ** 2) / 2 / d1 / d2
    cos2 = (d2 ** 2 + d3 ** 2 - a2 ** 2) / 2 / d2 / d3
    cos3 = (d1 ** 2 + d3 ** 2 - a3 ** 2) / 2 / d1 / d3

    if abs(cos1 + 1) < 1e-3 or abs(cos2 + 1) < 1e-3 or abs(cos3 + 1) < 1e-3:
        return 1
    else:
        return 0

def click(event):
    global flag1, flag2
    triangls = c.find_withtag('triang')
    for tri in triangls:
        if is_cursor_touch_triang(tri, event):
            tri_click(event, tri)
            return

    if event.x < 65 or event.x > 665 or event.y < 210 or event.y > 810:
        return

    print_dot(event)

    crds = canv_to_net(event.x, event.y)
    if var.get():
        flag2 += 1
        text2.insert(END, f'({crds[0]:g}; {crds[1]:g})\n')
    else:
        flag1 += 1
        text1.insert(END, f'({crds[0]:g}; {crds[1]:g})\n')

def print_dot(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    if var.get():
        c.create_oval(x1, y1, x2, y2, outline='blue', fill='blue', tag='dot')
    else:
        c.create_oval(x1, y1, x2, y2, outline='red', fill='red', tag='dot')

def dots_update():
    # sett1 = text1.get(1.0, END).split(',')[:-1] if text1.get(1.0, END).split(',')[-1].strip() == '' \
    #     else text1.get(1.0, END).split(',')
    # sett2 = text2.get(1.0, END).split(',')[:-1] if text2.get(1.0, END).split(',')[-1].strip() == '' \
    #     else text2.get(1.0, END).split(',')

    sett1 = text1.get(1.0, END).split('\n')[:-1]

    if not sett1[-1]:
        sett1 = sett1[:-1]

    sett2 = text2.get(1.0, END).split('\n')[:-1]

    if not sett2[-1]:
        sett2 = sett2[:-1]

    dotts = c.find_withtag('dot')

    for dot in dotts:
        c.delete(dot)

    clean_tri()

    try:
        xs = []
        ys = []
        for dot in sett1:
            x, y = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
            xs.append(abs(x))
            ys.append(abs(y))
        for dot in sett2:
            x, y = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
            xs.append(abs(x))
            ys.append(abs(y))
        max_x, max_y = max(xs), max(ys)
        scale(max_x, max_y)
    except:
        box.showinfo('Error', 'Некорректные координаты!2')
        return

    for dot in sett1:
        x, y = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
        x, y = net_to_canv(x, y)
        x2, y2 = x + 2, y + 2
        x -= 2
        y -= 2
        c.create_oval(round(x), round(y), round(x2), round(y2), outline='red', fill='red', tag='dot')

    for dot in sett2:
        x, y = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
        x, y = net_to_canv(x, y)
        x2, y2 = x + 2, y + 2
        x -= 2
        y -= 2
        c.create_oval(round(x), round(y), round(x2), round(y2), outline='blue', fill='blue', tag='dot')

    # try:
    #     for dot in sett1:
    #         x1, y1 = map(int, dot.strip(' ').strip('\n').strip(')').strip('(').split(';'))
    #         if x1 < 0 or x1 > 650 or y1 < 0 or y1 > 540:
    #             raise
    #         x2, y2 = x1 + 2, y1 + 2
    #         x1 -= 2
    #         y1 -= 2
    #         c.create_oval(x1 + 40, y1 + 210, x2 + 40, y2 + 210, outline='red', fill='red', tag='dot')
    #     for dot in sett2:
    #         x1, y1 = map(int, dot.strip(' ').strip('\n').strip(')').strip('(').split(';'))
    #         if x1 < 0 or x1 > 650 or y1 < 0 or y1 > 540:
    #             raise
    #         x2, y2 = x1 + 2, y1 + 2
    #         x1 -= 2
    #         y1 -= 2
    #         c.create_oval(x1 + 40, y1 + 210, x2 + 40, y2 + 210, outline='blue', fill='blue', tag='dot')
    # except:
    #     box.showinfo('Error', 'Некорректные координаты!')

def net_to_canv(x, y):
    global sz
    center = (365, 510)

    return round(x/sz + center[0]), round(center[1] - y/sz)

def canv_to_net(x, y):
    global sz
    center = (365, 510)

    return round((x - center[0])*sz, 3), round((center[1] - y)*sz, 3)


def scale(x, y):
    global sz
    prev_sz = sz
    center = (365, 510)
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
        c.create_text(i, 530, text=f'{round((i - 365)*sz, 3):g}' if i - 365 else '', tag='coord',
                      font='Verdana 8' if max_len > 6 else 'Verdana 12')

    for i in range(210, 820, 50):
        c.create_text(345, i + 10, text=f'{round(-(i - 510)*sz, 3):g}' if i - 510 else '', tag='coord')

def is_count_true(set1, set2, a, b, c):
    count1 = 0
    count2 = 0
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    for dot in set1:
        x0, y0 = dot
        k1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
        k2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
        k3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
        if k1 > 0 and k2 > 0 and k3 > 0 or k1 < 0 and k2 < 0 and k3 < 0:
            count1 += 1

    for dot in set2:
        x0, y0 = dot
        k1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
        k2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
        k3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
        if k1 > 0 and k2 > 0 and k3 > 0 or k1 < 0 and k2 < 0 and k3 < 0:
            count2 += 1

    return count1 == count2 and count1

def triang_find_and_draw():
    dots_update()
    # sett1 = text1.get(1.0, END).split(',')[:-1] if text1.get(1.0, END).split(',')[-1].strip() == '' \
    #     else text1.get(1.0, END).split(',')
    # sett2 = text2.get(1.0, END).split(',')[:-1] if text2.get(1.0, END).split(',')[-1].strip() == '' \
    #     else text2.get(1.0, END).split(',')

    sett1 = text1.get(1.0, END).split('\n')[:-1]
    if not sett1[-1]:
        sett1 = sett1[:-1]

    sett2 = text2.get(1.0, END).split('\n')[:-1]
    if not sett2[-1]:
        sett2 = sett2[:-1]

    set1_t = []
    set2_t = []

    for dot in sett1:
        x1, y1 = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
        set1_t.append((x1, y1))

    for dot in sett2:
        x1, y1 = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
        set2_t.append((x1, y1))

    for i in range(len(set1_t) - 2):
        for j in range(i + 1, len(set1_t) - 1):
            for k in range(j + 1, len(set1_t)):
                a = set1_t[:]
                del a[i], a[j - 1], a[k - 2]
                if is_count_true(a, set2_t, set1_t[i], set1_t[j], set1_t[k]):
                    c.create_line(net_to_canv(set1_t[i][0], set1_t[i][1]),
                                  net_to_canv(set1_t[j][0], set1_t[j][1]),
                                  net_to_canv(set1_t[k][0], set1_t[k][1]),
                                  net_to_canv(set1_t[i][0], set1_t[i][1]), fill='green', width=2,
                                  activefill='lightgreen', tag='triang')

def text_and_labels_creation():
    text1.place(x=20, y=33)
    scroll = Scrollbar(command=text1.yview)
    scroll.pack(side=LEFT, fill=Y)
    text1.config(yscrollcommand=scroll.set)

    text2.place(x=445, y=33)
    scroll = Scrollbar(command=text2.yview)
    scroll.pack(side=RIGHT, fill=Y)
    text2.config(yscrollcommand=scroll.set)

    label1 = Label(text='Точки первого множества:', font='Arial 15')
    label2 = Label(text='Точки второго множества:', font='Arial 15')
    c.create_text(348, 25, text='Выбирать на поле точки:', font='Verdana 10')
    label1.place(x=13, y=5)
    label2.place(x=440, y=5)

def buttons_creation():
    btn_upd = Button(root, text='обновить точки', fg='green', command=lambda: dots_update())
    # btn_upd = Button(root, text='обновить точки', fg='green', command=lambda: dots_update())
    btn_add1 = Button(root, text='добавить', fg='red', command=lambda: add_dot(1))
    btn_add2 = Button(root, text='добавить', fg='blue', command=lambda: add_dot(2))
    btn_tri = Button(root, text='найти ΔΔ', fg='blue', command=lambda: triang_find_and_draw())
    btn_cl_tri = Button(root, text='🗑ΔΔ', fg='orange', command=lambda: clean_tri())
    btn_cl_all = Button(root, text='🗑всё', fg='orange', command=lambda: clean_all())
    btn_exit = Button(root, text=' выход ', fg='red', command=exit)
    btn_cl_tri.place(x=285, y=140)
    btn_add1.place(x=220, y=180)
    btn_add2.place(x=648, y=180)
    btn_cl_all.place(x=365, y=140)
    btn_upd.place(x=310, y=80)
    # btn_upd.place(x=310, y=80)
    btn_tri.place(x=327, y=110)
    btn_exit.place(x=650, y=840)

def coordinate_field_creation():
    c.create_line(33, 510, 690, 510, fill='black',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6")
    c.create_line(365, 820, 365, 185, fill='black',
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

    c.create_text(10, 190, text='X:')
    c.create_text(110, 190, text='Y:')
    c.create_text(438, 190, text='X:')
    c.create_text(538, 190, text='Y:')

    for i in range(65, 750, 50):
        c.create_line(i, 503, i, 520, fill='black', width=2)
        c.create_line(i, 210, i, 810, fill='black', width=1, dash=(1, 9))
        c.create_text(i, 530, text=f'{i - 365}' if i - 365 else '', tag='coord')

    for i in range(210, 820, 50):
        c.create_line(358, i, 372, i, fill='black', width=2)
        c.create_line(65, i, 665, i, fill='black', width=1, dash=(1, 9))
        c.create_text(345, i+10, text=f'{-(i - 510)}' if i - 510 else '', tag='coord')

    c.create_text(688, 498, text='X', font='Verdana 20', fill='green')
    c.create_text(380, 195, text='Y', font='Verdana 20', fill='green')

def radiobutton_creation():
    var.set(0)
    set0 = Radiobutton(text="1-го мн-ва", fg='red', variable=var, value=0)
    set1 = Radiobutton(text="2-го мн-ва", fg='blue', variable=var, value=1)
    set0.place(x=290, y=33)
    set1.place(x=290, y=55)


c.bind('<1>', click)

text_and_labels_creation()
buttons_creation()
coordinate_field_creation()
radiobutton_creation()

c.pack()
root.mainloop()